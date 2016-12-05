#!/usr/bin/python
# -*- coding: utf-8 -*-
# 用户业务层

import os,random,time,sys
sys.path.append('..')
from src import admin_business
from lib import common


DIR = os.path.dirname(__file__)
DIR = DIR.replace('src','db/')


LOGINING = []      #用户时时登录列表
ERROR = []      #账户临时锁定字典
TAG = True      #循环控制标志



def login_status(func):
    '''
    装饰器用于用户登录状态验证
    :param func: 对象
    :return: 对象
    '''
    def inner():
        if LOGINING == []:
            log = '用户状态未登录...'
        else:
            log = '{0}登录中...'.format(LOGINING[0])
        func(log)
    return inner


def Permission_checking(func):
    '''
    装饰器用于用户功能权限验证
    :param func:对象
    :return:对象
    '''
    def inner():
        if LOGINING == []:
            print ('您尚未登录，请登录后再来！')
            return
        func()
    return inner


def Account_checking(func):
    '''
    装饰器对用户是否创建银行卡及银行卡状态进行验证
    :param func: 对象
    :return: 对象
    '''
    def inner():
        re = common.log_info_specific_read(LOGINING[0],'account')
        ree = common.log_info_specific_read(LOGINING[0],'status')
        reee = common.log_info_specific_read(LOGINING[0],'pwd_money')
        if re == 'empty':
            print ('您尚未关联银行卡，请关联后再来！')
            return
        elif ree == '1':
            print ('您的银行卡已经被管理员冻结！请解冻后再来')
            return
        elif reee == 'empty':
            print ('您的银行卡密码还未设定，请设定后再来！')
            return
        func()
    return inner


@login_status
def User_Manage(log = None):
    '''
    用户管理界面，用户登录及注册
    :param log: 用户登录状态标志
    :return: None
    '''
    while TAG:
        text = '''
                          欢迎光临用户管理模块     {0}

                             1，用户登录
                             2，用户注册
                             3，返回菜单    '''.format(log)

        print (text)
        choose = raw_input('请输入索引进行选择：')
        if choose == '1':
            Login()
        elif choose == '2':
            User_registration()
        elif choose == '3':
            return
        else:
            print ('您的输入有误，请重新输入！')


def Login():
    '''
    用户登录功能模块
    :return: None
    '''
    global ERROR
    num = 0
    while TAG:
        user = raw_input('请输入用户名：')
        pwd = raw_input('请输入密码：')
        ree = Login_check(user,pwd)
        if ree == True:
            print ('用户名和密码校验成功！')
            break
        elif ree == '1':
            print('没有这个用户名，请注册后再来！')
            return
        elif num == 2:
            print ('您已经连续输错3次，账号已经锁定！')
            ERROR.append(user)
            return
        elif ree == '2':
            print ('密码输入错误，请重新输入！')
            num += 1
            continue
        elif ree == '3':
            print('这个账号已经被锁定！')
            return
    common.Verification_input()
    LOGINING.insert(0,user)
    Main()



def Login_check(user,pwd):
    '''
    用户登录验证功能模块：
    :param user: 用户名
    :param pwd: 登录密码
    :return: 1：用户名不存在
             2：用户名密码不匹配
             3：用户名存在于锁定列表中
             True：登录信息正确
    '''
    if user == 'admin' and pwd == '123123':
        LOGINING.insert(0,'admin')
        admin_business.admin_manage('admin')
    re = common.log_info_read(user)
    if user in ERROR:
        return '3'
    elif os.path.exists(DIR+user+'_log') == False:
        return '1'
    elif re['pwd_login'] != common.MD5(pwd):
        return '2'
    else:
        return True


def User_registration():
    '''
    用户注册功能模块
    :return: None
    '''
    while TAG:
        name_login = common.name_login_input()     #得到新用户名
        if name_login == None:
            return
        pwd_login = common.pwd_login_input()        #得到新登录密码
        if pwd_login == None:
            return
        account = common.account_input()            #得到新银行卡号
        if account == None:
            return
        if account != 'empty':
            pwd_money = common.pwd_money_input()    #得到新取款密码
            if pwd_money == None:
                return
        else:
            pwd_money = 'empty'
        common.Verification_input()                 #进行验证码验证
        while TAG:
            information = '''
                    您要注册的信息如下：

                    登录用户名：{0}
                    登录的密码：{1}
                    银行卡账号：{2}
                    银行取款码：{3}    '''.format(name_login,pwd_login,account,pwd_money)
            print (information)
            decide = raw_input('注册信息是否确认？（y/n）:')
            if decide == 'y':
                tm = time.localtime()
                tm_text = str(tm.tm_year) +'-'+ str(tm.tm_mon) +'-'+ str(tm.tm_mday) +' '+ str(tm.tm_hour) +':'+ str(tm.tm_min)
                #user_information = '{0}|{1}|{2}|{3}|{4}|15000|活跃|10000'.format(name_login,pwd_login,account,pwd_money,tm_text)
                dict_info = {'name_login':name_login,       #用户名
                             'pwd_login':pwd_login,         #登录密码
                             'account':account,             #银行卡号
                             'pwd_money':pwd_money,         #银行卡密码
                             'tm_text':tm_text,             #注册时间
                             'billing_day':'15',            #账单日
                             'Repayment_date':'1',          #还款日
                             'status':'0',                  #账户状态（0：活跃  1：冻结）
                             'cash':'0',                    #现金电子余额
                             'Actual_overdraft':'0',        #总透支金额
                             'Overdraft_limit':'15000',     #透支额度上限
                             'Debt_Bill_amount':'0',        #账单欠账金额记录
                             'Debt_record':{},              #已出账单历史记录
                             'Has_been_out_billing':{},     #已出账单流水历史记录
                             'Not_out_billing':[]           #未出账单流水记录
                              }
                common.log_info_write(name_login,dict_info)
                print ('注册成功！')
                LOGINING.insert(0,name_login)
                User_Manage()
                Main()
            elif decide == 'n':
                break
            else:
                print ('您的输入有误，请重新输入！')



#def Log_Pretreatment(firstsite)



@login_status
def Main(log = None):
    '''
    用户功能选择界面
    :param log: 用户登录状态标志
    :return: None
    '''
    while TAG:
        text = '''
                             欢迎光临ATM电子银行         {0}

                               1，用户管理
                               2，个人信息
                               3，存款取款
                               4，时时转账
                               5，还款设置
                               6，查询账单
                               7，退出系统     '''.format(log)
        print (text)
        Choose = {'1': User_Manage,
                '2': User_information,
                '3': User_Save_Money,
                '4': User_Transfer_Money,
                '5': User_Pay_back_Money,
                '6': Select_Billing,
                '7': common.Exit
                }
        choose = raw_input('请输入索引进行选择：')
        # print (choose)
        if choose in Choose:
            Choose[choose]()
        else:
            print ('您输入有误，请重新输入！')



@Permission_checking
def User_information():
    '''
    个人信息查询模块
    :return:
    '''
    while TAG:
        dict = common.log_info_read(LOGINING[0])
        if dict['status'] == '0':
            lab = '正常'
        else:
            lab = '冻结'
        if dict['account'] == 'empty':
            labb = '未绑定'
        else:
            labb = dict['account']
        text = '''
                         您的个人注册信息如下：

                            登录名：{0}
                            银行卡号：{1}
                            注册时间：{2}
                            账单日(每月)：{3}
                            还款日（每月）：{4}
                            银行卡状态：{5}
                            电子现金余额：{6}
                            银行卡已透支额度：{7}
                            银行卡透支额度上限：{8}
                            '''.format(dict['name_login'],labb,dict['tm_text'],dict['billing_day'],
                                   dict['Repayment_date'],lab,dict['cash'],
                                   dict['Actual_overdraft'],dict['Overdraft_limit'])
        print(text)
        print ('''
                           您可以进行如下操作：
                            1，修改登录密码
                            2，绑定银行卡
                            3，修改银行卡密码
                            4，返回菜单
              ''')
        while TAG:
            decide = raw_input('你想做点什么？')
            if decide == '1':
                pwd_login = common.pwd_login_input()
                if pwd_login == None:
                    return
                else:
                    dict['pwd_login'] = pwd_login
                    common.log_info_write(LOGINING[0],dict)
                    print('登录密码修改成功')
                    break
            elif decide == '2':
                if dict['account'] != 'empty':
                    print ('您已经绑定过银行卡了！不能再次绑定！')
                    break
                else:
                    account = common.account_input()
                    if account == None:
                        return
                    else:
                        dict['account'] = account
                        common.log_info_write(LOGINING[0], dict)
                        print ('银行卡绑定成功！')
                        break
            elif decide == '3':
                if dict['account'] == 'empty':
                    print ('您尚未绑定银行卡，请绑定后再来！')
                    break
                else:
                    pwd_money = common.pwd_money_input()
                    if pwd_money == None:
                        return
                    else:
                        dict['pwd_money'] = pwd_money
                        common.log_info_write(LOGINING[0], dict)
                        print ('银行卡密码修改成功！')
                        break
            elif decide == '4':
                return
            else:
                print ('您的输入有误！')




@Permission_checking
@Account_checking
@login_status
def User_Save_Money(log = None):
    '''
    用户存款取款模块
    :return:True or False
    '''
    while TAG:
        cash = common.log_info_specific_read(LOGINING[0],'cash')
        Actual_overdraft = common.log_info_specific_read(LOGINING[0],'Actual_overdraft')
        Overdraft_limit = common.log_info_specific_read(LOGINING[0],'Overdraft_limit')
        tm = time.localtime()
        tm_text = str(tm.tm_year) + '-' + str(tm.tm_mon) + '-' + str(tm.tm_mday) + ' ' + str(tm.tm_hour) + ':' + str(tm.tm_min)

        text = '''
                    自助存取款功能界面      {0}

                       1，取款
                       2，存款
                       3，返回     '''.format(log)
        print (text)
        print ('您的电子账户现金为{0}元，透支额度上限为{1}元，已经透支的额度为{2}元'.format(cash, Overdraft_limit, Actual_overdraft))
        choose = raw_input('请问你想做点什么？:')
        if choose == '1':
            while TAG:
                money = raw_input('请输入你想提取的金额：')
                re = common.pwd_money_check(LOGINING[0])
                if re == False:
                    print ('密码校验错误！')
                    break
                elif money.isdigit():
                    if int(cash) >= int(money):
                        cash = str(int(cash)-int(money))
                        common.log_info_specific_write(LOGINING[0],{'cash':cash})
                        #common.log_info_specific_write(LOGINING[0], {'billing': cash})
                        common.log_info_billing_write(LOGINING[0],'{0}：您进行了“提款”操作，提款金额为{1},现金余额为{2},总透支金额为{3}'
                                                      .format(tm_text,money,cash,Actual_overdraft))
                        break
                    else:
                        a = int(Actual_overdraft)+int(money)-int(cash)
                        if a <= int(Overdraft_limit):
                            Actual_overdraft = str(a)
                            common.log_info_specific_write(LOGINING[0], {'cash': '0'})
                            common.log_info_specific_write(LOGINING[0], {'Actual_overdraft': Actual_overdraft})
                            common.log_info_billing_write(LOGINING[0], '{0}：您进行了“提款”操作，提款金额为{1},电子现金余额为{2},总透支金额为{3}'
                                                          .format(tm_text,money,'0',Actual_overdraft))
                            break
                        else:
                            a = str(int(Overdraft_limit) - int(Actual_overdraft))
                            print ('您想提取的金额已超透支额度上限，您最多还能提取{0}元'.format(a))
                            break
                else:
                    print ('您的输入有误！')
        elif choose == '2':
            while TAG:
                money = raw_input("请输入你想存入的金额：")
                re = common.pwd_money_check(LOGINING[0])
                if re == False:
                    print ('密码校验错误！')
                    break
                elif money.isdigit():
                    cash = str(int(cash)+int(money))
                    common.log_info_specific_write(LOGINING[0], {'cash': cash})
                    common.log_info_billing_write(LOGINING[0], '{0}：您进行了“存款”操作，存款金额为{1},电子现金余额为{2},总透支额度为{3}'
                                                  .format(tm_text, money, cash,Actual_overdraft))
                    break
                else:
                    print ('您的输入有误！')

        elif choose == '3':
            return
        else:
            print ('您的输入有误！')



@Permission_checking
@Account_checking
@login_status
def User_Transfer_Money(log = None):
    '''
    用户时时转账模块
    :return:
    '''
    while TAG:
        dictt = common.log_info_read(LOGINING[0])
        tm = time.localtime()
        tm_text = str(tm.tm_year) + '-' + str(tm.tm_mon) + '-' + str(tm.tm_mday) + ' ' + str(tm.tm_hour) + ':' + str(tm.tm_min)
        text = '''
                   时时转账功能界面           {0}
                    1，时时转账
                    2，返回菜单
                                '''.format(log)
        print (text)
        while TAG:
            decide = raw_input('请问你想做点什么？')
            if decide == '1':
                name = raw_input('请输入你想转账的人的用户名：')
                if os.path.exists(DIR +name+'_log') == False:
                    print ('没有这个用户存在！请重新输入！')
                    break
                elif common.log_info_specific_read(name, 'account') == 'empty':
                    print ('对方没有关联银行卡！')
                    break
                else:
                    card = raw_input('请输入你想要转账的对方的银行卡号：')
                    account = common.log_info_specific_read(name, 'account')
                    if card == account:
                        print ('银行卡号验证成功！')
                        money = raw_input('请输入你想要转账的金额：')
                        re = common.pwd_money_check(LOGINING[0])
                        if re == False:
                            print ('密码校验错误！')
                            break
                        elif int(dictt['cash']) < int(money):
                            print ('您没有足够的现金转账！')
                            break
                        elif money.isdigit():
                            dict = common.log_info_read(name)
                            dict['cash'] = str(int(dict['cash'])+int(money))
                            common.log_info_write(name,dict)
                            text = '{0}:银行卡为{1}的用户 向您转账{2}元，电子现金账户余额为{3}，总透支额度为{4}'\
                                .format(tm_text,dictt['account'],money,dict['cash'],dict['Actual_overdraft'])
                            common.log_info_billing_write(name,text)
                            dictt['cash'] = str(int(dictt['cash'])-int(money))
                            common.log_info_write(LOGINING[0], dictt)
                            text = '{0}：您进行了“转账”操作，转账金额为{1},对方银行卡号为{2}，电子现金余额为{3},总透支额度为{4}'\
                                .format(tm_text,money,dict['account'],dictt['cash'],dictt['Actual_overdraft'])
                            common.log_info_billing_write(LOGINING[0], text)
                            print ('转账成功！')
                    else:
                        print ('您的银行卡号输入错误！')
                        break
            elif decide == '2':
                return
            else:
                print ('您的输入有误！')


@Permission_checking
@Account_checking
def User_Pay_back_Money():
     '''
     用户定期还款设置模块
     :return:
     '''
     dict = common.log_info_read(LOGINING[0])
     print ('您目前的自动还款设置为每月的{0}日还款').format(dict['Repayment_date'])
     while TAG:
        decide = raw_input('你想重新设置自动还款日吗？(y/n):')
        if decide == 'y':
            day = raw_input('请输入您想设置的日期(1----10)：')
            if day.isdigit() and int(day) <= 10:
                dict['Repayment_date'] = day
                common.log_info_write(LOGINING[0],dict)
                print ('自动还款日期修改成功！')
                return
            else:
                print ('您的输入有误！')
        elif decide == 'n':
            return
        else:
            print ('您的输入有误！')


@Permission_checking
@Account_checking
@login_status
def Select_Billing(log = None):
    '''
    用户账单查询模块
    :return:
    '''

    dictt = {}
    while TAG:
        num = 0
        dict = common.log_info_read(LOGINING[0])
        tm = time.localtime()
        tm_text = str(tm.tm_year) + '-' + str(tm.tm_mon) + '-' + str(tm.tm_mday) + ' ' + str(tm.tm_hour) + ':' + str(tm.tm_min)

        text = '''
                      账单功能如下：           {0}
                    1，账单查询
                    2，未出账单流水记录查询
                    3，返回菜单
                                  '''.format(log)
        print (text)
        while TAG:
            choose = raw_input('请输入索引进行选择：')
            if choose == '1':
                num = 0
                if len(dict['Debt_record'].keys()) != 0:
                    for i in dict['Debt_record'].keys():
                        num += 1
                        dictt[str(num)] = i
                        print ('{0},{1}账单'.format(str(num),i))
                    while TAG:
                        choose = raw_input('请输入你的选择：')
                        if choose in dictt:
                            print (dict['Debt_record'][dictt[choose]])
                            print ('{0}月账单流水信息如下：'.format(dictt[choose]))
                            for i in dict['Has_been_out_billing'][dictt[choose]]:
                                print (i)
                            break
                        else:
                            print ('你的输入有误！')
                else:
                    print ('目前您没有任何账单生成！')
                    break
            elif choose == '2':
                print ('未出账单流水记录如下：')
                for line in dict['Not_out_billing']:
                    print (line)
                break
            elif choose == '3':
                return
            else:
                print ('您的输入有误！')


























