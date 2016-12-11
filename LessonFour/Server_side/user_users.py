#!usr/bin/env python
# -*- coding:utf-8 -*-
# auther:Mr.chen
# 描述：



class PersonInfo:
    import os

    DIR = os.path.dirname(os.path.abspath(__file__))
    DIR = DIR + '/Folder/'

    def __init__(self,name,password):
        self.Name = name   #用户名
        self.Password = password   #密码
        self.DIR = PersonInfo.DIR + self.Name   #用户家目录


    def login(self):
        return True


    def register(self):
        return True


    def view_file(self):
        pass


    @staticmethod
    def config_read():
        pass


    @staticmethod
    def config_write():
        pass

