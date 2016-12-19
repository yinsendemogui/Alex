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
    DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DIR = DIR + '/Folder/'
    ConfigDir = DIR.replace('Folder','conf')

    def __init__(self,name,password):
        self.Name = name   #用户名
        self.Password = password   #密码
        self.DIR = PersonInfo.DIR + self.Name +'/'   #用户家目录





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

