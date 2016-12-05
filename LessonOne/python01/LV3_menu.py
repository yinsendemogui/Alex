#!/usr/bin/python
# -*- coding: utf-8 -*-
#模拟三级菜单
#python01_homework02

num1 = {'北京':['北京东部','北京南部','北京西部','北京北部'],'上海':['上海东部','上海南部','上海西部','上海北部']}
num1_1 = {'北京东部':['东上','东中','东下'],'北京南部':['南上','南中','南下'],'北京西部':['西上','西中','西下'],'北京北部':['北上','北中','北下']}
num1_2 = {'上海东部':['东上','东中','东下'],'上海南部':['南上','南中','南下'],'上海西部':['西上','西中','西下'],'上海北部':['北上','北中','北下']}

while True :
    print "一级菜单：{0} {1}".format(num1.keys()[0],num1.keys()[1])
    decide = raw_input("请输入您的选择or（b=返回上级q=退出程序）：")
    if decide == 'b' :
        print '已经是第一级菜单了，不能继续返回，请重新输入选择！'
        continue
    elif decide == 'q' :
        print '程序退出!'
        exit()
    elif decide in num1 :
        while True :
            print "二级菜单：{0} {1} {2} {3}".format(num1[decide][0],num1[decide][1],num1[decide][2],num1[decide][3])
            decide2 = raw_input('请输入您的选择or（b=返回上级q=退出程序）：')
            if decide2 == 'b' :
                break
            elif decide2 == 'q' :
                print '程序退出'
                exit()
            elif decide2 in num1_1 :
                print '三级菜单：{0} {1} {2}'.format(num1_1[decide2][0],num1_1[decide2][1],num1_1[decide2][2])
                print '三级菜单已经到达，程序退出！'
                exit()
            elif decide2 in num1_2 :
                print '三级菜单：{0} {1} {2}'.format(num1_2[decide2][0],num1_2[decide2][1],num1_2[decide2][2])
                print '三级菜单已经到达，程序退出！'
                exit()
            else:
                print '您的选择有误，请重新输入！'
    else :
        print '您的选择有误，请重新输入！'
