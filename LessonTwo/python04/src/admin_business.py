#!/usr/bin/python
# -*- coding: utf-8 -*-
# 管理员业务层


from lib import common
import user_business
import os
DIR = os.path.dirname(__file__)
DIR = DIR.replace('src','db/')


LOGINING = []      #用户时时登录列表
TAG = True      #循环控制标志


def admin_manage(log = None):
    '''
    管理员操作界面，只有管理员能进
    :param log: 用户登录状态标志
    :return: None
    '''
    while TAG:
        text = '''
                          欢迎光临管理员操作界面        {0}

                             1，添加用户银行卡号
                             2，指定用户透支额度
                             3，冻结用户银行卡号
                             4，系统退出             '''.format(log)
        print (text)
        while TAG:
            choose = raw_input('管理员你好，你想做点什么？：')
            if choose in {'1','2','3','4'}:
                if choose == '1':
                    admin_add_bankcard()
                    break
                elif choose == '2':
                    admin_Overdraft_limit()
                    break
                elif choose == '3':
                    admin_Freeze_bankcard()
                    break
                elif choose == '4':
                    common.Exit()
            else:
                print ('您的输入有误！')


def admin_add_bankcard():
    '''
    给没有关联银行卡的用户关联银行卡号
    :return:None
    '''
    dict = {}
    print ('尚未建立银行卡关联信息的账户如下：\n')
    list = os.listdir(DIR)
    num = 0
    for i in list:
        if i == '__init__.py' or i == '__init__.pyc':
            continue
        else:
            re_dict = common.log_info_read(i.strip().split('_')[0])
            if re_dict['account'] == 'empty':
                num += 1
                print ('{0} 登录名称：{1}  \n'.format(num,re_dict['name_login']))
                dict[str(num)] = re_dict['name_login']
    while TAG:
        choose = raw_input('输入索引选择你想添加银行卡的用户(n = 返回上级菜单):')
        if choose == 'n':
            return
        elif choose in dict:
            account = common.account_input()
            re_dict = common.log_info_read(dict[choose])
            re_dict['account'] = account
            common.log_info_write(dict[choose],re_dict)
            print ('用户{0}的银行卡关联成功'.format(dict[choose]))
        else:
            print('您输入的信息有误！')



def admin_Overdraft_limit():
    '''
    修改用户银行卡的透支额度
    :return:None
    '''
    dict = {}
    print ('所有用户额度信息如下：\n')
    list = os.listdir(DIR)
    num = 0
    for i in list:
        if i == '__init__.py' or i == '__init__.pyc':
            continue
        else:
            re_dict = common.log_info_read(i.strip().split('_')[0])
            num += 1
            print ('{0} 登录名称：{1}  透支额度为：{2}  \n'.format(num, re_dict['name_login'],re_dict['Overdraft_limit']))
            dict[str(num)] = re_dict['name_login']
    while TAG:
        choose = raw_input('输入索引选择你想修改额度的账户(n = 返回上级菜单):')
        if choose == 'n':
            return
        elif choose in dict:
            Quota = raw_input('你想把额度改成多少？：')
            re_dict = common.log_info_read(dict[choose])
            re_dict['Overdraft_limit'] = Quota
            common.log_info_write(dict[choose], re_dict)
            print ('用户{0}的额度修改成功！'.format(dict[choose]))
        else:
            print('您输入的信息有误！')



def admin_Freeze_bankcard():
    '''
    冻结or解冻用户的银行卡号
    :return:None
    '''
    dict = {}
    print ('所有已关联银行卡的用户的银行卡状态信息如下：\n')
    list = os.listdir(DIR)
    num = 0
    for i in list:
        if i == '__init__.py' or i == '__init__.pyc':
            continue
        else:
            re_dict = common.log_info_read(i.strip().split('_')[0])
            if re_dict['account'] != 'empty':
                num += 1
                if re_dict['status'] == '0':
                    lab = '活跃'
                else:
                    lab = '冻结'
                print ('{0} 登录名称：{1}  账户状态：{2} \n'.format(num, re_dict['name_login'],lab))
                dict[str(num)] = re_dict['name_login']
    while TAG:
        choose = raw_input('输入索引选择用户来改变他的银行卡状态（活跃-->冻结-->活跃）(n = 返回上级菜单):')
        if choose == 'n':
            return
        elif choose in dict:
            re_dict = common.log_info_read(dict[choose])
            if  re_dict['status'] == '0':
                labb = '冻结'
                labbb = '1'
            else:
                labb = '活跃'
                labbb = '0'
            decide = raw_input('你确定要将用户{0}的银行卡的状态改成{1}吗？（y/n）:'.format(dict[choose],labb))
            if decide == 'n':
                return
            re_dict['status'] = labbb
            common.log_info_write(dict[choose], re_dict)
            print('用户{0}的银行卡的状态信息已经改变！'.format(dict[choose]))
        else:
            print('您输入的信息有误！')





