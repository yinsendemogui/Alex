#!usr/bin/env python
# -*- coding:utf-8 -*-
# auther:Mr.chen
# 描述：

import socket
import os
import threading
import time

DIR = os.path.dirname(os.path.abspath(__file__))
DIR = DIR+'/Folder/'

TAG = True




def Recvfile(conn,filename):
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
        d = conn.resv(4096)
        if not buffer or buffer == 'exit':
            print ("{0}文件接收成功！".format(filename))
            break
        else:
            buffer.append(d)
    data = ''.join(buffer)
    with open(DIR+filename,'w') as f:
        f.write(data)



def Sendfile(conn,filename):
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
            if not data :
                break
            conn.sendall(data)
    time.sleep(1)
    conn.send('exit')
    print ("文件放送成功！")


def tcplink(conn,addr):
    print ("收到来自{0}的连接请求".format(addr))
    conn.send('欢迎你！')
    while TAG:
        try:
            data = conn.resv(4096)
            time.sleep(1)
            if not data:
                break
            else:
                action,filename = data.strip().split()
                if action == 'put':
                    Recvfile(conn,filename)
                elif action == 'get':
                    Sendfile(conn,filename)
                else:
                    print ("请求方的输入有错！")
                    continue
        except Exception,e:
            print "tcplink处理出现问题",e





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




