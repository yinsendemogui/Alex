#!usr/bin/env python
# -*- coding:utf-8 -*-
# auther:Mr.chen
# 描述：

import time
import os
import pickle


class PersonInfo:
    """
    用户模型类
    """
    DIR = os.path.dirname(os.path.abspath(__file__))
    DIR = DIR + '/Folder/'
    ConfigDir = DIR.replace('Folder','db')

    def __init__(self,name,password):
        self.Name = name   #用户名
        self.Password = password   #密码
        self.DIR = PersonInfo.DIR + self.Name +'/'   #用户家目录


    def login(self):
        """
        用户登陆
        :return:
        """
        dict = PersonInfo.config_read()
        if dict == None:
            return False
        if self.Name in dict:
            if dict[self.Name] == self.Password:
                return True
        return False



    def register(self):
        """
        用户注册
        :return:
        """
        if os.path.exists(self.DIR) != True:
            os.system('mkdir'+' '+  self.DIR)
        try:
            dict = PersonInfo.config_read()
            if dict == None:
                dict = {}
            if self.Name not in dict:
                dict[self.Name] = self.Password
            else:
                print ("姓名重复")
                return False
            re = PersonInfo.config_write(dict)
            if re == True:
                return True
        except Exception,e:
            print "注册出现异常！",e
            return False



    def view_file(self,conn):
        """
        查看用户家目录
        :param conn:
        :return:
        """
        data = os.popen('ls'+' '+ self.DIR).read()
        conn.sendall(data)

    def Recvfile(self,conn,filename):
        """
        接收文件方法
        :param conn:tcp连接对象
        :param filename:目标文件名
        :return:
        """
        print ("开始接收文件...")
        conn.send('Ready!')
        buffer = []
        while True:
            d = conn.recv(4096)
            if d == 'exit':
                break
            else:
                buffer.append(d)
        data = ''.join(buffer)
        if data == '':
            return False
        print (data)
        print (filename)
        print (self.DIR)
        with open(self.DIR + filename, 'w') as f:
            f.write(data)
            return True


    def Sendfile(self,conn,filename):
        """
            放送文件方法
            :param conn: tcp连接对象
            :param filename: 目标文件名
            :return:
            """

        if os.path.exists(self.DIR + filename):
            print ("开始放送文件...")
            conn.send('Ready!')
            time.sleep(1)
            with open(self.DIR + filename, 'r') as f:
                while True:
                    data = f.read(4096)
                    print (data)
                    if not data:
                        break
                    conn.sendall(data)
            time.sleep(1)
            conn.send('exit')
            print ("文件放送成功！")
        else:
            conn.send('False!')


    @staticmethod
    def config_read():
        """
        配置文件全部读取
        :return:
        """
        if os.path.exists(PersonInfo.ConfigDir+'user_config'):
            with open(PersonInfo.ConfigDir+'user_config','r') as f:
                dict = pickle.load(f)
                return dict


    @staticmethod
    def config_write(dict):
        """
        配置文件全部写入
        :param dict:
        :return:
        """
        with open(PersonInfo.ConfigDir + 'user_config', 'w') as f:
            pickle.dump(dict,f)
            return True

