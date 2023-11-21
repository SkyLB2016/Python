#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Michael Liao'

import sys


def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello, world!')
    elif len(args) == 2:
        print('Hello, %s!与%s' % (args[1], args[0]))
    else:
        print('Too many arguments!')


if __name__ == '__main__':
    test()
