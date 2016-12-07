#!usr/bin/env python
# -*- coding:utf-8 -*-
# auther:Mr.chen
# 描述：

import random,time,sys,os
sys.path.append('..')
from lib import common




class lock_demon_tower_Model:
    '''
    锁妖塔模型类
    '''



    def __init__(self,lname,difficulty,mlist_obj):
        self.Lname = lname                #塔名
        self.Difficulty = difficulty      #难度（小怪攻击力倍增）
        self.Mlist_obj = mlist_obj        #小怪列表


    def __str__(self):
        return self.Lname












    #
    # def success_Radio(self):    # 创塔随机意外率
    #     num = random.randrange(1, 1000)
    #     if num > 500:
    #         return True
    #     else:
    #         a = random.randrange(1, 5)
    #         lock_demon_tower_Model.event(str(a))
    #         return False
    #
    # @staticmethod
    # def event(num):     #授课意外事件
    #     dict = {'1': '据说老师刚刚失恋了，授课状态很差', '2': '据说老师已经递交了辞职报告，授课状态很差',
    #             '3': '据说老师相亲去了，到现在状态都还没恢复。', '4': '据说老师家里节哀了，心情极度悲伤',
    #             '5': '据说老师钱包丢了，内心无比哀叹'}
    #     time.sleep(1)
    #     print(dict[num])