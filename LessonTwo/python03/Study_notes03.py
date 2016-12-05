#!/usr/bin/python
# -*- coding: utf-8 -*-
# python第三周学习摘记
#__author__:The_thirteen_group_chensiqi

# #函数的返回值
# def sendmail():
#     import smtplib
#     from email.mine.firstsite import MIMEText
#     from email.utils import formataddr
#     try:
#         msg = MIMEText('邮件内容','plain','utf-8')
#         msg['From'] = formataddr(["武沛齐",'wptawy@126.com'])
#         msg['To'] = formataddr("陈思齐",'215379068@qq.com')
#         msg['Subject'] = "主题"
#
#         server = smtplib.SMTP("smtp.126.com",25)
#         server.login("wptamy@126.com","ww.3945.59")
#         server.sendmail('wptawy@126.com',['215379068@qq.com',],msg.as_string())
#         server.quit()
#     except:
#         # 发送失败
#         return False
#     else:
#         # 发送成功
#         return True
# ret = sendmail()
# print (ret)
# if ret == True :
#     print ('发送成功')
# else:
#     print ('发送失败')
#
# def f1():
#     print (123)
#
#     return "111"
#     print (456)
# r = f1()
# print (r)
#
# def f2():
#     print (123)
#
# r = f2()
# print (r)
#
# #函数的参数
# #1,普通参数
# #2，默认参数(必须放置在参数列表的最后）
# #3，指定参数
# #4，* （可以接收任意个参数,并且以元组的形式储存每个参数）
# #5，** （将参数转化为字典的形式存储）
# #6，万能参数 *args **kwargs
#
#
#
# def send(xxoo,xx,content):
#     print (xxoo,content)
#     return True
# send('alex','sb')
#
# def f1(*args):
#     print (args)
#
# f1(11,22,'alex','hhhh')
# li = [11,22,'alex','hhhh']
# f1(li)
#
# def f1(*args,**kwargs):
#     print (args)
#     print (kwargs)
#
# f1(11,22,33,44,k1='v1',k2='v2')
#
# s1 = 'i am {0} ,age {1}'.format('alex',18)
# print (s1)
# s2 = "i am {0},age {1}".format(*['alex',18])
# print(s2)
#
# s3 = "i am {name},age {age}".format(age = 18,name = 'alex')
# print (s3)
#
# dic = {'name':'alex','age':18}
# s4 = "i am {name},age {age}".format(**dic)
# print (s4)
#
# #函数内容补充
# #全局变量用全部大写
# def f1(a1,a2):
#     global name # 表示name是全局变量
#     return a1 + a2
#
# def f1(a1,a2):
#     return a1 * a2
#
# ret = f1(8,8)
# print (ret)
# #全局变量，所有作用域都可读
# name = "alex"
#
# def f1():
#     age = 18
#     print (age,name)
#
# def f2():
#     age = 19
#     print (age,name)
#
# f1()
#
# #实例：函数式编程实现登录和注册
# def login(username,password):
#     """
#     :param username:用户输入的用户名
#     :param password: 用户输入的密码
#     :return:
#     """
#     f = open("db",'r')
#     for line in f:
#         line_list = line.split("|")
#         if line_list[0] == username and line_list[1] == password :
#             return True
#         else:
#             return False
#     f.close()
#
# def register(username,password):
#     """
#     用于用户注册
#     :param username:用户输入的用户名
#     :param password: 用户输入的密码
#     :return:
#     """
#     f = open("db",'a')
#     temp = username + "|" + password
#     f.write(temp+"\n")
#     f.close()
#
# def main():
#     t = raw_input("1:登录；2：注册")
#     if t == '1':
#         user = raw_input("请输入用户名：")
#         pwd = raw_input("请输入密码：")
#         r = login(user,pwd)
#         if r :
#             print ("登录成功")
#         else:
#             print ("登录失败")
#     elif t == '2':
#         user = raw_input("请输入用户名：")
#         pwd = raw_input("请输入密码：")
#         r = register(user,pwd)
#
# main()
#
# #三元运算
# if 1 = 1:
#     name = "alex"
#
# else:
#     name = "SB"
#
# name = "alex" if 1 == 1 else "SB"
#
# #lambda表达式
# def f1(a1):
#     return a1 + 100
#
# f2 = lambda a1,a2: a1+ 100
#
# ret = f1(10)
# print (ret)
#
# r2 = f2(9)
#
#
#
# #内置函数
#
# #all 所有为真，才为真
# #n = all([1,2,3,4,None])
# #print (n)
# #any 只要有真，就为真
# #n = any([[],0,"",None])
# #print (n)
#
#
# #ascii()  #自动执行对象的__str__方式
# #class Foo:
# #    def __repr__(self):
# #        return "111"
# #
# #n = ascii(Foo())
# #print (n)
#
# #bin() 转成二进制
# #oct() 转成8进制
# #hex() 转成16进制
#
# #print (bin(7))
# #print (oct(9))
# #print (hex(15))
#
# #字符串转换字节类型
# #bytes(只要转换的字符串，按照什么编码）
# #n = bytes("陈思齐", encoding="gbk")
# #print (n)
#
# #文件操作
#
# #打开文件
# #f = open('db','r')#只读
# #f = open('db','w')#只写，先清空原文件
#
# #f = open('db','x')#如果文件存在报错，不存在创建并写内容
# #f = open('db','a')#追加
# #f = open('db','a')#追加
#
#
# # 操作文件
# # 通过源码查看功能
# # 关闭文件
# # f.close()
# # with open('xb') as f:
#
# # f = open('db','r')
# # data = f.read()
# # print (data,type(data))
# # f.close()
#
# # f = open('db','r')
# # # data = f.read()
# # # print (data,type(data))
# # f = open('db','ab')
# # f.write('hello')
# # f.close()
#
# # f = open("db",'r+')
# # data = f.read(1)
# # print (data)
# # f.write('777')
# # f.close()
#
# f = open('db','r+')
# data = f.read()
# print(data)
# # print (f.tell())
# # f.write('你好')
# # print (f.tell())
# # f.seek(1)
# # f.write('888')
# # f.close()
#
# read()#无参数，读全部，有参数，（打开方式无b，按字符，有b，按字符）
# write()#写数据，（打开方式有b，按字节写入，打开方式无b，按字符写入）
#
# #
# # #truncate()根据指针位置截取数据，指针后数据清空
# # f = open('db','r+',encoding='utf-8')
# # f.seek(3)
# # f.truncate()
# # f.close()
# #for循环文件对象
# # f = open('db','r+',encoding='utf-8')
# #
# # for line in f:
# #     print (line)
# #
# # with open('db1','r',encoding='utf-8') as f1,open('db2','w',encoding='utf-8') as f2:
# #
# #     for line in f1:
# #
# #         if times <=10:
# #             f2.write(line)
# #         else:
# #             break
