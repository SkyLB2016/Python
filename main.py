#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from learn.learn01 import learn_method_10, learn_method_14, learn_method_11, learn_method_22, learn_method_31, \
    learn_method_20, learn_method_21

# 控制台输入操作
# s = input('birth: ')
# birth = int(s)
# if birth < 2000:
#     print('00前')
# else:
#     print('00后')

# print('python的数据类型分为：整数，浮点数，字符串，布尔值，还有个特殊值 None（空值）---------------------------------------')
# learn_method_01()￥
# print('字符编码转换-------------------------------')
# learn_method_02()
# print('字符串格式化，是字符串与变量的格式化拼接----------------------------------')
# learn_method_03()

# print('python 内置的数据列表类型：list 与 tuple----------------------------------')
# learn_method_04()

# print('python 的字典集合：distmap ----------------------------------')
# learn_method_05()

# print('set集合----------------------------------')
# learn_method_06()

# print('数据类型转换----------------------------------')
# learn_method_07()

# print('时间类型转换----------------------------------')
# time_format()

# print('函数多个返回值测试,其实返回的是一个tuple 类型，可以单个变量逐个接收，也可以接收整个tuple--------------')
# x, y, z, a, b = learn_method_08()
# print(x)
# print(y)
# print(z)
# print(a)
# b = learn_method_08()
# print(b)

# print(f'参数对应类型验证=={isinstance(9, (int, float))}')
# learn_method_09()
# print('函数定义，默认参数，可变参数，关键字参数，命名关键字参数，以及组合---------------------')
# learn_method_10()
# print('去除字符串中空字符的几种方法---------------')
# learn_method_11()
# print('递归函数-------------------------------------------')
# learn_method_12()
# print('切片操作符-------------------------------------------')
# learn_method_13()
# print('循环，迭代，Iterable---------------------------------------------------------------')
# learn_method_14()
# print('列表生成式，以中括号[]为准，繁琐的一比---------------------------------------------')
# learn_method_15()

# print('列表生成器 generator，以小括号 ()为准-----------------------------')
# learn_method_16()

# print('MD5加密------------------------------')
# learn_method_17()

# print('map，reduce，filter，sorted方法的使用---------------------------------------------')
# learn_method_18()

# print('闭包的使用---------------------------------------------------------------------')
# learn_method_19()

# print('匿名函数应用,lambda 表示匿名函数，函数的简化-------------------------------------------------')
# learn_method_20()

# print("装饰器模式-----------------------------------------")
# learn_method_21()

# print('自定义类，属性-------------------------------------------------')
# print('集成与多态-----------------------------------------------------------------')
# learn_method_22()

# print('type()，dir(),hasattr,getattr,setattr 方法使用，获取类型-----------------------------------------------------------------')
# learn_method_23()

# print('MethodType动态绑定方法-------------------------------------------------------')
# learn_method_24()

# print('自定义类__slots__绑定属性，绑定之后，这各类只能有这几个属性，不能在定义其他属性------------------------------------------------------------')
# learn_method_25()

# print('__xxx__ 特殊属性的使用---------------------------------------------------')
# learn_method_26()

# print('文件读写-------------------------------------------------------')
# learn_method_27()

# print('StringIO操作-------------------------------------------------------')
# learn_method_28()

# print('BytesIO操作-------------------------------------------------------')
# learn_method_29()

# print('OS系统操作-------------------------------------------------------')
# learn_method_30()


# print("json的loads与dumps方法应用")
# learn_json()

# learn_method_31()






# Only works on Unix/Linux/Mac:
# pid = os.fork()
# print(f"pid={pid}")
# if pid == 0:
#     print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))

# 子进程要执行的代码
# def run_proc(name):
#     print('Run child process %s (%s)...' % (name, os.getpid()))
#
#
# if __name__ == '__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Process(target=run_proc, args=('test',))
#     print('Child process will start.')
#     p.start()
#     p.join()
#     print('Child process end.')


import os
import random
import time


def long_time_task(name):
    print('任务名称== %s id==(%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('任务 %s 运行 %0.2f 秒.' % (name, (end - start)))

# if __name__ == '__main__':
#     print('主线程id== %s.' % os.getpid())
#     p = Pool(4)
#     for i in range(5):
#         p.apply_async(long_time_task, args=(i,))
#     # print('Waiting for all subprocesses done...')
#     print('等待所有进程执行完毕')
#     p.close()
#     p.join()
#     # print('All subprocesses done.')
#     print('所有进程执行完毕.')

# print('$ nslookup www.python.org')
# r = subprocess.call(['nslookup', 'www.python.org'])
# print('Exit code:', r)


# print('$ nslookup')
# p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# output, err = p.communicate(b'set q=mx\n'
#                             b'python.org\n'
#                             b'exit\n')
# print(output.decode('utf-8'))
# print('Exit code:', p.returncode)


# from multiprocessing import Process, Queue
# import os, time, random
#
# # 写数据进程执行的代码:
# def write(q):
#     print('Process to write: %s' % os.getpid())
#     for value in ['A', 'B', 'C']:
#         print('Put %s to queue...' % value)
#         q.put(value)
#         time.sleep(random.random())
#
# # 读数据进程执行的代码:
# def read(q):
#     print('Process to read: %s' % os.getpid())
#     while True:
#         value = q.get(True)
#         print('Get %s from queue.' % value)
#
# if __name__=='__main__':
#     # 父进程创建Queue，并传给各个子进程：
#     q = Queue()
#     pw = Process(target=write, args=(q,))
#     pr = Process(target=read, args=(q,))
#     # 启动子进程pw，写入:
#     pw.start()
#     # 启动子进程pr，读取:
#     pr.start()
#     # 等待pw结束:
#     pw.join()
#     # pr进程里是死循环，无法等待其结束，只能强行终止:
#     pr.terminate()


# 新线程执行的代码:
# def loop():
#     print('2.thread %s is running...' % threading.current_thread().name)
#     n = 0
#     while n < 5:
#         n += 1
#         print('thread %s >>> %s' % (threading.current_thread().name, n))
#         time.sleep(1)
#     print('3、thread %s ended.' % threading.current_thread().name)
#
#
# print('1、thread %s is running...' % threading.current_thread().name)
# t = threading.Thread(target=loop, name='LoopThread')
# t.start()
# # t.join()#插队，子线程执行完成后，才会执行主线程。
# print('4、thread %s ended.' % threading.current_thread().name)


# balance = 0
#
# lock = threading.Lock()
#
#
# def change_it(n):
#     global balance
#     balance = balance + n
#     balance = balance - n
#
#
# def run_thread(n):
#     for i in range(200000):
#         lock.acquire()
#         try:
#             change_it(n)
#         finally:
#             lock.release()
#
#
# thread01 = threading.Thread(target=run_thread, args=(3,))
# thread02 = threading.Thread(target=run_thread, args=(6,))
#
# thread01.start()
# thread02.start()
#
# thread01.join()
# thread02.join()
# print(balance)
#
# print(4 ^ 2)
# print(4 + 2)


# import threading, multiprocessing
#
#
# def loop():
#     x = 0
#     while True:
#         x = x ^ 1
#
#
# for i in range(multiprocessing.cpu_count()):
#     t = threading.Thread(target=loop)
#     t.start()
