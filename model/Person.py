#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'类'

__author__ = '李彬'


class Person(object):
    __slots__ = ('name', 'age', '_score')

    def __init__(self, name='默认', age=0, address="默认地址"):
        self.name = name
        self.age = age
        print('姓名：%s，性别：%s，年龄：%s' % (self.name, self.age, address))

    @property
    def score(self):
        return self._score


    @score.setter
    def score(self, value):
        self._score = value
