#!usr/bin/env python
# -*- coding:utf-8 -*-
# auther:Mr.chen
# 描述：

import socket

s = socket.socket()
s.connect(('localhost',9999))

while True:
    cmd = raw_input("请输入指令>>:").strip()
    if len(cmd) == 0:
        continue
    s.send(cmd.encode("utf-8"))
    cmd_res_size= s.recv(1024)
    if cmd_res_size == 'Exit!':
        print ("服务器没有响应，也许您的输入有误！")
    else:
        s.send("Ready!")
        print("命令结果大小:{0}".format(cmd_res_size))
        received_size = 0
        received_data = ''
        while received_size < int(cmd_res_size):
            data = s.recv(1024)
            received_size += len(data)
            received_data += data
            print ("命令执行结果如下：")
            print (received_size)
        else:
            print  ("cmd res receive done...",received_size)
            print (received_data)
s.close()




    # cmd_res = s.recv(1024)
    # print (cmd_res)

