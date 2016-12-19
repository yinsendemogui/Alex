#!usr/bin/env python
# -*- coding:utf-8 -*-
# auther:Mr.chen
# 描述：

import socket,os
import time,json


DIR = os.path.dirname(os.path.abspath(__file__))
DIR = DIR.replace('core','Folder/')
HOST = 'localhost'
PORT = 8888


# def Recvfile(s,filename):
#     """
#     接收文件方法函数
#     :param s: 套接字封装对象
#     :param filename: 目标文件名
#     :return:
#     """
#     print ("开始下载文件...")
#     buffer = []
#     while TAG:
#         d = s.recv(4096)
#         if d == 'exit':
#             break
#         buffer.append(d)
#     data = ''.join(buffer)
#     with open(DIR+filename,'w') as f:
#         f.write(data)
#     print ("文件下载完毕！")
#
#
# def Sendfile(s,filename):
#     """
#     放送文件方法函数
#     :param s: 套接字封装对象
#     :param filename: 目标文件名
#     :return:
#     """
#     print ("开始上传文件！")
#     if os.path.exists(DIR+filename):
#         with open(DIR+filename,'r') as f:
#             data = f.read()
#             data_size = len(data)
#             s.send(data_size)
#             if s.recv(1024) == 'OK':
#
#                 data_size = len(data)
#                 s.send(data_size)
#                 time.sleep(0.5)
#                 s.sendall(data)
#         time.sleep(1)
#         s.send('exit')
#         print ("文件上传完毕")
#     else:
#         print ("你的目录里没有这个文件")
#         time.sleep(1)
#         s.send('exit')
#
#
#
#
# def Confirm(s,command):
#     """
#     验证与服务器连接是否正常；
#     把用户命令发过去，让服务器做好相应准备准备
#     :param s: 套接字封装对象
#     :param command: 用户输入的命令
#     :return:
#     """
#     s.sendall(command)
#     re = s.recv(4096)
#     if re == 'Ready!':
#         return True
#     elif re == 'False!':
#         return False
#     else:
#         print ("与服务器连接出现异常！")


def ls_Method(s):
    pass


def put_Method(s,action,filename):
    pass


def get_Method(s,action,filename):
    pass


def cd_Method(s,action,filename):
    pass


def mkdir_Method(s,action,filename):
    pass


def rm_Method(s,action,filename):
    pass


def MD5(password):
    """
    加密函数
    :param password:
    :return:
    """
    import hashlib
    return hashlib.md5(password).hexdigest()


def File_transfer(s):
    """
    用户指令函数
    :param s:
    :return:
    """

    while True:
        command = raw_input("请输入你想执行的命令>>")
        if not command:
            continue
        if command.lower().strip() == 'help':
            text = """
                    请用'put'+'空格'+'文件名'的格式上传文件
                    请用'get'+'空格'+'文件名'的格式下载文件
                    请用'cd'+'空格'+'目录名'的格式进入家目录下的子文件夹
                    请用'cd'+'空格'+'..'的格式退出家目录下的子文件夹
                    请用'mkdir'+'空格'+'目录名'的格式进入家目录的文件夹
                    请用'rm'+'空格'+'文件名／目录名'的格式删除家目录下的文件
                    输入'ls'查看用户服务器家目录
            """
            print (text)
            continue
        try:
            action,filename = command.strip().split()
            action = action.lower()
        except:
            if command.lower().strip() == 'ls':
                s.send('ls')
                if s.recv(1024) == 'OK!':
                    ls_Method(s)
            else:
                print ("您的输入有误!输入help查看帮助文档")
                continue
        else:
            s.send(action)
            if s.recv(1024) == 'OK!':
                eval(action+'_Method')(s,action,filename)
            else:
                print ("您的输入有误！输入help查看帮助文档")




def Login(s):
    """
    用户登录
    :param s:
    :return:
    """
    while True:
        name = raw_input("请输入你的登陆名：").strip()
        password = raw_input("请输入你的密码：").strip()
        if not name or not password:
            print ("用户名和密码不能为空！")
            continue
        password = MD5(password)   #密码加密
        data = [name,password]
        s.send(json.dumps(data))
        if s.recv(1024) == 'OK!':
            print ("用户登陆成功！")
            File_transfer(s)
        else:
            print ("用户登陆失败！")
            break






def Main():
    """
    用户登陆
    :param s:
    :param log:
    :return:
    """
    s = socket.socket()
    try:
        s.connect((HOST, PORT))
        s.recv(1024)  #接收服务器欢迎信息
        Login(s)
    except Exception,e:
        print "服务器连接不上....", e
    finally:
        s.close()


if __name__ == "__main__":
    Main()











