#!usr/bin/env python
# -*- coding:utf-8 -*-
# auther:Mr.chen
# 描述：

LOGIN = []
TAG = True
import os,sys
sys.path.append('..')
from lib import common
from lib.Players_model import players_Model
import Story_start

DIR = os.path.dirname(__file__)
DIR = DIR.replace('src','db/')



def user_Login():
    num = 0
    List = []
    dict = common.log_info_read(DIR + 'config_conf')
    if dict == False:
        print ("请让管理员先创建怪物及锁妖塔模型后再来！")
        return
    if len(dict['players']) == 0:
        print ("请注册角色以后再来！")
        return
    while TAG:
        text = """
                你一共创建了{0}个角色如下：
        """.format(str(len(dict['players'])))
        print (text)
        for P in dict['players']:
            print ("{0},姓名：{1}，年龄：{2}，国籍：{3}，特长：{4}，体力：{5}，武力：{6}，智力：{7}，魅力：{8}，游戏模式：{9}"
                   .format(str(num+1),P.Name,P.Age,P.Nationality,P.Specialty,P.Strength,P.Force,P.IQ,P.Charm,P.GameMode))
            num += 1
            List.append(str(num))
        choose = raw_input("请输入索引选择登陆角色（单选）：")
        if choose in List:
            LOGIN.insert(0,dict['players'][int(choose)-1])
            print ("{0}角色登陆成功！".format(LOGIN[0].Name))
            return
        else:
            print ("您的选择有误，请重新选择！")
            num = 0







def login_Check():
    dict = common.log_info_read(DIR + 'config_conf')

    name = raw_input("请输入你的姓名：")
    age = raw_input("请输入你的年龄：")
    nationality = raw_input("请输入你的国籍：")

    text = """
                  游戏可选特长如下：
                1，无双（初始武力+10，武力越高，敌人的伤害越低）
                2，奇才 (初始智力+10，智力越高遇敌率越低)
                3，妖异 (初始魅力+10，魅力越高，敌人暴击率越低)
                4，守财 (初始体力+300，体力越高越耐打)
    """
    while TAG:
        print(text)
        specialty = raw_input("请输入索引选择你的特长（单选）：")
        Dic = {'1':'无双','2':'奇才','3':'妖异','4':'守财'}
        if specialty in Dic.keys():
            specialty = Dic[specialty]
            break
        else:
            print ("你的输入有误，请重新输入！")
    while TAG:
        decide = raw_input("是否开启作弊模式？（y/n）")
        if decide == 'y':
            gamemode = '作弊模式'
            break
        elif decide == 'n':
            gamemode = '正常模式'
            break
        else:
            print ("你的输入有误！")
    text = """
            你的注册信息如下：
              姓名：{0}
              年龄：{1}
              国籍：{2}
              特长：{3}
              模式：{4}
    """.format(name,age,nationality,specialty,gamemode)
    while TAG:
        print (text)
        decide = raw_input("是否确认（y/n）：")
        if decide == 'y':
            P = players_Model(name,age,nationality,specialty,gamemode,dict['towers'])
            # Dict = {'无双': 'Force', '奇才': 'IQ', '妖异': 'Charm'}
            if specialty == '无双':
                P.Force += 10
            elif specialty == '奇才':
                P.IQ += 10
            elif specialty == '妖异':
                P.Charm += 10
            else:
                P.Strength += 300
            if gamemode == '作弊模式':
                P.Force = 100
                P.IQ = 100
                P.Charm = 100
                P.Strength = 100000

            dict['players'].append(P)
            common.log_info_write(DIR + 'config_conf', dict)
            print ('信息注册成功')
            return
        elif decide == 'n':
            return
        else:
            print ('你的输入有误！')







def user_Main():

    text = """
              欢迎体验模拟的人生
                1，角色选择
                2，角色注册
                3，游戏开始
                4，游戏退出
    """
    while TAG:
        print (text)
        dict = {'1':user_Login,'2':login_Check,'3':Story_start.Pre_chapter,'4':common.Exit}
        choose = raw_input("请输入你的选择：")
        if choose in dict.keys():
            if choose == '3' and LOGIN != []:
                dict[choose](LOGIN[0])
            elif choose == '3':
                print ("请登陆角色后再来！")
            else:
                dict[choose]()
        else:
            print ("你的输入有误！")

if __name__ == "__main__":
    user_Main()