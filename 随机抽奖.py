#!/usr/bin/python
# -*- coding: UTF-8 -*-
from random import randint
All_People = raw_input('请输入参与抽奖总人数:')
Luckydogs = raw_input('请输入需要抽奖个数:')
flag = True

while flag:
    if Luckydogs.isdigit() and All_People.isdigit():
        Num_Luckydogs = int(Luckydogs)
        Num_All_People = int(All_People)
        flag = False
    else:
        print '输入错误'
        break
else:
    for i in range( Num_Luckydogs):
        print randint(1,Num_All_People)    #呵呵