#!usr/bin/env python
# -*- coding:utf-8 -*-
# auther:Mr.chen
# 描述：



class aaa:
    def __init__(self,name):
        self.Name = name


class bbb(aaa):
    def __init__(self,age,name):
        aaa.__init__(self,name)
        self.Age = age

