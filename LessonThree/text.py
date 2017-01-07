#!usr/bin/env python
# -*- coding:utf-8 -*-
# auther:Mr.chen
# 描述：

path = '/Users/chensiqi/Git/Alex/LessonFour/FTP_server/Folder/chensiqi/'

list = path.split('/')
del list[0]
del list[len(list) - 1]
del list[len(list) - 1]
str = '/'
for i in range(len(list)):
    str = str + list[i] + '/'
    print i
print list
print str
