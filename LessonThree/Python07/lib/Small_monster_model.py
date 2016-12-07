#!usr/bin/env python
# -*- coding:utf-8 -*-
# auther:Mr.chen
# 描述：教师模型类

import random,time,os,sys
sys.path.append('..')
from lib import common
DIR = os.path.dirname(__file__)
DIR = DIR.replace('src', 'db/')
DICT = common.log_info_read(DIR + 'config_conf')

class small_monster_Model:
    '''
    小怪物模型类
    '''
    def __init__(self,name,hurt):
        self.Name = name                    # 怪物名
        self.Hurt = hurt                    # 破坏力
        self.Drop = ['大还丹','小还丹']       # 掉宝


    def __str__(self):
        return self.Name




