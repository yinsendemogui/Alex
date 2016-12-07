#!usr/bin/env python
# -*- coding:utf-8 -*-
# auther:Mr.chen
# 描述：

import os,sys
sys.path.append('..')
from lib.Small_monster_model import small_monster_Model
from lib.Lock_demon_tower_model import lock_demon_tower_Model
from lib import common

DIR = os.path.dirname(__file__)
DIR = DIR.replace('src','db/')

TAG = True

def create_monsters_model():
    """
    创建小怪模型
    :return: None
    """
    while TAG:
        name = raw_input("请输入怪物的姓名：")
        hurt = raw_input("请输入怪物的破坏力：")
        text = """
            怪物信息如下：
             姓名：  {0}
             破坏力：{1}
        """.format(name,hurt)
        print (text)
        decide = raw_input("是否确认（y/n）：")
        if decide == 'y':
            M = small_monster_Model(name,hurt)
            dict = common.log_info_read(DIR+'config_conf')
            if dict != False:
                dict['monsters'].append(M)
                common.log_info_write(DIR + 'config_conf', dict)
                print ("怪物信息保存成功！")
                return
            else:
                dict = {
                    'monsters':[M],
                    'towers':[],
                    'players':[]
                }
                common.log_info_write(DIR+'config_conf',dict)
                print ("怪物信息保存成功！")
                return
        elif decide == 'n':
            break
        else:
            print ("您的输入有误！")



def create_Tower_model():
    """
    创建锁妖塔模型
    :return: None
    """

    dict = common.log_info_read(DIR + 'config_conf')
    if dict == False:
        print ("请先创建怪物模型后再来！")
        return
    name = raw_input("请输入锁妖塔的名称：")
    difficulty = raw_input("请输入本层的难度（倍增小怪攻击力）：")
    T= lock_demon_tower_Model(name,difficulty,dict['monsters'])
    while TAG:
        text = """
                    课程的信息如下：
                     塔名：  {0}
                     难度：  {1}
            """.format(name,difficulty)
        print (text)
        decide = raw_input("是否确认（y/n）：")
        if decide == 'y':
            dict['towers'].append(T)
            common.log_info_write(DIR + 'config_conf', dict)
            return
        elif decide == 'n':
            return
        else:
            print ("您的输入有误！")









def model_Config():
    """
    查看已经创建的模型
    :return: None
    """
    num = 0
    Num = 0
    dict = common.log_info_read(DIR + 'config_conf')
    if dict == False:
        print ("请先创建怪物模型后再来！")
        return
    print ("已经创建的怪物模型，如下：".format(str(len(dict['monsters']))))
    for M in dict['monsters']:
        print ("{0}:怪物名：{1}，破坏力：{2}，掉宝：{3}".format(str(num + 1), M.Name, M.Hurt, M.Drop))
        num += 1
    print ("已经创建的塔模型，如下：".format(str(len(dict['towers']))))
    for P in dict['towers']:
        print ("{0}:塔名：{1}，难度：{2}，怪物列表：{3}".format(str(Num + 1), P.Lname, P.Difficulty, P.Mlist_obj))
        Num += 1




def admin_Main(log = None):
    """
    管理员管理界面
    :param log: 用户登录标志
    :return: None
    """
    while TAG:
        text = """
                    欢迎来到管理员界面        {0}登陆中
                    1，创建怪物模组
                    2，创建锁妖塔模组
                    3，查看模组配置
                    4，系统退出
        """.format(log)
        print (text)
        while TAG:
            choose = raw_input('请输入你的选择：')
            if choose == '1':
                create_monsters_model()
                break
            elif choose == '2':
                create_Tower_model()
                break
            elif choose == '3':
                model_Config()
                break
            elif choose == '4':
                common.Exit()
            else:
                print ('您的输入有误！')

if __name__ == "__main__":
    admin_Main('admin')