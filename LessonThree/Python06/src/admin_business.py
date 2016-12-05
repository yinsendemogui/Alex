#!usr/bin/env python
# -*- coding:utf-8 -*-
# auther:Mr.chen
# 描述：

import os,sys
sys.path.append('..')
from lib.Teachers_model import teacher_Model
from lib.Lessons_model import lesson_Model
from lib import common

DIR = os.path.dirname(__file__)
DIR = DIR.replace('src','db/')

TAG = True

def create_Teachers_model():
    """
    创建老师模型
    :return: None
    """
    while TAG:
        name = raw_input("请输入老师的姓名：")
        age = raw_input("请输入老师的年龄：")
        sex = raw_input("请输入老师的性别：")
        while TAG:
            text = """
                老师信息如下：
                 姓名：{0}
                 年龄：{1}
                 性别：{2}
            """.format(name,age,sex)
            print (text)
            decide = raw_input("是否确认（y/n）：")
            if decide == 'y':
                P = teacher_Model(name,age,sex)
                dict = common.log_info_read(DIR+'config_conf')
                if dict != False:
                    dict['teachers'].append(P)
                    common.log_info_write(DIR + 'config_conf', dict)
                    print ("老师信息保存成功！")
                    return
                else:
                    dict = {
                        'teachers':[P],
                        'lessons':[],
                        'students':[]
                    }
                    common.log_info_write(DIR+'config_conf',dict)
                    print ("老师信息保存成功！")
                    return
            elif decide == 'n':
                break
            else:
                print ("您的输入有误！")



def create_Lesson_model():
    """
    创建课程模型
    :return: None
    """
    num = 0
    list = []
    dict = common.log_info_read(DIR + 'config_conf')
    if dict == False:
        print ("请先创建老师模型后再来！")
        return
    name = raw_input("请输入课程名称：")
    cost = raw_input("请输入课时费：")
    while TAG:
        print ("目前有{0}个老师可供选择，如下：".format(str(len(dict['teachers']))))
        for P in dict['teachers']:
            print ("{0}:姓名：{1}，年龄：{2}，性别：{3}".format(str(num+1),P.Name,P.Age,P.Sex))
            num += 1
            list.append(str(num))
        choose = raw_input("请输入索引选择授课老师：")
        if choose in list:
            tobj = dict['teachers'][int(choose)-1]
            L = lesson_Model(name,cost,tobj)
            while TAG:
                text = """
                        课程的信息如下：
                         课程名：{0}
                         课时费：{1}
                        授课老师：{2}
                """.format(name, cost, L.Tobj.Name)
                print (text)
                decide = raw_input("是否确认（y/n）：")
                if decide == 'y':
                    dict['lessons'].append(L)
                    common.log_info_write(DIR + 'config_conf', dict)
                    return
                elif decide == 'n':
                    return
                else:
                    print ("您的输入有误！")
        else:
            print ("您的输入有误！")
            num = 0


def model_Config():
    """
    查看已经创建的模型
    :return: None
    """
    num = 0
    Num = 0
    dict = common.log_info_read(DIR + 'config_conf')
    if dict == False:
        print ("请先创建老师模型后再来！")
        return
    print ("已经创建的老师模型，如下：".format(str(len(dict['teachers']))))
    for P in dict['teachers']:
        print ("{0}:姓名：{1}，年龄：{2}，性别：{3}".format(str(num + 1), P.Name, P.Age, P.Sex))
        num += 1
    print ("已经创建的课程模型，如下：".format(str(len(dict['teachers']))))
    for P in dict['lessons']:
        print ("{0}:课程名：{1}，课时费：{2}，授课老师：{3}".format(str(Num + 1), P.Lname, P.Lcost, P.Tobj.Name))
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
                    1，创建老师模组
                    2，创建课程模组
                    3，查看模组配置
                    4，系统退出
        """.format(log)
        print (text)
        while TAG:
            choose = raw_input('请输入你的选择：')
            if choose == '1':
                create_Teachers_model()
                break
            elif choose == '2':
                create_Lesson_model()
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