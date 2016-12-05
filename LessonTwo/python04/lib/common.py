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



def pwd_money_check(user):
    '''
    用户银行卡密码登录验证
    :return: True or False
    '''
    while TAG:
        pwd = raw_input('请输入6位银行卡密码：')
        if pwd.isdigit() and len(pwd) == 6:
            pwd_money = log_info_specific_read(user, 'pwd_money')
            if pwd_money == False:
                print ('用户日志不存在！')
                return False
            else:
                if MD5(pwd) == pwd_money:
                    print ('密码验证成功！')
                    return True
                else:
                    return False
        else:
            print ('您的输入有误!')


###########################前台请求输入方法组##################################################################

def name_login_input():
    '''
    键盘输入登录名
    :return:新用户名
    '''
    while TAG:
        name_login = raw_input('请输入登陆用户的用户名(n=返回上级菜单)：')
        if name_login == 'n':
            return
        elif os.path.exists('db/'+name_login+'_log'):
            print('你输入的用户名已存在，请重新输入！')
        elif len(name_login) != len(name_login.strip()) or len(name_login.strip().split()) != 1:
            print('登录名不能为空，且不能有空格，请重新输入！')
        else:
            return name_login


def pwd_login_input():
    '''
    键盘输入登录密码
    :return:新登录密码
    '''
    while TAG:
        pwd_login = raw_input('请输入登陆密码(n=返回上级菜单)：')
        if pwd_login == 'n':
            return
        elif len(pwd_login) < 8:
            print('您输入的密码不能小于8位数（8位以上字母数字+至少一位大写字母组合）,请重新输入！')
        elif len(pwd_login.strip().split()) != 1:
            print('您输入的密码不能有空格，密码也不能为空，请重新输入！')
        elif pwd_login.isdigit():
            print('密码不能全为数字（8位以上字母数字+至少一位大写字母组合），请重新输入！')
        elif pwd_login.lower() == pwd_login:
            print('请至少保留一位的大写字母（8位以上字母数字+至少一位大写字母组合），请重新输入！')
        else:
            pwd_login = MD5(pwd_login)
            return pwd_login


def account_input():
    '''
    键盘输入银行卡号
    :return: 新银行卡号
    '''
    while TAG:
        account = raw_input('请输入银行卡号(如果没有可以为空)(n=返回上级菜单)：')
        if account.strip() == '':
            account = 'empty'
            return account
        elif account == 'n':
            return
        elif len(account.strip()) < 16:
            print('银行卡号是不能小于16位的纯数字，请重新输入！')
        elif account.isdigit() != True:
            print('银行卡号是不能小于16位的纯数字，请重新输入！')
        else:
            return account


def pwd_money_input():
    '''
    键盘输入银行卡密码
    :return: 新银行卡密码
    '''
    while TAG:
        pwd_money = raw_input('请输入银行卡的6位数字取款（转账）密码(n=返回上级菜单)：')
        if pwd_money == 'n':
            return
        elif len(pwd_money.strip()) != 6:
            print('取款密码只能是6位纯数字，请重新输入！')
        elif pwd_money.strip().isdigit() != True:
            print('取款密码只能是6位纯数字，请重新输入！')
        else:
            pwd_money = MD5(pwd_money)
            return pwd_money




##################################数据读取写入方法组####################################################################


def log_info_read(user):
    '''
    指定用户日志文件全部读取
    :param user:用户名
    :return:dict字典
            如果无文件返回False
    '''
    if os.path.exists(DIR+user+'_log'):
        with open(DIR+user+'_log','r') as f:
            dict = pickle.load(f)
            return dict
    else:
        return False


def log_info_specific_read(user,text):
    '''
    指定用户日志文件指定内容读取
    :param user: 用户名
    :param text: 预读取的字段名
    :return: 指定的字段内容
            如果无文件返回False
    '''
    if os.path.exists(DIR+user+'_log'):
        with open(DIR+user+'_log','r') as f:
            dict = pickle.load(f)
            re = dict[text]
            return re
    else:
        return False


def log_info_write(user,dict = None):
    '''
    指定用户日志文件全部写入
    :param user:用户名
    :param dict: 日志字典
    :return: True or False
    '''
    #if os.path.exists(user+'_log'):
    #print (DIR+user+'_log')
    with open(DIR+user+'_log','w') as f:
        pickle.dump(dict,f)
        return True


def log_info_specific_write(user,dict):
    '''
    指定用户日志文件指定内容写入
    :param user: 用户名
    :param dict: 预修改的字典内容
    :return: True or False
    '''
    dictt = log_info_read(user)
    if dictt == False:
        print ('用户日志文件不存在！')
        return  False
    dictt[dict.keys()[0]] = dict[dict.keys()[0]]
    re = log_info_write(user,dictt)
    if re == True:
        return True
    else:
        return False


def log_info_billing_write(user,text):
    '''
    指定用户日志文件流水数据写入
    :param user: 用户名
    :param text: 用户流水数据
    :return: True or False
    '''

    dict = log_info_read(user)
    if dict == False:
        print ('用户日志文件不存在！')
        return False
    dict['Not_out_billing'].append(text)
    re = log_info_write(user, dict)
    if re == True:
        return True
    else:
        return False


###############################windows计划任务执行方法组#######################################################


def Autopay(user):
    '''
    自动还款模块
    :param user: 用户
    :return: True or False
    '''
    dict = log_info_read(user)
    tm = time.localtime()
    tm_text = str(tm.tm_year) + '-' + str(tm.tm_mon) + '-' + str(tm.tm_mday) + ' ' + str(tm.tm_hour) + ':' + str(tm.tm_min)
    if time.localtime().tm_mday == int(dict['Repayment_date']) and dict['Debt_Bill_amount'] != '0':
        if int(dict['cash']) >= int(dict['Debt_Bill_amount']):
            print ('用户{0}日期吻合触发自动还款！'.format(user))
            dict['cash'] = str(int(dict['cash']) - int(dict['Debt_Bill_amount']))
            dict['Actual_overdraft'] = str(int(dict['Actual_overdraft'])-int(dict['Debt_Bill_amount']))
            text = '{0}:触发“自动还款”操作，还款成功，还款总额为：{1},电子现金余额为{2},总透支金额为{3}'.format(tm_text,dict['Debt_Bill_amount'],dict['cash'],dict['Actual_overdraft'])
            # log_info_billing_write(user,'{0}:触发“自动还款”操作，还款成功，还款总额为：{1},电子现金余额为{2},总透支金额为{3}'.format(tm_text,dict['Debt_Bill_amount'],dict['cash'],dict['Actual_overdraft']))
            dict['Not_out_billing'].append(text)
            dict['Debt_Bill_amount'] = '0'
            log_info_write(user, dict)
            print ('用户{0}自动还款成功！'.format(user))
            return True
        else:
            print ('用户{0}自动还款失败！电子现金账户余额不足！请存够钱再行尝试'.format(user))
            log_info_billing_write(user,'{0}：触发“自动还款”操作，还款失败，失败原因：电子现金余额不足。还款总额为：{1},电子现金余额为{2}，总透支金额为{3}'.format(tm_text,dict['Debt_Bill_amount'],dict['cash'],dict['Actual_overdraft']))
            return False
    else:
        return


def AutoBilling(user):
    '''
    账单自动生成模块
    :param user: 用户
    :return:True or False
    '''
    dict = log_info_read(user)
    time_year = time.localtime().tm_year
    time_mon = time.localtime().tm_mon
    time_mday = time.localtime().tm_mday
    date = str(time_year)+'-'+str(time_mon)

    text = '''
                            亲爱的{0}，您的{1}年{2}月账单如下：

                          账单总金额为:{3}(当期+历史欠账)，最后还款日为下月{4}日
                            请您按时还款，谢谢您的使用，再见！'''.format(user,str(time_year),str(time_mon),dict['Actual_overdraft'],dict['Repayment_date'])
    if date not in dict['Debt_record']:
        dict['Debt_record'][date] = text
        dict['Debt_Bill_amount'] = dict['Actual_overdraft']
    if date not in dict['Has_been_out_billing']:
        dict['Has_been_out_billing'][date] = dict['Not_out_billing']
        dict['Not_out_billing'] = []
    log_info_write(user,dict)




def Traverse_folder():
    '''
    根据条件遍历某文件夹里的全部文件内容，
    找出符合条件的文件后调用自动执行模块
    （需windows计划任务触发）
    :return:None
    '''
    list = os.listdir(DIR)
    time_year = time.localtime().tm_year
    time_mon = time.localtime().tm_mon
    time_mday = time.localtime().tm_mday
    for i in list:
        if i == '__init__.py' or i == '__init__.pyc':
            continue
        else:
            name = i.strip().split('_')[0]
            dict = log_info_read(name)
            if dict['billing_day'] == str(time_mday):
                AutoBilling(name)
            if dict['Repayment_date'] == str(time_mday):
                Autopay(name)


def test():
    '''
    自动还款测试函数
    :return:None
    '''
    dict = log_info_read('chensiqi')
    dict['Debt_Bill_amount'] = '4000'
    dict['cash'] = '5000'
    dict['Actual_overdraft'] = '5000'
    dict ['Repayment_date'] = '6'
    log_info_write('chensiqi',dict)
    print (dict['Not_out_billing'])







