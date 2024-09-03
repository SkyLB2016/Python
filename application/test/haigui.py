#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 导入turtle包的所有内容:
from turtle import *

# 设置笔刷宽度:
width(2)
#
# # 前进:
# forward(200)
# # 右转90度:
# right(90)
#
# # 笔刷颜色:
# pencolor('red')
# forward(100)
# right(90)
#
# pencolor('green')
# forward(200)
# right(90)
#
# pencolor('blue')
# forward(100)
# right(90)

speed(300)
pencolor('red')

goto(100, 0)
for i in range(75):
    left(80)
    fd(100)
    left(135)
    fd(120)

back(100)
pencolor('yellow')

for i in range(75):
    left(80)
    fd(100)
    left(135)
    fd(120)


back(100)
pencolor('green')
for i in range(75):
    left(80)
    fd(100)
    left(135)
    fd(120)

back(100)
pencolor('blue')
for i in range(75):
    left(80)
    fd(100)
    left(135)
    fd(120)
back(100)
pencolor('pink')
for i in range(75):
    left(80)
    fd(100)
    left(135)
    fd(120)

# back(100)
# pencolor('gray')
# for i in range(75):
#     left(80)
#     fd(100)
#     left(135)
#     fd(120)

# 调用done()使得窗口等待被关闭，否则将立刻关闭窗口:
done()
