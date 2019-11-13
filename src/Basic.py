#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 练习 Python 基本模块

import sys

# https://blog.csdn.net/The_Time_Runner/article/details/87722919
sys.stdout.write("【Helle Python %s】\n" % (sys.version))
print('Hello')

f = open('test.txt', 'a')
print('this is a test', file=f)  # 增量添加文件内容



list = ['Michael', 'Bob', 'Tracy']
print("【list长度】：", len(list))
print(list[0])
print(list[1])
print(list[2])
# print(list[3]) #IndexError: list index out of range

d = dict(Michael=95, Bob=75, Tracy=85)
print("【dict长度】：", len(d))
print('d[\'Michael\'] =', d['Michael'])
print('d[\'Bob\'] =', d['Bob'])
print('d[\'Tracy\'] =', d['Tracy'])
print('d.get(\'Thomas\', -1) =', d.get('Thomas', -1)) # 不存在就去默认值 -1

import datetime

print(datetime.datetime.now())  # 打印当前时间
# 来自 <https://www.zhihu.com/question/38857862>


