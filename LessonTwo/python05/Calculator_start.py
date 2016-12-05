#!/usr/bin/python
# -*- coding: utf-8 -*-
# 模拟表达式计算器（支持加减乘除和小括号）
# 本程序可以在windows下运行基于python2.7.8版本开发
# python05_homework
# __author__:The_thirteen_group_chensiqi

import re


TAG = True    #循环控制标志


def Remove_Redundance(str):
    '''
    去除冗余符号
    :param str: 表达式字符串
    :return: 去冗余的表达式字符串
    '''
    num = len (str)   #记录初始表达式的元素个数
    while TAG:
        while TAG:     #合并+-符号为-号
            a = re.sub('\+-', '-', str)
            if len(a) == len(str):
                break
            else:
                str = a
        while TAG:      #合并-+符号为-号
            a = re.sub('-\+', '-', str)
            if len(a) == len(str):
                break
            else:
                str = a
        while TAG:     #合并--符号为+号
            a = re.sub('-{2}','+',str)
            if len(a) == len(str):
                break
            else:
                str = a
        while TAG:     #合并++符号为+号
            a = re.sub('\+{2}', '+', str)
            if len(a) == len(str):
                break
            else:
                str = a
        while TAG:     #合并非法**符号为*号
            a = re.sub('\*{2}', '*', str)
            if len(a) == len(str):
                break
            else:
                str = a
        while TAG:     #合并非法//符号为/号
            a = re.sub('/{2}', '/', str)
            if len(a) == len(str):
                break
            else:
                str = a
        if len(str) == num:    #判断冗余符号是否去除完毕
            return str
        else:
            num = len(str)



def Operation(Str):
    '''
    加减乘除运算
    :param str:字符串表达式
    :return: 运算结果
    '''
    if Str.count('(') != 0:        #脱去括号的外衣
        Str = Str[1:len(Str)-1]
    Str = Remove_Redundance(Str)    #去除冗余符号
    if len(Str) <= 2:      #判断是否只是一个正数或者负数
        return Str
    else:
        return str(eval(Str))


def slice(str):
    '''
    用正则对表达式切片，
    切出括号里的部分并反复调用计算函数
    :param str:表达式字符串
    :return:计算结果
    '''
    if str.count('(') == 0:
        print ('无括号直接计算！')
        Re = Operation(str)
        return Re
    else:
        for i in range(str.count('(')):         #循环去除括号
            Tuple = re.search('\(.+?\)',str)
            Regular = str[list(Tuple.span())[0]:list(Tuple.span())[1]]
            print ('表达式{0}正则切片结果：{1}'.format(str,Regular))
            while TAG:
                if Regular.count('(') > 1:    #'('如果不等于1就继续切片
                    Regular = Regular[1:]
                    print ('括号太多继续加工，结果为：{0}'.format(Regular))
                    Tuple = re.search('\(.+?\)', Regular)
                    # print (Tuple.span())
                    Regular = Regular[list(Tuple.span())[0]:list(Tuple.span())[1]]
                    print ('继续切片结果：{0}'.format(Regular))
                else:
                    Result = Operation(Regular)                           #将切片进行运算
                    print ('{0}进行运算结果为：{1}'.format(Regular,Result))
                    str = str.replace(Regular, Result)                    #替换原表达式
                    print ('将原表达式的切片结果进行替换，替换后为：{0}'.format(str))
                    break
        finally_result = Operation(str)
        return finally_result








def EX_check(str):
    '''
    判断运算表达式是否合法
    :param str:算数表达式
    :return: True or False
    '''
    a = str.replace('(','')
    b = a.replace(')','')
    c = b.replace('+','')
    d = c.replace('-','')
    e = d.replace('*','')
    f = e.replace('/','')
    g = re.sub('\d+','',f)
    if len(g) == 0 and str.count('(') == str.count(')'):
        return True
    else:
        return False


def Main():
    while TAG:
        print '''
                            欢迎来到表达式计算器

            友情提示：本程序会自动将以下符号合并：
                            ++符号合并为-；
                            --符号合并为+；
                            +-符号合并为-；
                            -+符号合并为-；
                            //符号合并为/;
                            **符号合并为*;
            注意：请不要输入诸如：-/,+/，-*,+*,/*,*/等的让鄙人实在没法处理的符号逻辑
            另外(*,(/,/),*)这样的东东也不能出现-_-!

        '''
        EX = raw_input('请输入你想计算的表达式(只能计算+-*/和小括号)(输入n终止)：')
        if EX == 'n':
            break
        EX = re.sub('\s','',EX)                #去除空格
        Re = EX_check(EX)
        if Re == True:
            Result = slice(EX)
            print ('您的表达式的最终结果为{0}'.format(Result))
        else:
            print ('您的输入有误！')





if __name__ == '__main__':
    Main()