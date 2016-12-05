#!usr/bin/env python
# -*- coding:utf-8 -*-
# auther:Mr.chen
# 描述：

import random,time

class lesson_Model:
    '''
    课程模型类
    '''
    def __init__(self,lname,lcost,tobj):
        self.Lname = lname      #课程名
        self.Lcost = lcost      #课时费
        self.Tobj = tobj        #授课老师
        self.difficulty = random.randrange(10,40) #授课难度


    def classBegins(self):      #上课方法
        if self.success_Radio():
            self.Tobj.teacher_Success(self.Lcost)
            return True
        else:
            self.Tobj.teacher_Accident()
            return False





    def success_Radio(self):    #授课随机意外率
        num = random.randrange(1, 1000)
        if num <= (100-self.difficulty) * 10:
            return True
        else:
            a = random.randrange(1, 5)
            # print (type(a))
            lesson_Model.event(str(a))
            return False

    @staticmethod
    def event(num):     #授课意外事件
        dict = {'1': '据说老师刚刚失恋了，授课状态很差', '2': '据说老师已经递交了辞职报告，授课状态很差',
                '3': '据说老师相亲去了，到现在状态都还没恢复。', '4': '据说老师家里节哀了，心情极度悲伤',
                '5': '据说老师钱包丢了，内心无比哀叹'}
        time.sleep(1)
        print(dict[num])