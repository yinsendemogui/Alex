#!/usr/bin/python3.5.2
# -*- coding: utf-8 -*-
# Haproxy.cfg配置文件自动化部署程序
# 本程序可以在windows下运行
# python03_homework01
#__author__:The_thirteen_group_chensiqi

import os

BALANCING_dict = {'1':'roundrobin','2':'static-rr','3':'leastconn','4':'source','5':'ri','6':'rl-param'}   # 轮询算法字典
CONFIG_PATH = 'Haproxy.cfg'
TAG = True # while循环控制标志


#Nginx负载均衡群集优化模板写入模块
def Nginx_load_balancing_template() :
    '''
    生成Haproxy.cfg文件
    :return: 无
    '''

    text = '''
    请选择轮询算法模式：
    1，roundrobin
    2,static-rr
    3,leastconn
    4,source
    5,ri
    6,rl_param  '''

    print (text)

    while TAG:
        decide = input('请输入你的选择：')
        if decide in BALANCING_dict:
            polling = BALANCING_dict[decide]
            break
        else:
            print ('你的输入有误，请重新输入！')

    Haproxy_cfg = '''
    # this config needs haproxy-1.1.28 or haproxy-1.2.1

    global
            #log 127.0.0.1  local0
            #log 127.0.0.1  local1 notice
            log /dev/log    local0 info
            log /dev/log    local0 notice
            #log loghost    local0 info
            maxconn 10240
            #chroot /usr/share/haproxy
            uid 99
            gid 99
            daemon
            nbproc16
            pidfile /var/run/haproxy.pid
            #debug
            #quiet


    defaults

            log     global
            mode    http
            option  httplog
            option  dontlognull
            option  http-server-close
            timeout http-keep-alive 10000
            timeout http-request 10000
            retries 3
            #option redispatch
            maxconn 10240
            contimeout  5000
            clitimeout  50000
            srvtimeout  50000


    listen  web_nginx 0.0.0.0:80
            option httpchk GET /list.html
            balance {0} '''.format(polling)

    while TAG:
        try:
            f = open(CONFIG_PATH, 'x',encoding='utf-8')
            f.write(Haproxy_cfg)
        except:
            decide = input('配置文件已存在，是否进行备份操作（y/n）:')
            if decide == 'y':
                os.system('move'+' '+CONFIG_PATH+' '+CONFIG_PATH+'.bak')

            elif decide == 'n':
                os.system('move'+' '+CONFIG_PATH+' '+CONFIG_PATH+'.del')
            else:
                print ('您的输入有误，请重新输入！')
        else:
            print (CONFIG_PATH+'创建成功！')
            break


def Server_select():
    '''
    获取配置文件中的服务器的信息
    :return: 索引和server信息的映射字典
    '''
    dict = {}
    if os.path.exists(CONFIG_PATH) != True :
        print (CONFIG_PATH + '不存在，请生成后再来！')
        return
    Num = 0
    with open(CONFIG_PATH,'r',encoding='utf-8') as f:
        for line in f:
            if 'server' in line.strip().split():
                Num += 1
                print (str(Num)+' '+line.strip())
                dict[Num]=line.strip()
    return dict



def Server_add(Text):
    '''
    添加新的服务器
    :param Text:预添加的服务器的种类
    :return: 无
    '''

    if os.path.exists(CONFIG_PATH) != True :
        print (CONFIG_PATH + '不存在，请生成模板后再来！')
        return

    re_server = Server_Count('server',CONFIG_PATH)
    re_server_bak = Server_Count('nginx_bak',CONFIG_PATH)
    server_listen = re_server - re_server_bak
    text = '总共已经部署了{0}台服务器;\n其中nginx监听服务器{1}台;\n其中nginx备份服务器{2}台.'.format(re_server,server_listen,re_server_bak)
    print(text)

    if re_server_bak >= 1 and Text == '备份':
        print ('备份服务器已经有了，不能继续添加了！')
        return
    os.system('copy Haproxy.cfg Haproxy.cfg.bak')
    Num = server_listen + 1
    with open(CONFIG_PATH + '.bak', 'r', encoding='utf-8') as f1, open(CONFIG_PATH, 'w') as f2:
        for line in f1:
            if 'web_nginx' in line.strip().split():
                f2.write(line)
                while TAG:
                    try:
                        IP_address = input('请输入你想要{0}的服务器的IP地址（单条追加，信息为空停止追加）：'.format(Text))
                        re = Server_Count(IP_address+':80',CONFIG_PATH)
                        ree = Server_Count(IP_address+':80',CONFIG_PATH+'.bak')
                        if re > 0 or ree > 0:
                            print ('您输入的监听服务器地址重复，请重新输入')
                            continue
                        elif IP_address.strip() != '':
                            if Text == '监听':
                                f2.write(' '*12+'server nginx_{0} {1}:80 check inter 2000 rise 3 fall 3 weight 1\n'.format(Num,IP_address.strip()))
                                Num += 1
                            else:
                                f2.write(' '*12+'server nginx_bak {0}:80 check inter 2000 rise 3 fall 3 backup\n'.format(IP_address.strip()))
                                break
                            f2.flush()
                        else:
                            break
                    except:
                        print ('您输入的信息有误,请重新输入！')
                    else:
                        print('ip地址为{0}的待监听服务器追加成功！'.format(IP_address))
            else:
                f2.write(line)
                f2.flush()


def Server_update():
    '''
    修改服务器的信息
    :return: 无
    '''

    while TAG:
        dict = Server_select()
        decide = input('请输入你想修改的服务器前索引：（n=退出）')
        if int(decide) in dict:
            server_massage = input('请输入你想修改成的内容：')
            break
        elif decide == 'n':
            return
        else:
            print ('你输入的信息有误，请重新输入！')

    os.system('move'+' '+CONFIG_PATH+' '+CONFIG_PATH+'.bak')
    with open(CONFIG_PATH + '.bak','r') as f1,open(CONFIG_PATH,'w') as f2:
        for line in f1:
            if line.strip() == dict[int(decide)]:
                f2.write(' '*12+server_massage+'\n')
                print ('修改成功！')
            else:
                f2.write(line)



def Server_Count(text,path):
    '''
    计算配置文件中服务器的数量
    :param text: 计数的内容
    :param path: 配置文件路径
    :return: 数量
    '''
    num = 0
    with open(path,'r',encoding='utf-8') as f:
        for line in f:
            if text in line.strip().split():
                num += 1
        return num

# 主函数
def Main():
    '''
    用户功能界面
    :return:无
    '''

    text = '''
           系统功能清单
    1，生成优化后的haproxy.cfg模板
    2，获取监听服务器信息
    3，添加nginx—server监听服务器
    4，添加nginx-bak备份服务器
    5，修改server服务器信息
    6, 退出系统  '''
    while TAG:
        os.system('cls')
        print (text)
        while TAG:
            decide = input('请输入你的选择：')
            if decide in ['1','2','3','4','5','6','7']:
                if decide == '1':
                    Nginx_load_balancing_template()
                    break
                elif decide == '2':
                    Server_select()
                    break
                elif decide == '3':
                    Server_add('监听')
                    break
                elif decide == '4':
                    Server_add('备份')
                    break
                elif decide == '5':
                    Server_update()
                    break
                elif decide == '6':
                    exit()
            else:
                print ('你的输入有误，请重新输入！')





Main()




