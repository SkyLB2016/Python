#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'动物类'

__author__ = '李彬'

from model.Animal import Animal


class Cat(Animal):

    # def __init__(self, name, gender, age):
    #     super(name, gender, age)

    def print_ani(self):
        print('动物名：%s，性别：%s，年龄：%d' % (self.name, self.gender, self.age))

    # def toString(self):
    #     return '物种：%s，性别：%s，年龄：%d' % (self.name, self.gender, self.age)
