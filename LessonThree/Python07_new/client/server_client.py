#!usr/bin/env python
# -*- coding:utf-8 -*-
# auther:Mr.chen
# 描述：

import socket,os
import time
TAG =True

DIR = os.path.dirname(os.path.abspath(__file__))
DIR = DIR+'/Folder/'
HOST = 'localhost'
PORT = 8888


def Recvfile(s,filename):
    """
    接收文件方法函数
    :param s: 套接字封装对象
    :param filename: 目标文件名
    :return:
    """
    print ("开始下载文件...")
    buffer = []
    while TAG:
        d = s.recv(4096)
        if d == 'exit':
            break
        buffer.append(d)
    data = ''.join(buffer)
    with open(DIR+filename,'w') as f:
        f.write(data)
    print ("文件下载完毕！")


def Sendfile(s,filename):
    """
    放送文件方法函数
    :param s: 套接字封装对象
    :param filename: 目标文件名
    :return:
    """
    print ("开始上传文件！")
    if os.path.exists(DIR+filename):
        with open(DIR+filename,'r') as f:
            while TAG:
                data = f.read(4096)
                if not data:
                    break
                s.sendall(data)
        time.sleep(1)
        s.send('exit')
        print ("文件上传完毕")
    else:
        print ("你的目录里没有这个文件")
        time.sleep(1)
        s.send('exit')




def Confirm(s,command):
    """
    验证与服务器连接是否正常；
    把用户命令发过去，让服务器做好相应准备准备
    :param s: 套接字封装对象
    :param command: 用户输入的命令
    :return:
    """
    s.sendall(command)
    re = s.recv(4096)
    if re == 'Ready!':
        return True
    elif re == 'False!':
        return False
    else:
        print ("与服务器连接出现异常！")


def File_transfer(s):
    """
    用户指令函数
    :param s:
    :return:
    """
    while TAG:
        command = raw_input("请输入你想执行的命令>>")
        if not command:
            continue
        if command.lower().strip() == 'help':
            print ("请用'put'+'空格'+'文件名'的格式上传文件")
            print ("请用'get'+'空格'+'文件名'的格式下载文件")
            print ("输入'ls'查看用户服务器家目录")
            continue
        if command.lower().strip() == 'ls':
            s.send('ls')
            data = s.recv(4096)
            print (data)
            continue
        try:
            action,filename = command.strip().split()
            action = action.lower()
        except:
            print ("您的输入有误!输入help查看帮助文档")
            continue
        if action == 'put':
            re = Confirm(s,command)
            if re == True:
                Sendfile(s, filename)
            else:
                print ("对方服务器没有准备好！")
                break
        elif action == 'get':
            re = Confirm(s,command)
            if re == True:
                Recvfile(s, filename)
            elif re == False:
                print ("服务器家目录没有这个文件")
            else:
                print ("对方服务器没有准备好！")
                break
        else:
            print ("你输入的命令有误！输入help查看帮助文档")



def Login(s):
    """
    用户登录
    :param s:
    :return:
    """
    name = raw_input("请输入你的用户名：")
    password = raw_input("请输入你的密码：")
    command = 'login'+' '+ name + ',' + password
    re = Confirm(s, command)
    if re == True:
        print ("登陆成功！")
        File_transfer(s)
    elif re == False:
        print ("您的输入有误，请重新输入！")
        Login(s)
    else:
        print ("与服务器连接出现异常！")


def Register(s):
    """
    用户注册
    :param s:
    :return:
    """
    name = raw_input("请输入你的用户名：")
    password = raw_input("请输入你的密码：")
    Password = raw_input("请再次输入密码：")
    if password != Password:
        print ("你的密码两次输入不一致，请重新输入！")
        Register(s)
    command = 'register' + ' ' + name + ',' + password
    print (command)
    re = Confirm(s,command)
    if re == True:
        File_transfer(s)
    elif re == False:
        print ("用户名重复，请重新输入！")
        Register(s)
    else:
        print ("与服务器连接出现异常！")

def Main(s,log = '未联通主机...'):
    """
    用户登陆界面
    :param s:
    :param log:
    :return:
    """
    text = """
            用户登陆界面      {0}

            1，用户登陆
            2，用户注册
    """.format(log)
    print (text)
    choose = raw_input("请输入索引进行选择：")
    if choose == '1':
        Login(s)
    elif choose == '2':
        Register(s)
    else:
        print ("你的选择有误！")


if __name__ == "__main__":

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        s.connect((HOST,PORT))
        Main(s,s.recv(1024))
    except Exception,e:
        print "服务器连接不上....",e
    finally:
        s.close()











