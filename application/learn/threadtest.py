


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
