#!usr/bin/env python
# -*- coding:utf-8 -*-
# auther:Mr.chen
# 描述：
import random,time,os,sys
sys.path.append('..')
import common

DIR = os.path.dirname(__file__)
DIR = DIR.replace('src', 'db/')
DICT = common.log_info_read(DIR + 'config_conf')


class players_Model:
    '''
    玩家模型类
    '''


    def __init__(self,name,age,nationality,specialty,gamemode,tlist_obj):
        self.Name = name                        # 姓名
        self.Age = age                          # 年龄
        self.Nationality = nationality          # 国籍
        self.Specialty = specialty              # 特长
        self.Strength = 1000                    # 体力
        self.GameMode = gamemode                # 游戏模式
        self.Tlist_obj = tlist_obj              # 锁妖塔层关数列表
        self.Force = random.randrange(40, 60)   # 随机武力
        self.IQ= random.randrange(40,60)        # 随机智力
        self.Charm= random.randrange(40,60)     # 随机魅力
        self.Item = {'大还丹':0,'小还丹':0}       # 背包栏
        self.schedule = {}
        self.num = {}
        for obj in self.Tlist_obj:
            self.schedule[obj] = 0    #锁妖塔每层进度率
            self.num[obj] = 0         #闯塔次数



    def Begins(self,tobj):      #闯塔
        time.sleep(1)
        print("{0}慢慢的走了过去，用尽力量推开了{1}的大门，第{2}次闯塔开始！").format(self.Name,tobj,str(self.num[tobj]+1))
        re = self.success_Radio()
        if re != True:
            self.Battle(tobj)
        else:
            time.sleep(1)
            print ("很幸运，这次没遇到敌人！")
        self.schedule[tobj] += 10
        self.num[tobj] += 1
        time.sleep(1)
        print ("{0}结束了本次创塔，{1}的进度率变为{2}%,".format(self.Name, tobj, self.schedule[tobj]))
        if self.schedule[tobj] == 100:
            return False
        else:
            return True




    def Battle(self,tobj):          #战斗
        num = random.randrange(1,len(tobj.Mlist_obj))
        bum = random.randrange(1,1000)
        if bum > self.Charm * 10 :      #暴击判定
            hurt = (int(tobj.Mlist_obj[num - 1].Hurt) - (self.Force / 20)) * int(tobj.Difficulty) * 2
            self.Strength = self.Strength - hurt
            time.sleep(1)
            print ("{0}对你发起了毁灭性攻击（暴击），造成了{1}体力的伤害，你还剩余{2}体力".format(tobj.Mlist_obj[num - 1].Name, hurt, self.Strength))
        else:
            hurt = (int(tobj.Mlist_obj[num - 1].Hurt) - (self.Force / 20)) * int(tobj.Difficulty)
            self.Strength = self.Strength - hurt
            time.sleep(1)
            print ("{0}对你发起了打击，造成了{1}体力的伤害，你还剩余{2}体力".format(tobj.Mlist_obj[num - 1].Name, hurt, self.Strength))
        num = random.randrange(1,1000)
        if num >= 800:
            print ("费尽艰辛，你终于打败了怪物，从一堆渣子中你发现了大还丹！！")
            self.Item['大还丹'] +=1
        elif num >500 and num <800:
            print ("费尽艰辛，你终于打败了怪物，从一堆渣子中你发现了小还丹！！")
            self.Item['小还丹'] += 1
        else:
            print ("费劲艰辛打败怪物你的，仍旧一无所获。。。")


    def success_Radio(self):    #遇敌判定
        num = random.randrange(1, 1100)
        if num <= self.IQ * 10:
            return True
        else:
            a = random.randrange(1,5)
            # print (type(a))
            players_Model.event(str(a))
            return False


    @staticmethod
    def event(num):     #战斗事件
        dict = {'1':'你不小心猜了一坨屎，没想到当中居然有个怪物，突然向你袭来','2':'你看到一幅画，画里的人正是灵儿，突然它看了过来...',
                '3':'一个怪物坐在一个独木桥中间，没办法你只能向它杀了过去','4':'一个胡同黑乎乎的，正当你想该往哪走的时候，有个东西摸了你的背后...',
                '5':'你静悄悄的缓步绕路，意图躲开怪物，但是它的同伴却发现了你....'}
        time.sleep(1)
        print (dict[num])


