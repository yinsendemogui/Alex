#!usr/bin/env python
# -*- coding:utf-8 -*-
# auther:Mr.chen
# 描述：

from lib.Players_model import players_Model
import os
from lib import common
from src.Story_start import Lock_demon_tower
DIR = os.path.abspath(__file__)
DIR = DIR.replace('text.py', 'db/')

# p = players_Model('chensiqi','32','china','sdfsd','sdfsdf',['锁妖塔一层','锁妖塔二层'])
# print (p.schedule)
# print (p.schedule.keys()[2])

dict = common.log_info_read(DIR + 'config_conf')
P = dict['players'][0]
Lock_demon_tower(P)
# dict['players'] = []
# common.log_info_write(DIR + 'config_conf', dict)