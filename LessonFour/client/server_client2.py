#!usr/bin/env python
# -*- coding:utf-8 -*-
# auther:Mr.chen
# 描述：
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("localhost", 8888))
while True:

    message = raw_input("输入：")
    s.send(message)



    s.close()