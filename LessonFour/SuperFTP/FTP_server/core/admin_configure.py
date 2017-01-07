#!usr/bin/env python
# -*- coding:utf-8 -*-
# auther:Mr.chen
# 描述：
import os,sys
import pickle

DIR = os.path.dirname(os.path.abspath(__file__))
DIR = DIR.replace('core','conf/')    #用户配置文件目录路径
DIRR =DIR.replace('conf','Folder')   #用户家目录路径


def user_list():
    pass


def user_register():
    while True:
        name = raw_input("请输入要注册的用户的用户名：")
        quota = raw_input("请输入要注册的用户的磁盘配额(范围10-100)M：")
        if quota.isdigit() != True:
            print ("磁盘配额只能是数字！请重新输入！")
            continue
        if int(quota) < 10 or int(quota) > 100:
            print ("磁盘配额只能在10-100之间，请重新输入！")
            continue
        quota = str(int(quota)*1000000)
        password = MD5('88888888')
        dict = {
                'Name':name,                    # 用户名
                'Password':password,            # 用户密码
                'Quota':quota,                  # 用户磁盘配额
                'Home_path':DIRR+name+'/',      # 用户家目录路径
                'Current_path':DIRR+name+'/'    # 用户当前路径
        }
        re = config_read(name)
        if re == None:
            config_write(dict)
            Mkdir(dict)
            print ("用户注册成功！")
            return
        else:
            print ("{0}这个用户已经注册！".format(name))


def Mkdir(dict):
    if not os.path.exists(dict['Home_path']):
        os.system('mkdir'+' '+dict['Home_path'])
    else:
        print ("新建用户的家目录已经存在。")



def Exit():
    print ("系统退出！")
    exit()


def config_read(username):
    """
    配置文件全部读取
    :return:
    """
    if os.path.exists(DIR+username+'_config'):
        with open(DIR+username+'_config','r') as f:
            dict = pickle.load(f)
            return dict


def config_write(dict):
    """
    配置文件全部写入
    :param dict:
    :return:
    """
    with open(DIR+dict['Name']+'_config', 'w') as f:
        pickle.dump(dict,f)
        return True


def MD5(password):
    """
    加密函数
    :param password:
    :return:
    """
    import hashlib
    return hashlib.md5(password).hexdigest()



def Main():
    while True:
        text = """
                    欢迎来到管理员管理界面
                        1，查看用户列表
                        2，FTP用户注册
                        3，退出系统
            """
        print (text)
        choose = raw_input("请输入你的选择：")
        if choose == '1':
            user_list()
        elif choose == '2':
            user_register()
        elif choose == '3':
            Exit()
        else:
            print ("你的输入有误！")






if __name__ == "__main__":

    Main()


