#!usr/bin/env python
# -*- coding:utf-8 -*-
# auther:Mr.chen
# 描述：

import SocketServer
import os,time,sys

DIR = os.path.dirname(os.path.abspath(__file__))
DIR = DIR.replace('core','Folder/')
HOST = 'localhost'
PORT = 8888


class Myserver(SocketServer.BaseRequestHandler):

    def __init__(self,request,client_address,server):
        SocketServer.BaseRequestHandler.__init__(self,request,client_address,server)
        self.Name = ''          #用户名
        self.Password = ''      #用户密码
        self.Quota = ''         #用户磁盘配额
        self.Home_path = ''     #用户家目录路径
        self.Current_path = ''  #用户当前路径



    def ls_Method(self):
        pass


    def put_Method(self):
        pass


    def get_Method(self):
        pass


    def cd_Method(self):
        pass


    def mkdir_Method(self):
        pass


    def rm_Method(self):
        pass


    def headle(self):
        conn = self.request
        print ("收到来自{0}的客户端连接...".format(self.client_address[0]))




if __name__ == "__main__":
    s = SocketServer.ThreadingTCPServer((HOST,PORT),Myserver)
    s.serve_forever()









