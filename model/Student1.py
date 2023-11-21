#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'学生类'

__author__ = '李彬'


class Student1(object):
    tag = 'Student1'  # 设置tag
    count = 0

    def __init__(self, name, gender, age, score):
        self.name = name
        self.gender = gender
        self.age = age
        self.score = score
        # Student.count += 2

    def print_stu(self):
        print('姓名：%s，性别：%s，年龄：%d，分数：%.2f' % (self.name, self.gender, self.age, self.score))

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_gender(self):
        return self.gender

    def set_gender(self, gender):
        self.gender = gender

    def __str__(self):
        return '姓名：%s，性别：%s，年龄：%d，分数：%.2f' % (self.name, self.gender, self.age, self.score)

    def __call__(self):
        return "以实例自身为方法"

    def stu_dict(self):
        return {
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
            'score': self.score
        }
