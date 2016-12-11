#!usr/bin/env python
# -*- coding:utf-8 -*-
# auther:Mr.chen
# 描述：

import socket
import os
import threading
import time
import json
from user_users import PersonInfo

DIR = os.path.dirname(os.path.abspath(__file__))
DIR = DIR+'/Folder/'

TAG = True




def Recvfile(conn,filename,P):
    """
    接收文件方法函数
    :param conn:tcp连接对象
    :param filename:目标文件名
    :return:
    """
    print ("开始接收文件...")
    conn.send('Ready!')
    buffer = []
    while TAG:
        d = conn.recv(4096)
        if d == 'exit':
            print ("{0}文件接收成功！".format(filename))
            break
        else:
            buffer.append(d)
    data = ''.join(buffer)
    with open(DIR+filename,'w') as f:
        f.write(data)



def Sendfile(conn,filename,P):
    """
    放送文件方法函数
    :param conn: tcp连接对象
    :param filename: 目标文件名
    :return:
    """
    print ("开始放送文件...")
    conn.send('Ready!')
    time.sleep(1)
    with open(DIR+filename,'r') as f:
        while TAG:
            data = f.read(4096)
            print (data)
            if not data :
                break
            conn.sendall(data)
    time.sleep(1)
    conn.send('exit')
    print ("文件放送成功！")






def tcplink(conn,addr):
    """
    tcp请求分析函数
    :param conn: tcp连接对象
    :param addr: 连接地址
    :return:
    """
    print ("收到来自{0}的连接请求".format(addr))
    conn.send('与主机通信中...')
    while TAG:
        try:
            data = conn.recv(4096)
            time.sleep(1)
            if not data:
                break
            else:
                print (data)
                if data == 'ls':
                    P.view_file()
                action,filename = data.strip().split()
                action = action.lower()
                print (action)
                print (filename)
                if action == 'put':
                    Recvfile(conn,filename,P)
                elif action == 'get':
                    Sendfile(conn,filename,P)
                elif action == 'login':
                    name, password = filename.split(',')
                    P = PersonInfo(name, password)
                    re = P.login()
                    if re == True:
                        conn.send('Ready!')
                    else:
                        conn.send('False!')
                elif action == 'register':
                    name,password = filename.split(',')
                    P = PersonInfo(name, password)
                    re = P.register()
                    if re == True:
                        conn.send('Ready!')
                    else:
                        conn.send('False!')
                else:
                    print ("请求方的输入有错！")
                    continue
        except Exception,e:
            print "tcplink处理出现问题",e
            break




if __name__ == '__main__':
    host = 'localhost'
    port = 8888
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind((host,port))
    s.listen(5)
    print ("服务运行中：正在监听{0}地址的{1}端口：".format(host,port))
    while TAG:
        # 接受一个新连接
        conn,addr = s.accept()
        # 创建一个新线程处理TCP连接
        t = threading.Thread(target=tcplink,args=(conn,addr))
        t.start()




