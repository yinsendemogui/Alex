#!usr/bin/env python
# -*- coding:utf-8 -*-
# auther:Mr.chen
# 描述：
import random,time

class student_Model:
    '''
    学生模型类
    '''

    # num = 0
    def __init__(self,name,age,account,password,lobj):
        self.Name = name            #姓名
        self.Age = age              #年龄
        self.Account = account      #账户名
        self.Password = password    #密码
        self.Lobj = lobj            #课程对象列表
        self.IQ= random.randrange(40,90)   #随机智商
        self.schedule = {}
        self.num = {}
        for lesson in self.Lobj:
            self.schedule[lesson] = 0    #课程进度率字典
            self.num[lesson] = 0         #课程修业次数

    def Classbegins(self,lesson_name):      #上课
        for obj in self.Lobj:
            if obj.Lname == lesson_name :
                # print (self.num)
                print('{0}课程进行第{1}次修业...'.format(obj.Lname, str(self.num[obj] + 1)))
                time.sleep(1)
                if self.success_Radio():
                    tag = obj.classBegins()
                    if tag:
                        self.schedule[obj] += 20
                        self.num[obj] += 1
                        time.sleep(1)
                        print ('你感觉非常好！')
                        time.sleep(1)
                        print ('{0}:{1}课程学习成功！完成率提高20%，达成率变为{2}%'.format(self.Name,obj.Lname,str(self.schedule[obj])))
                    else:
                        self.num[obj] += 1
                        time.sleep(1)
                        print ('你突然有一种骂娘的冲动...')
                        time.sleep(1)
                        print ('{0}:{1}课程学习失败，你对课程的理解没有丝毫提高，达成率为{2}%'.format(self.Name,obj.Lname,str(self.schedule[obj])))
                else:
                    tag = obj.classBegins()
                    if tag:
                        self.schedule[obj] += 10
                        self.num[obj] += 1
                        time.sleep(1)
                        print('{0}:{1}课程学习欠佳！完成率提高10%，达成率变为{2}%'.format(self.Name,obj.Lname, str(self.schedule[obj])))
                    else:
                        self.num[obj] += 1
                        time.sleep(1)
                        print('你突然萌生了轻生的念头...')
                        time.sleep(1)
                        print('{0}:{1}课程学习失败，你对课程的理解没有丝毫提高，达成率为{2}%'.format(self.Name, obj.Lname,
                                                                            str(self.schedule[obj])))
            else:
                pass




    def success_Radio(self):    #学习随机意外率
        num = random.randrange(1, 1000)
        if num <= self.IQ * 10:
            return True
        else:
            a = random.randrange(1,5)
            # print (type(a))
            student_Model.event(str(a))
            return False


    @staticmethod
    def event(num):     #学习意外事件
        dict = {'1':'你感觉头晕脑胀，浑身乏力！','2':'外面突然飞过一只蜻蜓，你看着他飞了一节课！',
                '3':'女朋友来短信了，你激动的忘了听课','4':'你突然感觉肚子疼...原来是想拉屎了',
                '5':'你的眼镜片碎了....'}
        time.sleep(1)
        print (dict[num])

