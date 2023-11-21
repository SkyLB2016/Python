#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'学生类'

__author__ = '李彬'


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
        return '重写了__str__方法的返回：姓名：%s，性别：%s，年龄：%d，分数：%.2f' % (
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
