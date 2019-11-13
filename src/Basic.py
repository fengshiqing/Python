#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 练习 Python 基本模块

import sys

# https://blog.csdn.net/The_Time_Runner/article/details/87722919
sys.stdout.write("【Helle Python %s】\n" % (sys.version))
print('Hello')

f = open('test.txt', 'a')
print('this is a test', file=f)  # 增量添加文件内容

nameList = ['Michael', 'Bob', 'Tracy']
print("【list长度】：", len(nameList))
print(nameList[0])
print(nameList[1])
print(nameList[2])
# print(list[3]) #IndexError: list index out of range

d = dict(Michael=95, Bob=75, Tracy=85)
print("【dict长度】：", len(d))
print('d[\'Michael\'] =', d['Michael'])
print('d[\'Bob\'] =', d['Bob'])
print('d[\'Tracy\'] =', d['Tracy'])
print('d.get(\'Thomas\', -1) =', d.get('Thomas', -1))  # 不存在就去默认值 -1

import datetime

print(datetime.datetime.now())  # 打印当前时间
# 来自 <https://www.zhihu.com/question/38857862>

print('hello', 'world')  # 打印两个字符串，逗号会输出一个空格

print(10/3)

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Bob'])

L = list(range(0, 100))
print(L)
