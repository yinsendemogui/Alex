#!/usr/bin/python
# -*- coding: utf-8 -*-
# 练习

import json

class PersonInfo :
    def __init__(self,name,age):
        self.Name = name
        self.Age  = age

    def aaa(self):
        if hasattr(self,'bbb'):
            P = getattr(self,'bbb')
            print ("1")
            P()

            # print (getattr(self,'aaa'))

    def bbb(self):
        print ("2")


    def handle(self):
        # b = 'aa'
        # c = eval(b+'a')
        d = 'self.aa'
        eval(d+'a')()

P = PersonInfo("chensiqi","32")
P.handle()



