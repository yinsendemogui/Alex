#!usr/bin/env python
# -*- coding:utf-8 -*-
# auther:Mr.chen
# 描述：教师模型类


class teacher_Model:
    '''
    教师模型类
    '''
    def __init__(self,name,age,sex):
        self.Name = name    #姓名
        self.Age = age      #年龄
        self.Sex = sex      #性别
        self.__Calary = 0     #工资

    def teacher_Accident(self):   #教学事故
        self.__Calary -= 10


    def teacher_Success(self,cost):   #教学成功
        self.__Calary += int(cost)


    def calary_Return(self):   #返回工资数据
        return self.__Calary




