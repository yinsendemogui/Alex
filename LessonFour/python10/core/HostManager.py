#!usr/bin/env python
# -*- coding:utf-8 -*-
# auther:Mr.chen
# 描述：只能运行在MacOS或linux系统下


import os,sys,pickle,time
import paramiko,threading



sys.path.append('..')
PATH = os.path.dirname(os.path.abspath(__file__))
PUT_PATH = PATH.replace('core','Folder/')
GET_PATH = PATH.replace('core','download/')
CONF_PATH = PATH.replace('core','conf/')
semaphore = threading.BoundedSemaphore(1) # 进程锁

def new_Host():
    while True:
        hostname = raw_input("请输入服务器的主机名(输入n=返回上级)：")
        if os.path.exists(CONF_PATH+hostname+'_conf'):
            print ("主机名已存在，请重新输入！")
            continue
        if hostname =='n':
            return
        port = raw_input("请输入服务器的ssh端口号(输入n=返回上级)：")
        if port == 'n':
            return
        username = raw_input("请输入登陆的用户名(输入n=返回上级)：")
        if username == 'n':
            return
        password = raw_input("请输入用户的密码(输入n=返回上级)：")
        if password == 'n':
            return
        dic = {
            'hostname':hostname,    # 主机名
            'port':port,            # 端口
            'username':username,    # 用户名
            'password':password,    # 密码
            'status':0              # 状态(0:未激活 1：已激活 2：激活失败)
        }
        if os.path.isdir(GET_PATH + hostname) == False:
            command = 'mkdir ' + GET_PATH + hostname
            os.system(command)
        re = hostmessage_Write(dic)
        if re == True:
            return
        else:
            print ("主机信息存储失败，请检查原因！")



def delete_Host():
    List = Traverse_folder()
    while True:
        dic = {}
        num = 0
        print ("已存在的主机列表如下：")
        for i in List:
            print ("{0}，主机名：{1}".format(str(num+1),i))
            dic[str(num+1)] = i
            num += 1
        choose = raw_input("请输入你想删除的主机索引(输入n=返回上级)：")
        if choose == 'n':
            return
        elif choose in dic:
            hostname = dic[choose]
            command = 'rm -f '+CONF_PATH+hostname+'_conf'
            os.system(command)
            print ("删除成功！")
            break
        else:
            print ("您的输入有误！")



def auto_activeHost():
    text = """
            警告！程序准备开启多线程模式激活主机，请确保：
            1，远程服务器处于开启状态
            2，DNS或本地hosts映射能够解析远程服务器主机名
    """
    while True:
        print (text)
        choose = raw_input("是否确定开始激活远程主机（y/n）？:")
        if choose == 'n':
            return
        elif choose == 'y':
            break
        else:
            print ("你的输入有误！")
    print ("程序开始自动激活远程主机，请稍后...")
    List = Traverse_folder()
    if len(List) == 0:
        print ("请先创建主机！")
        return
    for i in List:
        dic = hostmessage_Read(i)
        t = threading.Thread(target=auto_Active,args=(dic,)) # 创建多线程对象
        t.setDaemon(True)  # 将对象设置为守护线程
        t.start() # 线程开启
    while threading.activeCount() != 1:    # 当前活跃的线程数
        pass
    else:
        print ("所有主机激活完毕！")
        time.sleep(2)


def auto_Active(dic):
    ssh = paramiko.SSHClient()  # 创建ssh对象
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #允许连接不在know_hosts文件中的主机
    try:
        ssh.connect(hostname=dic['hostname'],port=int(dic['port']),username=dic['username'],password=dic['password'],timeout=10)
    except Exception,e:
        print ("主机名：{0}的主机激活失败！失败原因：{1}".format(dic['hostname'],e))
        dic['status'] = 2
        hostmessage_Write(dic)
    else:
        print ("主机名：{0}的主机激活成功！".format(dic['hostname']))
        dic['status'] = 1
        hostmessage_Write(dic)
    finally:
        ssh.close()


def remote_Host():
    List = Traverse_folder(key='status',value=1)
    if len(List) == 0:
        print ("请先激活主机！")
        return
    while True:
        dic = {}
        print ("已激活主机如下：")
        num = 0
        for i in List:
            print ("{0},主机名：{1}".format(str(num+1),i))
            dic[str(num+1)] = i
            num += 1
        choose = raw_input("请输入你想操控的主机的索引（可多选,n=返回上级）：")
        if choose == 'n':
            return
        choose = list(set(choose)) #去重复
        if set(choose) & set(dic.keys()) == set(choose):
            LIST = []
            for i in choose:
                LIST.append(dic[i])
            remote_Host_control(LIST)
        else:
            print ("您的输入有误！")


def remote_Host_control(List):
    help = """
                    help帮助提示：
            1.程序的Folder目录是本地文件目录
            2，输入put向远程主机上传文件
            3，输入get向远程主机下载文件
            4，输入其他直接向远程主机发布命令
    """
    while True:
        print ("正在操控{0}台主机，如下：".format(len(List)))
        for i in List:
            print ("主机名：{0}".format(i))
        command = raw_input("请输入你想执行的命令（输入n=返回上级，输入help获取帮助）：>>")
        if command == 'n':
            return
        elif command == 'help':
            print help
        elif command == 'get':
            print ("程序准备下载文件...")
            remote_path = raw_input("请输入想要下载的远程服务器文件绝对路径（例如：／etc/hosts）：")
            LIST = remote_path.split('/')
            filename = LIST[len(LIST)-1]
            for i in List:
                local_path = GET_PATH + i + '/'+filename
                t = threading.Thread(target=get_Method,args=(i,[remote_path,local_path]))
                t.setDaemon(True)
                t.start()
            while threading.activeCount() != 1:
                pass
            else:
                print ("命令执行完毕！")
        elif command == 'put':
            print ("程序准备上传文件...")
            while True:
                filename = raw_input("请输入想上传的文件的文件名：")
                if os.path.exists(PUT_PATH+filename) == False:
                    print ("文件没有找到，请重新输入！")
                    continue
                local_path= PUT_PATH+filename
                remote_path = raw_input("你想将文件保存到远程服务器的哪里？（例如：／etc/）：")
                remote_path = remote_path + '/' + filename
                for i in List:
                    t = threading.Thread(target=put_Method, args=(i, [local_path,remote_path]))
                    t.setDaemon(True)
                    t.start()
                while threading.activeCount() != 1:
                    pass
                else:
                    print ("命令执行完毕！")
                    break
        else:
            for i in List:
                t = threading.Thread(target=execute_Command,args=(i,command))
                t.setDaemon(True)
                t.start()
            while threading.activeCount() != 1:
                pass
            else:
                print ("命令执行完毕！")

def put_Method(hostname,Path):
    dic = hostmessage_Read(hostname)
    transport = paramiko.Transport((hostname, int(dic['port'])))
    try:
        transport.connect(username=dic['username'], password=dic['password'])
        sftp = paramiko.SFTPClient.from_transport(transport)
        sftp.put(Path[0], Path[1])
    except Exception, e:
        print ("主机名：{0},上传失败！错误原因：{1}".format(hostname, e))
    else:
        pass
    finally:
        transport.close()


def get_Method(hostname,Path):
    dic = hostmessage_Read(hostname)
    transport = paramiko.Transport((hostname,int(dic['port'])))
    try:
        transport.connect(username=dic['username'],password=dic['password'])
        sftp = paramiko.SFTPClient.from_transport(transport)
        sftp.get(Path[0],Path[1])
    except Exception,e:
        print ("主机名：{0},下载失败！错误原因：{1}".format(hostname,e))
    else:
        pass
    finally:
        transport.close()

def execute_Command(hostname,command):
    dic = hostmessage_Read(hostname)
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(hostname=hostname,port=int(dic['port']),username=dic['username'],password=dic['password'])
        command_list = command.strip().split(';')
    except Exception,e:
        semaphore.acquire()     # 进程锁开启
        print ("主机：{0}连接出现异常:{1}".format(hostname,e))
        semaphore.release()     # 进程锁释放
        return
    for com in command_list:
        stdin, stdout, stderr = ssh.exec_command(com)
        error = stderr.read()
        output = stdout.read()
        semaphore.acquire()     # 进程锁开启
        if len(error) != 0:
            print ("主机：{0} 执行{1}命令时出错：{2}".format(hostname,com, error))
        if len(output) != 0:
            print ("主机：{0},执行{1}命令的结果如下：".format(hostname,com))
            print (output)
        semaphore.release()     # 进程锁释放




def Traverse_folder(key = None,value = None):
    '''
    根据条件遍历某文件夹里的全部文件内容，
    找出符合条件的文件返回包含主机名的列表
    如果无条件，则返回包含所有主机名的列表
    :return:LIST
    '''
    LIST = []
    List = os.listdir(CONF_PATH)
    for i in List:
        if i == '__init__.py' or i == '__init__.pyc' or i =='.DS_Store':
            continue
        else:
            with open(CONF_PATH+i,'r') as f:
                dic = pickle.load(f)
            if key != None:
                if dic[key] == value:
                    LIST.append(dic['hostname'])
            else:
                LIST.append(dic['hostname'])
    return LIST



def hostmessage_Write(dic):
    with open(CONF_PATH+dic['hostname']+'_conf','w') as f:
        pickle.dump(dic,f)
        return True


def hostmessage_Read(hostname):
    if os.path.exists(CONF_PATH+hostname+'_conf'):
        with open(CONF_PATH+hostname+'_conf','r') as f:
            dic = pickle.load(f)
            return dic



def Main():
    text = """
            欢迎来到Fabric主机管理界面
                1,创建主机
                2,删除主机
                3,自动激活所有主机
                4,开始远程操控
                5,退出程序
    """
    while True:
        print text
        choose = raw_input("请输入你的选择：")
        dic = {'1':new_Host,'2':delete_Host,'3':auto_activeHost,'4':remote_Host,'5':Exit}
        if choose in dic:
            dic[choose]()
        else:
            print ("你的输入有误！")



def Exit():
    print ("程序退出！")
    exit()







if __name__ == "__main__":
    Main()







