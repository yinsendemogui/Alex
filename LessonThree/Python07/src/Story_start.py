#!usr/bin/env python
# -*- coding:utf-8 -*-
# auther:Mr.chen
# 描述：

import time,os,sys
sys.path.append('..')
from lib import common
from lib.Players_model import players_Model
DIR = os.path.dirname(__file__)
DIR = DIR.replace('src','db/')
TAG = True


def Pre_chapter(user):
    time.sleep(2)
    title = """
                        * * * * * * * * * * * * * * * * * * * * * * *预章：传说* * * * * * * * * * * * * * * * * * * * * * *
    """
    print (title)
    time.sleep(5)
    text = """
                    相传很久以前,于古国疆域,有一奇人姓夸名父.
                    以大力闻于世间,以才智惊于圣贤,以风韵传于万载..
                    忽一日，慕之者至.询问之，其曰...
                    吾父乃真之才,生于凡中.无师而达天地...
                    终其一生教化万民,此乃吾真之所持..
                    父之事迹.且听我慢慢道来...

    """
    for i in text.decode('utf-8'):
        if i != ' ':
            time.sleep(0.5)
            print i.encode('utf-8'),
        else:
            print i.encode('utf-8'),
    The_first_chapter(user)


def The_first_chapter(user):

    # dict = common.log_info_read(DIR + 'config_conf')
    # for S in dict['students']:
    #     if S.Name == user.Name:
    time.sleep(2)
    introduce = """
                              登场人物介绍

                              姓名：{0}
                              年龄：{1}
                              国籍：{2}
                              特长：{3}
                              体力：{4}
                              武力：{5}
                              智力：{6}
                              魅力：{7}
                              秘籍：无

                          点评：屌丝，唯撩妹甚

                              姓名：灵儿
                              年龄：22
                              国籍：china
                              特长：
                              体力：1000
                              武力：70
                              智力：70
                              魅力：100
                              秘籍：游戏保护，万法不侵

                          点评：白富美
        """.format(user.Name,user.Age,user.Nationality,user.Specialty,user.Strength,user.Force,user.IQ,user.Charm)
    for i in introduce.decode('utf-8'):
        if i != ' ':
            time.sleep(0.2)
            print i.encode('utf-8'),
        else:
            print i.encode('utf-8'),
    time.sleep(2)
    title = """
                            * * * * * * * * * * * * * * * * * * * * * * *第一章：缘启* * * * * * * * * * * * * * * * * * * * * * *
            """
    print (title)
    time.sleep(5)
    text = """
                    我的父亲叫做{0},本是一介草民，少时机缘之下，
                    救助了一个跳河自杀之人，本也并无所求，只因
                    我父那时在河中捕鱼，闲河中波澜太盛，吓跑鱼儿，
                    故，救之，以安抚鱼心。谁想此人竟是一小门派
                    掌教之子，因修炼走火，盲目间跌落河中。恰逢我父
                    出海，机缘所致，掌教有感我父恩德，故收其为徒，
                    传功授法，指引修行。说来也怪，我父不论武力{1},
                    智力{1}魅力{2}尽数低于常人,但唯独撩妹能力
                    极其出众，故派中最小师妹灵儿常伴左右，个中滋味
                    不足为外人道也。


        """.format(user.Name,user.Force,user.IQ,user.Charm)
    for i in text.decode('utf-8'):
        if i != ' ':
            time.sleep(0.5)
            print i.encode('utf-8'),
        else:
            print i.encode('utf-8'),
    The_second_chapter(user)


def The_second_chapter(user):
    time.sleep(2)
    introduce = """
                                  登场人物介绍

                                  姓名：高富帅
                                  年龄：34
                                  国籍：china
                                  特长：有钱有势
                                  体力：1000
                                  武力：70
                                  智力：70
                                  魅力：70
                                  秘籍：无

                                点评：如其名


            """
    for i in introduce.decode('utf-8'):
        if i != ' ':
            time.sleep(0.2)
            print i.encode('utf-8'),
        else:
            print i.encode('utf-8'),
    time.sleep(2)
    title = """
                        * * * * * * * * * * * * * * * * * * * * * * *第二章：幻灭* * * * * * * * * * * * * * * * * * * * * * *
        """
    print (title)
    time.sleep(5)
    text = """
                    我父和灵儿就这样朝夕相处，日久生情，只待谈婚论嫁之时。
                    但，世事难料。一日，掌门大寿，宴请四方，祝寿者繁多。
                    有一人姓高名富帅，乃当朝一品大员之子，见灵儿貌美，
                    意欲图之。在其下手一刻，幸被我父所阻，于是心生恨意，
                    命其下人，禀报大员，以圣上赐婚为由，向掌门施压。怎料，
                    掌门欲息事宁人，遂命灵儿随高富帅回京，奉旨完婚。师命
                    难违，灵儿纵千般不愿，亦感无可奈何。临行前，挥泪别过，
                    劝我父放下仇恨，勿思勿念。我父伤心之余，亦感自身渺小。
                    暗发宏愿，以期报仇雪恨，救灵儿于水火之间。
        """
    for i in text.decode('utf-8'):
        if i != ' ':
            time.sleep(0.5)
            print i.encode('utf-8'),
        else:
            print i.encode('utf-8'),
    The_third_chapter(user)

def The_third_chapter(user):
    time.sleep(2)
    title = """
                        * * * * * * * * * * * * * * * * * * * * * * *第三章：暗涛* * * * * * * * * * * * * * * * * * * * * * *
        """
    print (title)
    time.sleep(5)
    text = """
                    灵儿事毕，我父再无心静修，辞别掌教，下山入世。
                    得一高人指点，拜于一隐门之中，勤学苦练，终得
                    真传。我父正欲出山报仇，被隐门上士所阻，言道
                    京城宦官家有一大内高手田伯光，武力高达90有余，
                    欲胜之需闯本门的锁妖塔拿一绝世宝物(双倍暴击率)
                    方可成行。
        """
    for i in text.decode('utf-8'):
        if i != ' ':
            time.sleep(0.5)
            print i.encode('utf-8'),
        else:
            print i.encode('utf-8'),
    time.sleep(2)
    while TAG:
        text = """
                    剧情分支选择如下：
                        1，听劝
                        2，不听劝

        """
        print (text)
        choose = raw_input("请输入索引进行选择")
        if choose == '1':
            Lock_demon_tower(user)
        elif choose == '2':
            Fail_ending_one()
        else:
            print ("你的选择有误！")



def Lock_demon_tower(user):
    List = []
    dict = common.log_info_read(DIR + 'config_conf')
    for pobj in dict['players']:
        if pobj.Name == user.Name:
            P = pobj

    time.sleep(2)
    title = """
                            * * * * * * * * * * * * * * * * * * * * * * *第四章：勇闯锁妖塔* * * * * * * * * * * * * * * * * * * * * * *
            """
    print (title)
    time.sleep(5)
    text = """
                        反复思量，我父还是决定暂缓报仇，遵从隐士的看法，
                        独自一人来到锁妖塔前，看者前方雄伟的高达{0}
                        层的锁妖塔，暗下决心，要尽快完成闯塔拿到宝物.
                        于是，我父来到了塔下的驿站里...
            """.format(str(len(user.Tlist_obj)))
    for i in text.decode('utf-8'):
        if i != ' ':
            time.sleep(0.5)
            print i.encode('utf-8'),
        else:
            print i.encode('utf-8'),
    while TAG:
        test = """
                  请问现在你想去哪？
                    1，闯塔
                    2，打开背包(吃药)          你还有{0}体力
                    3，不闯了，直接去报仇
        """.format(str(P.Strength))
        print (test)
        choose = raw_input("请输入索引进行选择：")
        num = 0
        bum = 0
        if choose == '1':
            for tobj in dict['towers']:
                if P.schedule[tobj] == 100:
                    schedule = '已达成'
                    bum += 1
                else:
                    schedule = P.schedule[tobj]
                print ("{0},{1},难度系数:{2}，进度率：{3}%,创塔次数：{4}次".format(str(num+1),tobj.Lname,tobj.Difficulty,str(schedule),str(P.num[tobj])))
                if bum == len(P.Tlist_obj):
                    print ("{0},锁妖塔顶层，难度系统：0".format(str(num+2)))
                num += 1
                List.append(str(num))
            decide = raw_input("请输入索引进行选择：")
            if decide == str(len(P.Tlist_obj)+1) and bum == len(P.Tlist_obj):
                Lock_demon_tower_Top(user)
            if decide in List:
                if P.schedule[dict['towers'][int(decide)-1]] < 100:
                    for i in range(10):
                        re = P.Begins(dict['towers'][int(decide)-1])
                        if re == False:
                            common.log_info_write(DIR + 'config_conf', dict)
                            break
                    else:
                        common.log_info_write(DIR + 'config_conf', dict)
                else:
                    print ("本层已经闯过了！")
            else:
                print ("你的输入有误！")


        elif choose == '2':
            while TAG:
                text = """
                        背囊物品如下：          你还有{0}体力
                        1，大还丹：{1}个
                        2，小还丹  {2}个
                """.format(str(P.Strength),str(P.Item['大还丹']),str(P.Item['大还丹']))
                print (text)
                choose = raw_input("请输入索引进行选择：")
                if choose == '1':
                    if P.Item['大还丹'] > 0 :
                        P.Item['大还丹'] -= 1
                        P.Strength += 500
                        common.log_info_write(DIR + 'config_conf', dict)
                        break
                    else:
                        print ("大还丹个数为0")
                        break
                elif choose == '2':
                    if P.Item['小还丹'] > 0:
                        P.Item['小还丹'] -= 1
                        P.Strength += 200
                        common.log_info_write(DIR + 'config_conf', dict)
                        break
                    else:
                        print ("小还丹个数为0")
                        break
                else:
                    print ("你的输入有误！请重新输入！")

        elif choose == '3':
            Fail_ending_one()
        else:
            print ("你的输入有误！")


def Lock_demon_tower_Top(user):
    dict = common.log_info_read(DIR + 'config_conf')
    for pobj in dict['players']:
        if pobj.Name == user.Name:
            P = pobj
    time.sleep(2)
    title = """
                                * * * * * * * * * * * * * * * * * * * * * * *第五章：锁妖塔顶* * * * * * * * * * * * * * * * * * * * * * *
                """
    print (title)
    time.sleep(5)
    text = """
                            克服磨难，吾父终至，锁妖塔顶。与前相比，此地奇静。
                            地方不大，有水缸一口，两人高有余。好奇之下，
                            侧身观之，怎料竟有活人居于缸内，遂上前，救出。
                            原来此人就是灵儿。询问下，方知，那日毕，其心已死，
                            趁高富帅不备，遂逃出，寻短见，幸被隐门上士所救，居
                            此疗伤，恰逢我父闯塔，喜得相逢。至此，我父恍然，直呼，
                            此宝胜万宝也（主角瞬间满怒体力翻倍）
                """
    for i in text.decode('utf-8'):
        if i != ' ':
            time.sleep(0.5)
            print i.encode('utf-8'),
        else:
            print i.encode('utf-8'),
    P.Strength = P.Strength * 2
    common.log_info_write(DIR + 'config_conf', dict)
    Wu_Duo(user)


def Wu_Duo(user):
    time.sleep(2)
    title = """
                            * * * * * * * * * * * * * * * * * * * * * * *终章：武夺* * * * * * * * * * * * * * * * * * * * * * *
        """
    print (title)
    time.sleep(5)
    text = """
                        相传很久以前,于古国疆域,有一奇人姓夸名父.
                        以大力闻于世间,以才智惊于圣贤,以风韵传于万载..
                        忽一日，慕之者至.询问之，其曰...
                        吾父乃真之才,生于凡中.无师而达天地...
                        终其一生教化万民,此乃吾真之所持..
                        父之事迹.且听我慢慢道来...

        """
    for i in text.decode('utf-8'):
        if i != ' ':
            time.sleep(0.5)
            print i.encode('utf-8'),
        else:
            print i.encode('utf-8'),




def Fail_ending_one():
    time.sleep(2)
    title = """
                                * * * * * * * * * * * * * * * * * * * * * * *终章：武夺* * * * * * * * * * * * * * * * * * * * * * *
            """
    print (title)
    time.sleep(5)
    text = """
                            报仇心切，我父终是不肯听劝，遂一人趁夜逃出隐门，
                            数日后，进京踩点，待万事俱备只欠东风之时，奈何
                            大员祖宅大内高手，先知先觉，早已暗随我父三日有余，
                            眼见我父正待出手，遂突袭之，我父重伤，感叹报仇无望，
                            自此隐居山林，不问世事.....BAD END......

            """
    for i in text.decode('utf-8'):
        if i != ' ':
            time.sleep(0.5)
            print i.encode('utf-8'),
        else:
            print i.encode('utf-8'),
    exit()