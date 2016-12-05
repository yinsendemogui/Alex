#!usr/bin/env python
# -*- coding:utf-8 -*-
# auther:Mr.chen
# 描述：

LOGIN = []
TAG = True
import os,sys
sys.path.append('..')
from lib import common
from lib.Students_model import student_Model
from src import admin_business

DIR = os.path.dirname(__file__)
DIR = DIR.replace('src','db/')



def user_Login():
    dict = common.log_info_read(DIR + 'config_conf')
    if dict == False:
        print ("请让管理员先创建老师及课程模型后再来！")
        return
    while TAG:
        account = raw_input("请输入你的登录名：")
        if account == 'admin':
            password = raw_input("请输入你的登陆密码：")
            if password == '123123':
                admin_business.admin_Main('admin')
        for S in dict['students']:
            if S.Account == account:
                while TAG:
                    password = raw_input("请输入你的登陆密码：")
                    if S.Password == password:
                        print ('登陆成功')
                        LOGIN.insert(0,S)
                        user_Main(S.Name)
                    else:
                        print ("您输入的密码有误！")
        else:
            print ("您输入的账号有误，请重新输入！")



def login_Check():
    dict = common.log_info_read(DIR + 'config_conf')
    if dict == False:
        print ("请让管理员先创建老师及课程模型后再来！")
        return
    name = raw_input("请输入你的姓名：")
    age = raw_input("请输入你的年龄：")
    account = raw_input("请输入你的登录账号：")
    password = raw_input("请输入你的登陆密码：")
    text = """
            你的注册信息如下：
              姓名：{0}
              年龄：{1}
              登陆账号：{2}
              登陆密码：{3}
    """.format(name,age,account,password)
    while TAG:
        print (text)
        decide = raw_input("是否确认（y/n）：")
        if decide == 'y':
            S = student_Model(name,age,account,password,[])
            dict['students'].append(S)
            common.log_info_write(DIR + 'config_conf', dict)
            LOGIN.insert(0,S)
            print ('信息注册成功')
            user_Main(name)
        elif decide == 'n':
            return
        else:
            print ('你的输入有误！')


def select_Lesson():
    num = 0
    List = []
    dict = common.log_info_read(DIR + 'config_conf')
    if LOGIN == []:
        print ('请登陆后再来！')
        return
    if dict == False:
        print ("请让管理员先创建老师及课程模型后再来！")
        return
    print ("目前的可选课程有{0}门，如下：".format(str(len(dict['lessons']))))
    for lesson in dict['lessons']:
        print ('{0}，课程名：{1}，课时费：{2},授课老师：{3}'.format(str(num+1),lesson.Lname,lesson.Lcost,lesson.Tobj.Name))
        num += 1
        List.append(str(num))
    while TAG:
        choose = raw_input("请输入索引选择课程（可以多选但不能重复）：")
        if choose.isdigit():
            if len(choose) == len(set(choose)):
                if set(choose) & set(List) == set(choose):
                    for S in dict['students']:
                        if S.Name == LOGIN[0].Name:
                            for i in list(choose):
                                if dict['lessons'][int(i)-1] in S.Lobj:
                                    print ("您已经添加过{0}课程了".format(dict['lessons'][int(i)-1].Lname))
                                else:
                                    S.Lobj.append(dict['lessons'][int(i)-1])
                                    S.schedule[dict['lessons'][int(i)-1]] = 0
                                    S.num[dict['lessons'][int(i) - 1]] = 0
                            common.log_info_write(DIR + 'config_conf', dict)
                            print ('选课成功！')
                            return
                        else:
                            pass
                else:
                    print ("您的选择超范围，请重新选择！")
            else:
                print ("您的选择里有重复内容，请重新输入！")
        else:
            print ('您的输入必须是纯数字，请重新输入！')


def class_Begins():
    num = 0
    List = []
    dict = common.log_info_read(DIR + 'config_conf')
    if LOGIN == []:
        print ('请登陆后再来！')
        return
    if dict == False :
        print ("请让管理员先创建老师及课程模型后再来！")
        return
    for S in dict['students']:
        if S.Name == LOGIN[0].Name and S.Lobj == []:
            print ("您还没有选课，请选课后再来！")
            return
    while TAG:

        for obj in dict['students']:
            if obj.Name == LOGIN[0].Name:
                print ("您有{0}门待修业课程，如下：".format(str(len(obj.Lobj))))
                for lesson in obj.Lobj:
                    if obj.schedule[lesson] >= 100:
                        finished = '已达成'
                    elif obj.num[lesson] >= 9:
                        finished = '修业失败'
                    else:
                        finished = obj.schedule[lesson]
                    print ('{0},课程名：{1},课时费：{2},授课老师：{3}，修业达成率：{4},已修业次数：{5}'.format(str(num+1),lesson.Lname,lesson.Lcost,lesson.Tobj.Name,finished,obj.num[lesson]))
                    num += 1
                    List.append(str(num))
        choose = raw_input("请输入你的选择(单选）(输入n返回上一级菜单)：")
        if choose in List:
            # if LOGIN[0].schedule[LOGIN[0].Lobj[int(choose)]] < 100:
            for obj in dict['students']:
                if obj.Name == LOGIN[0].Name:
                    for i in range(9):
                        # print (obj.Lobj[int(choose)-1])
                        if obj.schedule[obj.Lobj[int(choose)-1]] < 100 and obj.num[obj.Lobj[int(choose)-1]] < 9:
                            obj.Classbegins(obj.Lobj[int(choose)-1].Lname)
                            num = 0
                        else:
                            print ('您选择的课程已经修业完成，请重新选择！')
                            common.log_info_write(DIR + 'config_conf', dict)
                            num = 0
                            break
                    common.log_info_write(DIR + 'config_conf', dict)
        elif choose == 'n':
            return
        else:
            print ("您的输入有误！")
            num = 0




def user_Main(log = None):
    if log == None:
        log = '用户未登录...'
    else:
        log = "{0}登陆中...".format(log)
    text = """
              欢迎光临选课系统         {0}
                1，学生登录
                2，学生注册
                3，学生选课
                4，学生上课
                5，系统退出
    """.format(log)
    while TAG:
        print (text)
        dict = {'1':user_Login,'2':login_Check,'3':select_Lesson,'4':class_Begins,'5':common.Exit}
        choose = raw_input("请输入你的选择：")
        if choose in dict.keys():
            dict[choose]()
        else:
            print ("你的输入有误！")

if __name__ == "__main__":
    user_Main()