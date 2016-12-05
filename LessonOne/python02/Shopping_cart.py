#!/usr/bin/python
# -*- coding: utf-8 -*-
# 模拟电子商城购物系统
# 网上银行只添加了充值功能（本想真模拟网银，但没有太好的构思，文件读写并未练熟）
# 考虑到缓存占用，读取文件使用迭代读取方式，但写的有些吃力
# 本程序只能运行在Linux环境下
# python02_homework01
# __author__:The_thirteen_group_chensiqi

import os,time,linecache

shopping_path='/root/shopping.conf' #程序配置文件路径
sorce = {'chensiqi':'666666','chensiqi1':'666666','chensiqi2':'666666','chensiqi3':'666666'} #账号密码字典
error = [] #账号锁定列表
GoodsA = {} #商品价格字典
GoodsB = {} #商品名称字典
goods = None #
List = [] #购物车列表
ListHistory = [] #购物历史数据列表
Values = 0    #商品总价
salary = 0    #用户余额
Tag = True    #while循环控制标志

# 用户交互接口
def MainInterface () :
	while Tag :
		os.system('clear')
		choose = 0
		print '\n\n\n\n\n'
		print '\033[31;5m {0}\033[0m'.format(title.center(100))
		print '\033[34;5m {0}\033[0m'.format(title2.rjust(85))
		print '\n\n\n'
		print '\033[32;1m************************\033[0m'.rjust(68)
		print '\033[32;1m*     1,购物           *\033[0m'.rjust(70)
		print '\033[32;1m*     2,查看购物车     *\033[0m'.rjust(73)
		print '\033[32;1m*     3,结账退出       *\033[0m'.rjust(72)
		print '\033[32;1m*     4,网上银行       *\033[0m'.rjust(72)
		print '\033[32;1m*     5,直接退出       *\033[0m'.rjust(72)
		print '\033[32;1m************************\033[0m'.rjust(68)
		while Tag :
			choose = raw_input('请问，您想做些什么？(单选) :')
			if len(choose) == 1 :
				if choose.isdigit() :
					if '1' in choose :
						shopping()
						break
					elif '2' in choose :
						shoppingcart()
						break
					elif '3' in choose :
						exitsystem()
						break
					elif '4' in choose :
						E_bank()
						break
					elif '5' in choose :
						Exit()
						break
					else :
						print '\033[31;1m 别闹-_-!没有 {0} 这个选项！\033[0m'.format(choose).rjust(50)
				else :
					print '\033[31;1m 请输入纯数字，谢谢！\033[0m'.rjust(50)
			else :
				print '\033[31;1m 请进行单项选择! \033[0m'.rjust(50)

# 购物功能模块
def shopping () :
	global goods
	os.system('clear')
	print '\n\n\n\n\n'
	print '\033[31;5m {0}\033[0m'.format(title.center(100))
	print '\033[34;5m {0}\033[0m'.format(title2.rjust(85))
	print '\n\n\n'
	print '\033[32;1m***********************************\033[0m'.rjust(75)
	print '\033[32;1m*       1,手机       4800         *\033[0m'.rjust(77)
	print '\033[32;1m*       2,电视       2000         *\033[0m'.rjust(77)
	print '\033[32;1m*       3,冰箱       1000         *\033[0m'.rjust(77)
	print '\033[32;1m*       4,手表       500          *\033[0m'.rjust(77)
	print '\033[32;1m*       5,衣服       200          *\033[0m'.rjust(77)
	print '\033[32;1m*       6,帽子       100          *\033[0m'.rjust(77)
	print '\033[32;1m***********************************\033[0m'.rjust(75)
	while Tag :
		goods = raw_input('请问您打算买点什么？(可以多选复选): ')
		if goods.isdigit() :
			if set(goods) & set(GoodsA) == set(goods) :
				if len(goods) == len(set(goods)) :
					costkeeping()
				else :
					while Tag :
						decide = raw_input('\033[31;1m 您的选择里有重复内容，\033[0m是否继续购买多件？(y/n):')
						if decide == 'y' :
							costkeeping()
							break
						elif decide == 'n' :
							break
						else :
							print '\033[31;1m 您输入的数据有误请重新输入！ \033[0m'.rjust(50)
			else :
				print '\033[31;1m 请在1-6之间进行选择，谢谢！ \033[0m'.rjust(50)
		else :
			print '\033[31;1m 请输入纯数字进行选择，谢谢！ \033[0m'.rjust(50)
			
			
	
	
	
	
	
# 购物车功能模块
def shoppingcart() :
	while Tag :
		os.system('clear')
		global salary
		global Values
		global List
		Values = 0
		tab = 0
		for i in List :
			Values = Values + GoodsA[i]
	 
		print "\n\n\n\n\n"
		print '\033[31;5m {0}\033[0m'.format(title.center(100))
		print '\033[34;5m {0}\033[0m'.format(title2.rjust(85))
		print '\n\n\n'
		print '\033[32;1m|————————购物车——————|\033[0m'.rjust(99)
		num = 1
		for i in List :
			if int(i) <= 3 :
				print '\033[32;1m|  {0}   {1}   {2}   |\033[0m'.format(num,GoodsB[i],GoodsA[i]).rjust(70)
				num += 1
			else :
				print '\033[32;1m|  {0}   {1}   {2}    |\033[0m'.format(num,GoodsB[i],GoodsA[i]).rjust(70)
				num += 1
		print '\033[32;1m|————————————————————|\033[0m'.rjust(108)
		print '\033[31;1m    合计:    {0}    \033[0m'.format(Values).rjust(70)
		print '您的资金余额为\033[31;1m{0}\033[0m元'.format(salary)
		print '购物车总计消费为\033[32;1m{0}\033[0m元'.format(Values)
		if salary >= Values :
			name = '消费后剩余金额为\033[31;1m{0}\033[0m元,动态评估：\033[31;1m收支平衡\033[0m'.format(salary-Values)
		else :
			name = '消费后剩余金额为\033[31;7m{0}\033[0m元,动态评估：\033[31;1m余额不足！\033[0m'.format(salary-Values)
		print name
		while Tag :
			decide =  raw_input('是否继续删除购物车内商品？(y继续|n返回|clear清空): ')
			if decide == 'y' :
				if List != [] :
					while Tag :
						choose = raw_input('请输入你想删除的物品索引(单选)：')
						if choose.isdigit() :
							if 0 < int(choose) < num :
								del List[int(choose)-1]
								tab = 1
								break
							else :
								print '\033[31;1m 请输入正确的索引，谢谢！ \033[0m'.rjust(50)
						else :
							print '\033[31;1m 请输入纯数字进行选择，谢谢！ \033[0m'.rjust(50)
				else :
					print '\033[31;1m 购物车里没有东西，请返回购物后再来\033[0m'.rjust(50)
					time.sleep(2)
					return
			elif decide == 'n' :
				return
			elif decide == 'clear' :
				List = []
				break
			else :
				print '\033[31;1m 您输入的数据有误请重新输入！ \033[0m'.rjust(50)
			if tab == 1 :
				break

# 结账退出功能模块
def exitsystem() :
	global List
	global ListHistory
	os.system('clear')
	global salary
	global Values
	Values = 0

	for i in List :
		Values = Values + GoodsA[i]
	 
	print "\n\n\n\n\n"
	print '\033[31;5m {0}\033[0m'.format(title.center(100))
	print '\033[34;5m {0}\033[0m'.format(title2.rjust(85))
	print '\n\n\n'
	print '\033[32;1m|————————账单———————|\033[0m'.rjust(100)
	for i in List :
		if int(i) <= 3 :
			print '\033[32;1m|    {0}    {1}   |\033[0m'.format(GoodsB[i],GoodsA[i]).rjust(70)
		else :
			print '\033[32;1m|    {0}    {1}    |\033[0m'.format(GoodsB[i],GoodsA[i]).rjust(70)
	print '\033[32;1m|———————————————————|\033[0m'.rjust(106)
	print '\033[31;1m    合计:    {0}    \033[0m'.format(Values).rjust(70)
	if salary >= Values :
		while Tag :
			decide = raw_input('您的余额为{0}元，是否结账并退出系统？y/n: '.format(salary))
			if decide == 'y' :
				salary = salary -Values
				ListHistory = ListHistory + List
				List = []
				writeconfig()
				
				Exit()
			elif decide == 'n' :
				return
			else :
				print '\033[31;1m 您输入的数据有误请重新输入！ \033[0m'.rjust(50)
	else :
		while Tag :
			decide = raw_input('您的余额还剩\033[31;1m{0}\033[0m，不足以支付账单，是否前去购物车修改？y/n:'.format(salary))
			if decide == 'y' :
				shoppingcart()
				break
			elif decide == 'n' :
				return
			else :
				print '\033[31;1m 您输入的数据有误请重新输入！ \033[0m'.rjust(50)



				
# 只能充值的网上银行功能模块	
def E_bank() :
	global salary
	os.system('clear')
	print '\n\n\n\n\n'
	print '\033[31;5m {0}\033[0m'.format(title.center(100))
	print '\033[34;5m {0}\033[0m'.format(title2.rjust(85))
	print '\n\n\n'
	while Tag :
		decide = raw_input('您的余额为{0}元，是否继续充值？y/n: '.format(salary))
		if decide == 'y' :
			while Tag :
				try :
					salary = salary + int(raw_input('请输入你想充值的金额：'))
					break
				except :
					print '请输入正确的金额！'
		elif decide == 'n' :
			return
		else :
			print '请不要乱输入数据，谢谢！'
	

# 配置文件写入模块
def writeconfig() :
	global salary
	text1 = '[商品列表]\n'
	text2 = '[购物车列表]\n'
	text3 = '[购物历史信息]\n'
	text4 = '[账户余额]\n'
	text5 = '[]\n'
	text6 = '[]\n'
	f = file(shopping_path,'wb')
	if GoodsA == {} and GoodsB == {} and List == [] :
		f.write(text1)
		f.write('手机 4800\n')
		f.write('电视 2000\n')
		f.write('冰箱 1000\n')
		f.write('手表 500\n')
		f.write('衣服 200\n')
		f.write('帽子 100\n')
		f.write(text2)
		f.write(text3)
		f.write(text4)
		f.write(str(salary)+'\n')
		f.write(text5)
		f.write(text6)
	else :
		f.write(text1)
		for i in xrange(len(GoodsA)) :
			f.write(GoodsB[str(i+1)] + ' ' + str(GoodsA[str(i+1)]) + '\n')
		f.write(text2)
		for i in xrange(len(List)) :
			f.write(List[i] + '\n')
		f.write(text3)
		for i in xrange(len(ListHistory)) :
			f.write(ListHistory[i] + '\n')
		f.write(text4)
		f.write(str(salary)+'\n')
		f.write(text5)
		f.write(text6)
	f.close()
# 配置文件读取模块
def readconfig() :
	global salary
	text1 = '[商品列表]'
	text2 = '[购物车列表]'
	text3 = '[购物历史信息]'
	text4 = '[账户余额]'
	text5 = '[]'
	text6 = '[]'

	f = file(shopping_path,'rb')
	num = 1
	for line in f.xreadlines() :
		if line.strip() == text1 :
			i = num + 1
			while Tag :
				dline = linecache.getline(shopping_path,i)
				if '[' and ']' in dline or dline == '' :
					break
				elif dline.strip() == '' :
					i += 1
				else :
					GoodsA[str(len(GoodsA)+1)] = int(dline.strip().split()[1])
					GoodsB[str(len(GoodsB)+1)] = dline.strip().split()[0]
					i += 1
		elif line.strip() == text2 :
			i = num + 1
			while Tag :
				dline = linecache.getline(shopping_path,i)
				if '[' and ']' in dline or dline == '' :
					break
				elif dline.strip() == '' :
					i += 1
				else :
					List.append(dline.strip())
					i += 1
		elif line.strip() == text3 :
			i = num + 1
			while Tag :
				dline = linecache.getline(shopping_path,i)
				if '[' and ']' in dline or dline == '' :
					break
				elif dline.strip() == '' :
					i += 1
				else :
					ListHistory.append(dline.strip())
					i += 1
		elif line.strip() == text4 :
			i = num + 1 
			dline = linecache.getline(shopping_path,i)
			salary = int(dline.strip())
		elif line.strip() == text5 :
			pass
		elif line.strip() == text6 :
			pass
		num += 1
	f.close()

	
# 成本核算分支模块
def costkeeping() :
	global List
	global goods
	global salary
	global Values
	Values = 0
	values = 0
	for i in List+list(goods) :
		Values = Values + GoodsA[i]
	if len(List) != 0 :
		for i in List :
			values = values + GoodsA[i] 
	if salary < Values :
		print '您的余额还有\033[31;1m{0}\033[0m元，商品总价为\033[32;1m{1}元(含购物车{2}元)\033[0m '.format(salary,Values,values)
		while Tag :
			decide = raw_input('\033[31;7m您的余额已经不足！\033[0m是否取消本次选择？y/n: ')
			if decide == 'y' :
				return
			elif decide == 'n' :
				List = List +list(goods)
				MainInterface()
			else :
				print '\033[31;1m 您输入的数据有误请重新输入！ \033[0m'.rjust(50)
	else :
		print '您的余额还有\033[32;1m{0}\033[0m元，商品总价为\033[32;1m{1}元(含购物车{2}元)\033[0m: '.format(salary,Values,values)
		while Tag :
			decide = raw_input('是否将本次选择添加到购物车？y/n: ')
			if decide == 'y' :
				List = List +list(goods)
				MainInterface()
			elif decide == 'n' :
				return
			else :
				print '\033[31;1m 您输入的数据有误请重新输入！ \033[0m'.rjust(50)

# 直接退出系统
def Exit() :
	i = 5
	while i > 0 :
		print '\033[30;5m您的\033[0m\033[33;5m余额\033[0m\033[32;5m还剩下\033[0m\033[31;5m{0}元，\033[0m\033[34;5m欢迎再次\033[0m\033[35;5m光临！\033[0m\033[36;5m{1}秒后系统\033[0m\033[31;5m自动退出\033[0m'.format(salary,i).rjust(20)
		i -= 1
		time.sleep(1)
	writeconfig()
	exit()
		
#购物历史记录
def History() :
	global ListHistory
	i = 0
	if ListHistory != [] :
		print '历史购物信息如下：'
		for i in xrange(len(GoodsA.keys())+1) :
			if str(i) in ListHistory :				
				print '您历史上一共购买了{0}物品，{1}个'.format(GoodsB[str(i)],ListHistory.count(str(i)))
				time.sleep(1)
		else :
			time.sleep(3)
	else:
		return
			
# 用户信息验证		
def LoginInterface() :
	global error
	global sorce
	while Tag:
		name = raw_input('请输入登录用户的用户名：')
		if name in error:
			print "用户已经被锁定，请尝试登录其他用户！"
		elif name in sorce :
			passwd = raw_input("请输入登录用户名的密码：")
			i = 0
			while Tag :
				if passwd == sorce[name] :
					print "欢迎你，登陆成功！"
					return
				elif i == 2 :
					print "您的密码已经连续输错3次，{0}账户已经被锁定！请尝试登录其他用户.".format(name)
					error.append(name)
					break
				else :
					passwd = raw_input("您的密码输入错误，请重新输入：")
					i += 1
		else :
			print "用户名输入有误，请重新输入！"

	

# Main主函数
os.system('clear')
LoginInterface()
os.system('clear')
print "\n\n\n\n\n"
title = "欢迎光临电子商城购物系统"
title2 = "—————chensiqi-2016-10-22"
print '\033[31;5m {0}\033[0m'.format(title.center(100))
print '\033[34;5m {0}\033[0m'.format(title2.rjust(85))


if os.path.exists(shopping_path) :
	print "\n\n\n\n\n"
	print '\033[31;1m 亲爱的朋友，您是老顾客了，欢迎您的再次光临！\033[0m'.center(120)
	time.sleep(3)
else :
	while Tag :
		print "\n\n\n\n\n"
		salary = raw_input('请输入你的工资: '.rjust(50))
		if salary.isdigit():
			salary = int(salary)
			writeconfig()
			break
		else :
			print '\033[31;1m 您输入的数据有误，请重新输入!\033[0m'.rjust(50)
		
readconfig()
History()	

MainInterface()



