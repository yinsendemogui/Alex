#!usr/bin/env python
# -*- coding:utf-8 -*-
# auther:Mr.chen
# 描述：

import socket,os
import time
TAG =True

DIR = os.path.dirname(os.path.abspath(__file__))
DIR = DIR+'/Folder/'


def Recvfile(s,filename):
    print ("开始下载文件...")
    buffer = []
    while TAG:
        d = s.recv(4096)
        if not d or d == 'exit':
            break
        buffer.append(d)
    data = ''.join(buffer)
    with open(DIR+filename,'w') as f:
        f.write(data)
    print ("文件下载完毕！")


def Sendfile(s,filename):
    print ("开始上传文件！")
    with open(DIR+filename,'r') as f:
        while TAG:
            data = f.read(4096)
            if not data:
                break
            s.sendall(data)
    time.sleep(1)
    s.send('exit')
    print ("文件上传完毕")




def Confirm(s,command):
    s.sendall(command)
    re = s.recv(4096)
    if re == 'Ready!':
        return True


if __name__ == "__main__":
    host = 'localhost'
    port = 8888
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        s.connect((host,port))
        print (s.recv(1024))
        while TAG:
            command = raw_input("请输入你想执行的命令>>")
            if not command:
                continue
            action,filename = command.strip().split()
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
                else:
                    print ("对方服务器没有准备好！")
                    break
            else:
                print ("你输入的命令有误！")
    except Exception,e:
        print ("客户端连接有错！",e)
    finally:
        s.close()











# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#
# s.connect(("localhost",8888))
#
#
# while True:
#
#     message = raw_input('输入：')
#     if message == 'n':
#         break
#     s.send(message)
#     data = s.recv(1024)
#     print (data)
#
# s.close()
