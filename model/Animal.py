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
        return '重写__str__方法：物种：%s，性别：%s，年龄：%d' % (self.name, self.gender, self.age)

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_gender(self):
        return self.gender

    def set_gender(self, gender):
        self.gender = gender


class Cat(Animal):

    def __init__(self, name, gender, age, type="猫科"):
        super().__init__(name, gender, age)
        self.type = type

    def __str__(self):
        return '重写__str__方法：动物名：%s，性别：%s，年龄：%d；纲目：%s' % (self.name, self.gender, self.age, self.type)


class Dog(Animal):

    def __init__(self, name, gender, age, category="犬科"):
        super().__init__(name, gender, age)
        self.category = category

    def __str__(self):
        return '重写__str__方法：动物名：%s，性别：%s，年龄：%d，纲目：%s' % (self.name, self.gender, self.age, self.category)
