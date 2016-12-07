#!usr/bin/env python
# -*- coding:utf-8 -*-
# auther:Mr.chen
# 描述：

#!/usr/bin/python
# -*- coding: utf-8 -*-
# 公共方法层

import os,time,random,pickle

DIR = os.path.dirname(__file__)
DIR = DIR.replace('lib','db/')


TAG = True      #循环控制标志


def Exit():
    '''
    系统退出
    :return:None
    '''
    print ('程序退出！')
    exit()


def MD5(password):
    '''
    加密函数
    :param firstsite: 密码字符串
    :return: 加密字符串
    '''
    import hashlib
    return hashlib.md5(password).hexdigest()


def Verification_input():
    '''
    登录验证码校验
    :return: True
    '''
    while TAG:
        re = Verification_Code()
        code = raw_input('请输入括号里的验证码,不区分大小写({0}):'.format(re))
        if code.strip().lower() != re.lower():
            print('您输入的验证码有误，请重新输入！')
        else:
            return True


def Verification_Code():
    '''
    生成随机的6位验证码：大小写字母数字的组合
    :return: 验证码
    '''
    code = ''
    b = random.randrange(0, 5)
    c = random.randrange(0, 5)
    for i in range(6):
        if i == b:
            a = random.randrange(1, 9)
            code = code + str(a)
        else:
            a = random.randrange(65, 90)
            if i == c:
                code = code + chr(a).lower()
            else:
                code = code + chr(a)
    return code





def log_info_read(dir):
    '''
    配置文件全部读取
    :param user:用户名
    :return:dict字典
            如果无文件返回False
    '''
    if os.path.exists(dir):
        with open(dir,'r') as f:
            dict = pickle.load(f)
            return dict
    else:
        return False




def log_info_write(dir,dict):
    '''
    配置文件全部写入
    :param user:用户名
    :param dict: 日志字典
    :return: True or False
    '''
    #if os.path.exists(user+'_log'):
    #print (DIR+user+'_log')
    with open(dir,'w') as f:
        pickle.dump(dict,f)
        return True

