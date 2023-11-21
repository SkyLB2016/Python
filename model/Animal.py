#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'动物类'

__author__ = '李彬'


class Animal(object):

    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def print_ani(self):
        print('物种：%s，性别：%s，年龄：%d' % (self.name, self.gender, self.age))

    def __str__(self):
        return '重写__str__方法的返回：物种：%s，性别：%s，年龄：%d' % (self.name, self.gender, self.age)

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_gender(self):
        return self.gender

    def set_gender(self, gender):
        self.gender = gender
