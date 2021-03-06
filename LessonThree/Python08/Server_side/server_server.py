#!usr/bin/env python
# -*- coding:utf-8 -*-
# auther:Mr.chen
# 描述：

import socket
import os
import threadding_ex
import time
import json
from user_users import PersonInfo

DIR = os.path.dirname(os.path.abspath(__file__))
DIR = DIR+'/Folder/'

TAG = True



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
                    P.view_file(conn)
                    continue
                action,filename = data.strip().split()
                action = action.lower()
                if action == 'put':
                    re = P.Recvfile(conn,filename)
                    if re == True:
                        print ("文件接收成功！")
                    else:
                        print ("文件接收失败！")
                elif action == 'get':

                    P.Sendfile(conn,filename)
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
        t = threadding_ex.Thread(target=tcplink, args=(conn, addr))
        t.start()




