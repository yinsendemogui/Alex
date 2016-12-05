#!/usr/bin/python
# -*- coding: utf-8 -*-
#模拟用户登录接口
#python01_homework01

sorce = {'chensiqi':'666666','chensiqi1':'666666','chensiqi2':'666666','chensiqi3':'666666'} #账号密码字典
error = [] #账号锁定列表
while True:
    name = input('请输入登录用户的用户名：')
    if name in error:
        print ("用户已经被锁定，请尝试登录其他用户！")
    elif name in sorce :
        passwd = input("请输入登录用户名的密码：")
        i = 0
        while True :
            if passwd == sorce[name] :
                print ("欢迎你，登陆成功！")
                exit()
            elif i == 2 :
                print ("您的密码已经连续输错3次，{0}账户已经被锁定！请尝试登录其他用户.".format(name))
                error.append(name)
                break
            else :
                passwd = input("您的密码输入错误，请重新输入：")
                i += 1
        else :
            print ("用户名输入有误，请重新输入！")
