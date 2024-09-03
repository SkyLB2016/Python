#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'类'

__author__ = '李彬'

from flask_sqlalchemy.model import Model
from wtforms import IntegerField, StringField


class User(Model):
    id = IntegerField('id')
    name = StringField('name')


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


class Student(object):
    tag = 'Student'  # 设置tag
    count = 0

    # 两个__ 代表 私有属性。
    def __init__(self, name, gender, age, score):
        self.__name = name
        self.__gender = gender
        self.__age = age
        self.__score = score
        # Student.count += 2

    def print_stu(self):
        print('姓名：%s，性别：%s，年龄：%d，分数：%.2f' % (self.__name, self.__gender, self.__age, self.__score))

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        self.__gender = gender

    def __str__(self):
        return '重写__str__方法：姓名：%s，性别：%s，年龄：%d，分数：%.2f' % (
            self.__name, self.__gender, self.__age, self.__score)

    def __call__(self):
        return "以实例自身为方法"

    def stu_dict(self):
        return {
            'name': self.__name,
            'age': self.__age,
            'gender': self.__gender,
            'score': self.__score
        }

    def __iter__(self):
        return self

    def __next__(self):
        self.__age = self.__age + 1
        if self.__age > 1000:
            raise StopIteration()
        return self.__age

    @classmethod
    def cus(cls, field):
        pass


class Teacher(object):
    tag = 'teacher'  # 设置tag
    count = 0

    def __init__(self, name, gender, age, score):
        self.name = name
        self.gender = gender
        self.age = age
        self.score = score
        # Student.count += 2

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_gender(self):
        return self.gender

    def set_gender(self, gender):
        self.gender = gender

    def __str__(self):
        return '老师的姓名：%s，性别：%s，年龄：%d，分数：%.2f' % (self.name, self.gender, self.age, self.score)

    def __call__(self):
        return "以实例自身为方法"

    def stu_dict(self):
        return {
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
            'score': self.score
        }
