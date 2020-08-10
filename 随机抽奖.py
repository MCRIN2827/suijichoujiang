#!/usr/bin/python
# -*- coding: UTF-8 -*-
from random import randint
All = raw_input('请输入参与抽奖总人数:')
Num = raw_input('请输入需要抽奖个数:')
flag = True

while flag:
    if Num.isdigit() and All.isdigit():
        Ind1 = int(Num)
        Ind2 = int(All)
        flag = False
    else:
        print '输入错误'
        break
else:
    for i in range(Ind1):
        print randint(1,Ind2)