#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json,pickle
name = 'ddd'
password = 'ccc'
a = 'register' + ' '+name+','+password
print (a)
action,message = a.split()
print (action)
print (message)
name,password = message.split(',')
print (name)
print (password)
