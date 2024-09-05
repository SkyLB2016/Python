import datetime
import json
import os
import random
import secrets
import string
import time
import types
from collections.abc import Iterable
from functools import reduce, partial
# import functools
from io import StringIO, BytesIO

import numpy
import requests

from application import tools
from application.model import custom
from application.model.Chain import Chain
from application.model.Animal import Animal, Cat, Dog
import hashlib

from application.model.models import Teacher, Student, Person


def learn_method_01():
    print('01.python 的基本数据类型分为：数字（整数，浮点数）、字符串、布尔、列表、元组、集合、字典，还有个特殊值 None（空值）----')
    # name =input('please enter your name:')
    # 数字
    num = 123
    # 字符串
    str_val = "Hello, World!"
    # 布尔值
    bool_val = True
    # 列表
    list_val = [1, 2, 3, "four", "five"]
    # 元组
    tuple_val = (1, 2, 3, "four", "five")
    # 集合
    set_val = {1, 2, 3, "four", "five"}
    # 字典
    dict_val = {"one": 1, "two": 2, "three": 3}
    print("print的输出", str_val)
    print(f"num != str_val=={num != str_val}")

    print(f"科学计数法：1.23e6=={1.23e6}")
    print(f"科学计数法：1_000_000_000=={1_000_000_000}")
    print(f"科学计数法，十六进制：0xa1b2_c3d4=={0xa1b2_c3d4}")
    print('转义字符：\\ee\te')
    print(r'字符前加r 代表不需要转义\\ee\te')
    print(
        '''多行字符传串输出：line1 
        ...line2 
        ...line3'''
    )
    print('算数运算符------------------------------------------------')
    print('* 乘号，数字运算3*3==', 3 * 3)
    print('* 乘号，其他类型运算是重复执行几次==', "ABC" * 3)
    print('** 两个乘号是算幂，3的3次方：3**3 ==', 3 ** 3)
    print(f"单除号/，会得到浮点数：10 / 3：=={10 / 3}")
    print(f"双除号//，除数和被除数都为整数，会向下取整，得到整数：11 // 3=={11 // 3}")
    print(f"双除号//，除数和被除数都为整数，会向下取整，得到整数：-11 // 3=={-11 // 3}")
    print(f"双除号//，除数和被除数有一个整数，得到整值的浮点数：11.3 // 3=={11.3 // 3}")
    print(f"双除号//，除数和被除数有一个整数，得到整值的浮点数：11 // 3.0=={11 // 3.0}")


def learn_method_02():
    print('02.字符编码转换-------------------------------')
    print('字符 中 对应的编码==', ord('中'))
    print('字符 文 对应的编码==', ord('文'))
    print('数字 20013 对应的字符编码==', chr(20013))
    print('十六进制表示的字符：\\u4e2d\\u6587 == \u4e2d\u6587')
    print('encode()方法，字符串转bytes类型:ABC===', 'ABC'.encode('ascii'))
    print('encode()方法，字符串转bytes类型:中文===', '中文'.encode('utf-8'))
    print('decode()方法，bytes类型转字符串:b\'ABC\'===', b'ABC'.decode('ASCII'))
    print('decode()方法，bytes类型转字符串:b\'\\xe4\\xb8\\xad\\xe6\\x96\\x87\'===',
          b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
    print('decode()方法，bytes类型转字符串,错误忽略==', b'\xe4\xb8\xad\xe6\x96'.decode('utf-8', errors='ignore'))
    print('字符长度长度：宇宙洪荒==', len('宇宙洪荒'))
    print('字符串转bytes类型后，bytes类型长度==', len(b'ABC'))
    print('字符串转bytes类型，bytes类型长度==', len(b'\xe4\xb8\xad\xe6\x96\x87'))


def learn_method_03():
    print('03.字符串格式化，是字符串与变量的格式化拼接----------------------------------')
    str_val = '拼接的是字符串变量：world'
    money = 88.0
    money1 = 99
    print('字符串与变量拼接，%s，（字符）' % str_val)
    print('字符串与变量拼接，%s，（字符），花了%f元（数字）' % (str_val, money))
    print('字符串与变量拼接，%s，（字符），花了%d元（数字）' % (str_val, money1))
    print('字符串与变量拼接，%s，（字符），花了%s元（字符）' % (str_val, money))
    money2 = 4
    money3 = 5
    print('空位补零或空的操作：%d-%3d' % (money2, money3))
    print('空位补零或空的操作：%1d-%03d' % (money2, money3))
    print('空位补零或空的操作：%2d-%02d' % (money2, money3))
    print('空位补零或空的操作：%3d-%03d' % (money2, money3))
    PI = 3.141592654
    print('取两位小数：%.2f' % PI)
    print('取整同时空位补两个零%03d' % PI)
    print('取整同时空位补两个空%3d' % PI)
    print('百分号转义是两个百分号代表一个百分号7%%==: %d %%' % 7)
    print('format()格式化：{0}，花了{1:.2f}%'.format('小明', 12.256))
    print('format()格式化：%s，花了 %.2f %%' % ('小明', 12.256))
    print(f'f-string格式化展示：有{money2}个圆，圆周率是{PI}，圆周率曲两位小数是{PI:.2f}')


def learn_method_04():
    print('04.list与tuple----------------------------------')
    print('list是python 内置的一种列表数据类型，有序集合，可随时添加、删除，各个元素可以是不同类型----------------')
    names = ['刘一', '陈二', '张三', '李四', '王五', '赵六']

    # ['孙七','周八','吴九', '郑十']
    print(f"输出 names 的元素=={names}")
    names.append('刘七')
    print(f"添加元素：names.append('刘七')，并输出 names 的元素=={names}")
    print(f"访问元素：names[1]=={names[1]}")
    print(f"访问元素，最后一个：names[-1]=={names[-1]}")
    print(f"访问元素，倒数第二个：names[-2]=={names[-2]}")
    names.insert(1, '郑十')
    print(f"输出 names.insert(1,'郑十') 新添加的元素  ==  {names[1]}")
    # names.pop()# 末位删除
    # names.pop(1)# 指定删除
    print(f"输出 names.pop() 删除的元素  ==  {names.pop()}")
    print(f"输出 names.pop(1) 指定删除的元素  ==  {names.pop(1)}")

    # 用大扩号定义的 list 是set集合，添加用add(),移除用remove(),和用中括号定义的list 不一样。
    # print('用大扩号定义的list是set集合，添加用add(),移除用remove(),和用 中括号定义的list 不一样，而且输出是乱序的。----------------')
    # names = {'刘一', '陈二', '张三', '李四', '王五', '赵六'}  # 与[] 定义的list是不一样的。
    # print(f"输出 names 的元素=={names}")
    # names.append(4)
    # names.add("孙七")
    # names.remove("赵六")
    # print(f"访问元素，最后一个：names[-1]=={names}")

    print('用小扩号定义的list，叫tuple，有序列表，初始化后不可变。----------------')
    names_tuple = ('刘一', '陈二', '张三', '李四', '王五', '赵六')
    print(f"输出 names_tuple 的元素=={names_tuple}")
    print(f"输出 names_tuple[1] 的元素=={names_tuple[1]}")
    print(f"输出 names_tuple[-1] 的元素=={names_tuple[-1]}")
    names_tuple = ('定义一个元素的tuple',)
    print(f"输出 names_tuple 的元素=={names_tuple}")
    names_tuple = ('定义一个元素的tuple', [])
    names_tuple[1].append("刘一")
    names_tuple[1].append("陈二")
    print(f"输出 names_tuple 的元素=={names_tuple}")


def learn_method_05():
    print('05.dict 等同于 map，用大括号定义，内部是 key:value 的形式-------------------------------')
    dict_map = {'username': "刘一", 'phone': 18531022252, 'addresses': "北京市"}
    # key-value 形式直接添加
    print(f'字典dict的类=={dict_map.__class__}')
    print(f'字典dict的类=={type(dict_map)}')
    print(f'dict_map["username"]={dict_map["username"]}')
    dict_map['city'] = '北京'
    # print(dict_map["address"]) # key 不存在会报错
    print(f"判断dict_map中是否存在key==={'username' in dict_map}")
    user = 'username'
    print(f"key不存在，返回None=={dict_map.get(user)}")
    print(f"key不存在，返回指定的value=={dict_map.get('add', 'default')}")
    print(f"删除对应的key=={dict_map.pop('addresses')}")


def learn_method_06():
    print('06.set集合，是无序的，不重复的，可以直接用大括号定义----------------------------------')
    names = ['刘一', '陈二', '张三', '李四', '王五', '赵六']
    set_1 = set(names)
    # set_1 = set(['刘一', '陈二', '张三', '李四', '王五', '赵六'])
    print(f"set集合=={set_1}")

    set_1 = {'刘一', '陈二', '张三', '李四', '王五', '赵六', '刘一', '陈二', '张三', '李四', '王五', '赵六'}
    print(f"set集合=={set_1}")
    for x in set_1:
        print(x)
    set_1.add("孙七")
    print(f"set集合=={set_1}")
    s1 = {1, 2, 3}
    s2 = {2, 3, 4}
    print(f"取交集s1&s2=={s1 & s2}")
    print(f"取并集s1|s2=={s1 | s2}")

    # s2 = set((1, 2, 3), (2, 3, 4))  # 会报错
    # print(s2)
    # s2= {1, [2, 3]}
    # for x in s2:
    #     print(x)


def learn_method_07():
    print('07.数据类型转换-------------------------------')
    text = '5678'
    print(f'转成 int 类型=={int(text)}')
    print(f'转成 float 类型=={float(text)}')
    print(f'转成 str 类型=={str(text)}')
    print(f'转成 bool 类型=={bool(text)}')
    print(f'十进制 转成 十六进制=={hex(int(text))}')
    a = abs  # 为 abs 起一个别名，感觉多此一举啊
    print(f'方法别名：为 abs 起一个别名a，感觉多此一举啊a(-1)=={a(-1)}')


def learn_method_08():
    print('08.多个返回值测试--------------------------------------------')
    return 1, 3, 4, 56, 7


def learn_method_09():
    print(f'参数对应类型验证=={isinstance(9, (int, float))}')
    print(f'参数对应类型验证=={isinstance(9.0, (int, float))}')
    print(f'参数对应类型验证=={isinstance("9.09.0", (int, float))}')
    print(f'参数对应类型验证=={isinstance("9.09.0", str)}')


def learn_method_10():
    print('10.函数定义，默认参数，可变参数---------------------')
    print('1）位置参数(固定参数)：按顺序依次输入的参数，必须要传值。')
    print('2）默认参数：位置参数设置了默认值，就是默认参数，默认参数也是固定参数，也是按顺序复制')
    print('3）可变参数： *args 接收的是一个 tuple 类型')
    print(f"可变参数custom_field(1, 3, 5, 7)=={custom.custom_field(1, 3, 5, 7)}")
    tr = (1, 3, 5, 7)
    print(f"可变参数custom_field(*tr)=={custom.custom_field(*tr)}")
    print('4）关键字参数 **kw-------------------------------------------')
    custom.person('张三', 33)
    custom.person('张三', 33, gender='man', city='北京', year=2023)
    kw = {'city': '北京', 'job': '开发'}
    custom.person('张三', 33, gender='man', **kw)

    print('5）命名关键字参数 *-------------------------------------------')
    custom.person1('张三', 33, city='北京')
    custom.person1('张三', 33, city='北京', job=2023)
    print('5）可变参数+命名关键字参数 *args，city，job-------------------------------------------')
    custom.person2('张三', 33, 12, 3, 4, city='北京', job=2023)
    print('5）可变参数+命名关键字参数 *args，city，job-------------------------------------------')
    custom.person3('张三', 33, job=2023)

    print('默认参数后边跟着可变参数，如果默认参数没有赋值，会自动摘取可变参数 tuple 中的数据按顺序补位')
    custom.f1("张三", 111, 1, 3, 5, 7, 8, city='北京', job='开发')
    custom.f1("李四", 111, *tr, **kw)
    custom.f2("王五", 111, email=1, qq=1, city='北京', job='开发')
    custom.f2("赵六", 111, email=1, qq=1, **kw)


# 递归调用
def ride(n):
    return ride_iter(n, 1)


def ride_iter(num, result):
    if num == 1:
        return result
    return ride_iter(num - 1, num * result)


def learn_method_11():
    print('去除字符串中空字符的几种方法---------------')
    text = '    天地玄黄，  宇宙洪荒;   '
    print(f'去除字符串中开头和结尾处的空字符与换行：text.strip()==开头：{text.strip()}：结尾')
    print(f'去除字符串中开头的空字符与换行：text.lstrip()==开头：{text.lstrip()}：结尾')
    print(f'去除字符串中结尾的空字符与换行：text.rstrip()==开头：{text.rstrip()}：结尾')
    print(f'去除字符串中所有的空字符与换行：text.replace(" ", "")==开头：{text.replace(" ", "")}：结尾')

    print(f'text.rsplit()==开头：{text.rsplit()}：结尾')
    print(f'text.split()==开头：{text.split()}：结尾')
    print(f'text.split(" ")==开头：{text.split(" ")}：结尾')


# 递归函数，尾部调用
def learn_method_12():
    print('12.递归函数-------------------------------------------')
    print(f'输出1到10的乘积=={ride(10)}')
    print(f'输出1到10的乘积=={ride_iter(10, 1)}')
    print(f'输出1到10的乘积=={1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10}')


def learn_method_13():
    print('13.切片操作符，属于半开半闭区间-------------------------------------------')
    # nums = [0, 1, 2, 3, 4, 5, 6, 7]
    nums = 'ABCDEFGH'
    print('输出全部 nums == ', nums)
    print('输出全部 nums，并且是两次 == ', nums * 2)
    print('输出全部 nums[:] == ', nums[:])
    print('输出全部 nums[0:8] == ', nums[0:8])
    print('输出3到6的元素 nums[2:6] == ', nums[2:6])
    print('输出最后两个元素 nums[6:]， == ', nums[6:])
    print('输出最后两个元素 nums[-2:]， == ', nums[-2:])
    print('输出 nums[-5:-2] == ', nums[-5:-2])
    print('输出 nums[-5:] == ', nums[-5:])
    print('输出 nums[-7:-4] == ', nums[-7:-4])
    print('倒序输出 nums[::-1] == ', nums[::-1])

    nums = list(range(100))  # 一百以内的list(0-99)
    print(f'type == {type(nums)}')
    print('输出[60:70] == ', nums[60:70])
    print('输出[60:70:2]，间隔1个的数，每次递增2 == ', nums[60:70:2])
    print('输出[61:70:2] == ', nums[61:70:2])
    print('输出[61:70:5] 每次递增5，== ', nums[61:70:5])
    print('从0开始的，每次递增5 nums[::5] == ', nums[::5])
    print("倒序输出，递减5 == ", nums[::-5])  # 倒序输出


def learn_method_14():
    print('14.循环，迭代，Iterable---------------------------------------------------------------')
    nums = list(range(100))  # 一百以内的list(0-99)
    print(isinstance(nums, Iterable))
    text = 'ABCDEFGH'
    print(isinstance(text, Iterable))
    print(isinstance(123, Iterable))
    dict_map = {'username': "刘一", 'phone': 18531022252, 'addresses': "北京市"}
    for k, v in dict_map.items():
        print('dict_map迭代key=', k, 'v=', v)
    for i, v in enumerate(text):
        print('字符串迭代，索引=', i, '元素=', v)
    for x, y in [(10, 1), (27, 4), (3, 79)]:
        print('二元数组迭代，x=', x, 'y=', y)


def learn_method_15():
    print('15.列表生成式，以中括号[]为准，繁琐的一比---------------------------------------------')
    print('01.生成1-8的2次方的list==', [x * x for x in range(1, 9)])
    print('02.生成1-8中偶数2次方的list==', [x * x for x in range(1, 9) if x % 2 == 0])
    print('03.生成1-8中奇数2次方的list==', [x * x for x in range(1, 9) if x % 2 == 1])
    print('04.生成 123 和 abc 数字和字母组成的list==', [a + b for a in '123' for b in 'abc'])
    print('05.生成1-3与 1 到 5，各数相加组成的list==', [(a + b) for a in range(1, 4) for b in range(1, 6)])
    print('06.生成当前目录下的文件和文件夹组成的list==', [d for d in os.listdir('learn')])
    print('06,小括号，会转成 generator，是个需要迭代的对象', (d for d in os.listdir('learn')))
    dict_map = {'username': "刘一", 'phone': "18531022252", 'addresses': "北京市"}
    print('07.生成字典dict的kv组成的list==', [k + '=' + v for k, v in dict_map.items()])
    print('08.生成1-8中奇数为负，偶数为正，组成的list==', [x if x % 2 == 0 else -x for x in range(1, 9)])
    print('09.生成1-8中奇数为负，偶数为正，同时乘以原数组成的list==',
          [x * (x if x % 2 == 0 else -x) for x in range(1, 9)])
    print('10.生成1-8中奇数为负，偶数为正，2次方，组成的list==',
          [(x if x % 2 == 0 else -x) * (x if x % 2 == 0 else -x) for x in range(1, 9)])


def learn_method_16():
    print('16.列表生成器 generator，以小括号 ()为准-----------------------------')
    print('列表生成式是直接生成集合列表，容量确定。生成器是生成一个对象，一边循环 ，一边计算生成下一个使用元素')
    gene = ((x if x % 2 == 0 else -x) * (x if x % 2 == 0 else -x) for x in range(1, 9))
    print('列表生成器 ', gene)
    print('取值的方法', next(gene))
    print('取值的方法  ', gene.__next__())
    print('斐波那契数列输出，加入yield 后，返回的就是一个generator 对象------------')
    gene = fib(7)
    n = 1
    for x in gene:
        print('斐波那契数列第', n, '个', x)
        n = n + 1
    print('捕捉生成器 return的返回')
    gene = fib(7)
    n = 0
    while True:
        try:
            n += 1
            print('斐波那契数列第', n, '个', next(gene))
        except StopIteration as e:
            print('捕捉 生成器 fib 函数返回值，StopIteration,==', e.value)
            break

    n = 0
    gene = triangles()
    print(gene)
    for g in gene:
        if n > 8:
            break
        n = n + 1
        print('杨辉三角第', n, '列', g)
    print('06', (d for d in os.listdir('learn')))


def fib(num):
    n, a, b = 0, 0, 1
    while n < num:
        yield b
        n = n + 1
        a, b = b, a + b
    return '完成后返回的值，需要捕捉 StopIteration '


def triangles():
    n, l = 0, [1]
    # while n < max:
    while True:
        yield l
        if len(l) == 1:
            l = [1, 1]
        else:
            ll = []
            for i in range(len(l) + 1):
                if i == 0 or i == len(l):
                    ll.append(l[i - 1])
                else:
                    ll.append(l[i - 1] + l[i])
            l = ll
            # n = n + 1


def learn_method_17():
    print('17.MD5加密第一种------------------------------')
    password = '123456'
    print(password)
    md = hashlib.md5(password.encode())  # 创建md5对象
    md5pwd = md.hexdigest()  # md5加密
    print(md5pwd)

    print('MD5加密第一种，再次加密')
    md = hashlib.md5(md5pwd.encode())  # 创建md5对象
    md5pwd = md.hexdigest()  # md5加密
    print(md5pwd)
    print('MD5加密第一种------------------------------')

    print('MD5加密第二种------------------------------')
    password = '123456'
    print(password)
    SALE = password[:4]  # 设置盐值
    print(str(password) + SALE)
    md_sale = hashlib.md5((password + SALE).encode())  # MD5加盐加密方法一：将盐拼接在原密码后
    md5salepwd = md_sale.hexdigest()
    print(md5salepwd)
    print('MD5加密第二种------------------------------')

    print('MD5加密第三种------------------------------')
    password = '123456'
    print(password)
    SALE = password[:4]  # 设置盐值
    print(str(password).join(SALE))
    md_sale = hashlib.md5((str(password).join(SALE)).encode())  # MD5加盐加密方法二：将password整体插入SALE的每个元素之间
    md5salepwd = md_sale.hexdigest()
    print(md5salepwd)
    print('MD5加密第三种------------------------------')


def add(x):
    return x + x


def add1(x, y):
    return x + y


def filt(x):
    return x % 2 == 1


def learn_method_18():
    print('18.map()，reduce()，filter()，sorted()方法的使用---------------------------------------------')
    nums = [9, 3, 8, 3, 1]
    m = map(str, nums)
    print(f'map()生成一个 iterator 惰性序列=={type(m)}')
    print(f'把 map 转成一个字符串 list=={list(m)}')
    print('map()只接收一个参数的方法==', list(map(add, nums)))
    print('reduce()方法，接收两个参数的方法', reduce(add1, nums))
    print('map()字符串转编码集，并生成list,1234==', list(map(ord, '1234')))
    print('map()字符串转编码集，并生成list,ABCD==', list(map(ord, 'ABCD')))
    print('map()字符串转数字编码，并生成list,abcd==', list(map(ord, 'abcd')))
    print(f'filter()条件筛选，筛选出奇数，并组成list=={list(filter(filt, nums))}')
    print(f'filter()条件筛选，筛选出奇数，并组成list=={next(filter(filt, nums))}')
    print('sorted()排序方法，默认排序==', sorted(nums))
    text = 'abcd'
    print(f'把 abcd 转成大写的=={next(map(str.upper, text))}')
    print(f'把 abcd 转成大写的=={list(map(str.upper, text))}')
    text2 = list(map(str, text)) + list(map(str.upper, text))
    print(f'两个list相加=={text2}')
    print('字符串默认编码排序', sorted(text2))
    print('字符串默认编码排序, key=str', sorted(text2, key=str))
    print('不区分大小写排序,key=str.lower', sorted(text2, key=str.lower))
    print('不区分大小写排序,key=str.upper', sorted(text2, key=str.upper))
    print(list(map(ord, '0123456789')))


def learn_method_19():
    # 闭包，延迟计算
    print('19.闭包的使用，函数作为返回值---------------------------------------------------------------------')
    s1 = lazy_sum(1, 2, 3, 4, 5, 6, 7, 8, 9)
    s2 = lazy_sum(1, 2, 3, 4, 5, 6, 7, 8, 9)
    print('闭包s1==，返回的是函数类型', s1)
    print('闭包s1()=，返回的是数值', s1())
    print('闭包s1=s2为', s1 == s2)


# 闭包函数的写法
def lazy_sum(*args):
    def sum():
        s = 0
        for x in args:
            s = s + x
        return s

    return sum


def learn_method_20():
    print('20.匿名函数应用,lambda 表示匿名函数，函数的简化-------------------------------------------------')
    print('匿名函数应用==', list(map(lambda x: x * x, [1, 2, 3, 4, 5])))
    print('匿名函数应用==', type(lambda x: x * x))

    print('int() 方法默认是十进制转十进制，base等于8时，是8进制转十进制-------------------------------------------------')
    print('默认是十进制转成十进制：255 ==', int('255'))
    print('16进制转成十进制：255 == ', int('255', 16))
    print('16进制转成十进制：ff == ', int('ff', 16))
    print('二进制转成十进制：1111 == ', int('1111', base=2))
    print('八进制转成十进制：20 == ', int('20', 8))

    # 偏函数
    print('偏函数应用，functools.partial 定义的函数-------------------------------------------------')
    print('定义一个二进制转十进制的偏函数：int2=functools.partial(int, base=2)')
    int2 = partial(int, base=2)
    print(f'偏函数int2的类型=={type(int2)}')
    print('二进制转十进制：int2(1111) =', int2('1111'))
    print(max(11, 12, 45))
    max2 = partial(max, 99)
    print(f'偏函数max2的类型=={type(max2)}')
    print(max2(11, 12, 45))


def learn_method_21():
    print("21.decorator 装饰器模式，近似于java的注解，但java的注解使用的是反射，而 python 使用的是方法嵌套 ---------")
    print('1.无参数的且接收一个参数装饰器', factorial(10), '完')
    print('2.无参数的但接收多个参数装饰器', factorial2(1, 10), '完')
    print('3.有参数的且接收多个参数装饰器', factorial3(10, 100), '完')


def log(func):
    def wrappers(x):
        print('\n1.开始')
        print(f'执行的方法是：{func.__name__} ()；参数是x={x}')
        return func(x)

    return wrappers


@log
def factorial(n):
    print(f"计算1-{n}的阶乘")
    return reduce(lambda x, y: x * y, range(1, n + 1))


def log2(func):
    def wrappers(*args, **kw):
        print('\n2.开始')
        time1 = time.time_ns()
        r = func(*args, **kw)
        time2 = time.time_ns()
        print(f'执行方法{func.__name__}时间花费是=={int(time2 - time1)}纳秒')
        return r

    return wrappers


@log2
def factorial2(a, b):
    print(f"计算{a}-{b}的和")
    return reduce(lambda x, y: x + y, range(a, b + 1))


def log3(desc):
    def wrappers(func):
        def wrapper(*args, **kw):
            print('\n3.开始')
            time1 = time.time_ns()
            r = func(*args, **kw)
            time2 = time.time_ns()
            print(f'decorator（装饰器）自定义的参数{desc}执行方法{func.__name__}的时间是=={int(time2 - time1)}纳秒')
            return r

        return wrapper

    return wrappers


@log3('这是装饰器的参数')
def factorial3(a, b):
    print(f"计算{a}-{b}的和")
    return reduce(lambda x, y: x + y, range(a, b + 1))


def learn_method_22():
    print('22.自定义类，属性-------------------------------------------------')
    tea = Teacher('张三', '男', 33, 88)
    print(tea.__str__())
    tea.set_name("李四")
    print(tea.__str__())
    print(tea())
    stu = Student('王五', '男', 33, 88)
    print(stu.__str__())
    stu.set_name("赵六")
    print(stu.__str__())
    # 集成与多态
    print('继承与多态-----------------------------------------------------------------')
    cat = Cat('猫', '雄', 4)
    dog = Dog('狗', '雄', 4)
    ani = Animal('动物', '雄', 4)
    print(ani.__str__())
    print(cat.__str__())
    print(dog.__str__())
    print(dog.__repr__())
    print('猫是动物', isinstance(cat, Animal))
    print('动物是猫，但类不是猫', isinstance(ani, Cat))
    list1 = [2]
    print("list1是集合", isinstance(list1, list))


def learn_method_23():
    # type()应用
    print('23.type()，dir(),hasattr,getattr,setattr 方法使用，获取类型-------------------------------------------------')
    print("数字 123 的类型是 ==", type(123))
    print("字符串 123 的类型是 ==", type('123'))
    print("空类型 None 的类型是 ==", type(None))
    print("函数 abs 的类型是 ==", type(abs))
    print("type(abs) == types.BuiltinFunctionType === ", type(abs) == types.BuiltinFunctionType)
    cat = Cat('猫', '雄', 4)
    print("cat.tostring 的类型==", type(cat.__str__()))
    print("type(cat.__str__()) == types.MethodType", type(cat.__str__()) == types.MethodType)
    print("匿名函数  lambda x:x 的类型是", type(lambda x: x))
    print("type(lambda x: x) == types.LambdaType===", type(lambda x: x) == types.LambdaType)
    print("x for x in range(9)) 的类型是===", type((x for x in range(9))))
    print("type((x for x in range(9))) == types.GeneratorType==", type((x for x in range(9))) == types.GeneratorType)
    # dir方法
    print('dir方法使用，获取一个对象的所有属性和方法-----------------------------------------------------------------')
    print('dir方法', type(dir(cat)))
    print('dir方法', dir(cat))
    tea = Teacher('张三', '男', 33, 88)
    print('是否有name属性', hasattr(tea, 'name'))
    print('是否有name属性', hasattr(tea, '__name'))
    print('获取name属性的值', getattr(tea, 'name'))
    print('给stu设置name的属性，并赋值', setattr(tea, 'name', "张三"))
    print('获取name属性的值', getattr(tea, 'name'))
    print('给stu设置name1的属性，并赋值', setattr(tea, 'name1', "李四"))
    print('获取name1属性的值', getattr(tea, 'name1'))


def learn_method_24():
    print('24.MethodType动态绑定方法-------------------------------------------------------')
    teacher = Teacher('张三', '男', 33, 88)
    teacher.get_age = types.MethodType(get_age, teacher)
    teacher.set_age = types.MethodType(set_age, teacher)
    teacher.set_age(67)
    print(teacher.age)
    print(teacher.get_age())


def set_age(self, age):
    self.age = age


def get_age(self):
    return self.age


def learn_method_25():
    print(
        '25.自定义类__slots__绑定属性，绑定之后，这各类只能有这几个属性，不能在定义其他属性---------------------------------')
    per = Person('张三', 93)
    print(per.name)
    try:
        per.gender = '男'  # 已经限定死了属性，再次定义会报错
    except AttributeError as e:
        print(f"已经限定死了属性，再次定义会报错=={e}")
    per.score = 33
    print('获取 @property 属性定义', per.score)


def learn_method_26():
    print('26.__xxx__ 特殊属性的使用---------------------------------------------------')
    stu = Student('张三', '男', 33, 88)
    per = Person('张三', 93)
    print('重写类的 str 方法==', str(stu))
    print('不重写类的 str 方法==', str(per))
    print("重写 str 后可直接调用stu==", stu)
    print("不重写 str 后直接调用per==", per)
    print('repr==', repr(stu))
    print(Chain().status.user.timeline.list)
    print('重写 call 方法后，可调用自身 stu()==', stu())
    print('callable 判断是否重写了call方法==', callable(Student))
    print('callable 判断是否重写了call方法==', callable(stu))
    n = 9
    assert n != 0
    print('callable 判断是否重写了call方法==', callable(per))
    # for age in Student('张三', '男', 33, 88):
    #     print(age)


def learn_method_27():
    print('27.文件读写-------------------------------------------------------')
    path = './static/text.txt'
    f = open(path)
    print(f"f=={f}")
    print('读取一行：f.readline()===', f.readline())
    print('读取多行：f.readline()===', f.readlines())
    print(f"读取全部：f.read()=={f.read()}")
    f.close()
    print('第二遍读取，需要重新打开，with结束后，会自动关闭文件---------------------------------------------------')
    with open(path, 'r') as f:
        for line in f.readlines():
            print(line.strip())  # strip去除开头末尾的空字符
            # print(line[::-1])  # 倒序输出

    print('第三遍读取，追加内容-------------------------------------------------------')
    text = "天地玄黄，宇宙洪荒"
    with open(path, 'a') as f:
        f.write(text)


def learn_method_28():
    print('28.StringIO操作-------------------------------------------------------')
    str1 = StringIO()
    str1.write('拼接的')
    print(str1.getvalue())
    str1.write('字符串')
    print(str1.getvalue())


def learn_method_29():
    print('29.BytesIO操作-------------------------------------------------------')
    by1 = BytesIO()
    print(f"by1.write('拼接的'.encode('utf-8'))==={by1.write('拼接的'.encode('utf-8'))}")
    print(f"by1.__str__()=={by1.__str__()}")
    print(f"by1.getvalue()=={by1.getvalue()}")
    print(by1.write('字符串'.encode('utf-8')))
    print(f"by1.getvalue()=={by1.getvalue()}")
    print(f"by1.getvalue().decode('utf-8')=={by1.getvalue().decode('utf-8')}")


def learn_method_30():
    print('30.OS系统操作-------------------------------------------------------')
    print('os.name==', os.name)
    print('os.path==', os.path)
    print('os.uname()系统详情==', os.uname())
    print('os.environ，环境变量==', os.environ)
    print('os.environ.get(\'PATH\')==', os.environ.get('PATH'))
    print("程序执行的根目录绝对路径==", os.path.abspath('learn'))
    print("当前执行代码所在文件的绝对路径==", os.path.abspath(__file__))
    # print('创建目录==', os.path.join('.', 'testdir'))
    # print(os.mkdir('./testdir'))
    print('输出当前目录的所有文件和文件夹  ==', [d for d in os.listdir('learn')])
    gene = (d for d in os.listdir('learn'))
    print('中括号变成小括号，会转成 generator，是个对象===', gene)
    print('中括号变成小括号，会转成 generator，是个对象===', gene.__next__())
    print('输出当前文件夹', [d for d in os.listdir('learn') if os.path.isdir(d)])
    print('输出.py结尾的文件', [d for d in os.listdir('learn') if os.path.isfile(d) and os.path.splitext(d)[1] == '.py'])
    print('输出.txt结尾的文件', [d for d in os.listdir('static/images') if
                                 os.path.isfile('static/images/' + str(d)) and os.path.splitext(d)[1] == '.png'])
    for d in os.listdir('learn'):  # 获取当前目录下的文件和文件夹
        if os.path.isfile(d):  # 是否是文件
            print(f"文件名=={d}；转化的数组=={os.path.splitext(d)}")  # 文件名数组化


def learn_method_31():
    print("方法测试------------------------------------------------")
    # print('Process (%s) start...' % os.getpid())
    # print(f"3的3次方：math.pow(3,3)=={math.pow(3, 3)}")
    # print(f"π：pi:math.pi=={math.pi}")
    # print(f"sys.path=={sys.path}")
    learn_method_32()


def learn_method_32():
    text_set = set()  # set无序不重复集合
    text_ll = []  # list有序集合
    text_repeat = []  # 重复集合
    # lines = []
    count = 0  # 字数
    count_total = 0  # 字与符号的总数

    with open('./static/text.txt') as f:
        lines = f.readlines()
        for line in lines:
            count_total += len(line)
            line = line.replace("　", "") \
                .replace("，", "") \
                .replace("。", "") \
                .replace("；", "") \
                .replace("！", "") \
                .replace("、", "") \
                .replace("？", "") \
                .replace("：", "") \
                .replace("“", "") \
                .replace("”", "") \
                .replace("‘", "") \
                .replace("’", "") \
                .replace("【", "") \
                .replace("】", "") \
                .replace("[ ", "") \
                .replace("]", "") \
                .replace("\n", "") \
                .replace(" ", "") \
                .replace("~", "") \
                .replace("·", "") \
                .replace("（", "") \
                .replace("）", "") \
                .replace("0", "") \
                .replace("1", "") \
                .replace("2", "") \
                .replace("3", "") \
                .replace("4", "") \
                .replace("5", "") \
                .replace("6", "") \
                .replace("7", "") \
                .replace("8", "") \
                .replace("9", "") \
                .replace("》", "") \
                .replace("《", "")

            count += len(line)
            # print(line)

            for i in line:
                if i not in text_ll:  # 判断是否已添加
                    text_ll.append(i)
                else:
                    text_repeat.append(i)

                text_set.add(i)  # 加入到无序不重复集合
    print(f'有{len(lines)}行')
    print(f'一共有{count_total}个字与符号')
    print(f'一共有{count}字')
    print(f'有{count_total - count}符号')
    print(f'有{len(text_ll)}个不重复的字')
    print(text_ll)
    print(f'有{len(text_repeat)}个重复的字')
    # print(text_repeat)
    print(f'有{len(text_set)}个不重复的字')
    print(text_set)
    # print(f'判断是否为中文=={jieba.lcut("天地玄黄，宇宙洪荒")}')
    print('16进制3000对应的十进制是==', int("3000", base=16))
    print(f'数字 12288 对应的字符编码==start{chr(12288)}end')
    print('十六进制表示的字符：\\u3000 == start\u3000end')


def learn_method_33():
    print('18.random 随机数方法的使用---------------------------------------------')
    names = ['刘一', '陈二', '张三', '李四', '王五', '赵六']
    stus = []
    print(f"0-1之间的小数 == {random.random()}")
    print(f"1-100之间的小数 == {random.random() * 100 + 1}")
    print(f'1-100之间的整数 == {random.randint(1, 100)}')
    print(f"随机文本 == {random.choice(['男', '女', '男', '女', '男', '女', '男', '女'])}")

    print(f"numpy模块的1-100之间的整数 == {numpy.random.randint(1, 100)}")
    print(f"numpy模块的随机文本 == {numpy.random.choice(['男', '女', '男', '女', '男', '女', '男', '女'])}")

    for name in names:
        stus.append((name, random.choice(['男', '女', '男', '女', '男', '女', '男', '女']), random.randint(1, 100),
                     random.randint(1, 100)))
    print('原始排序 == ', stus)
    print('sorted()排序方法，默认排序 == ', sorted(stus))


def learn_method_34():
    print("前两天的日期获取------------------------------------------------")
    now = datetime.datetime.now()
    delta = datetime.timedelta(days=2)
    print(f'now=={now}')
    print(f'delta=={delta}')
    prev_day = now - delta
    prev_day_str = prev_day.strftime('%Y-%m-%d')
    start_ctime = prev_day_str + " 00:00:00"
    end_ctime = prev_day_str + " 23:59:59"
    print(f'prev_day=={prev_day}')
    print(f'prev_day_str=={prev_day_str}')
    print(f'start_ctime=={start_ctime}')
    print(f'end_ctime=={end_ctime}')
    # 获取当前日期
    today = datetime.datetime.today()
    # 获取前两天的日期
    two_days_ago = today - datetime.timedelta(days=2)
    #
    print("前两天的日期是:", two_days_ago)
    print("时间戳:", time.time_ns())
    print("时间戳:", time.time())
    print("时间戳:", datetime.datetime.now().timestamp())
    print("时间戳:", datetime.datetime.now())
    pass


# 文本倒序输出
def learn_method_35():
    texts = []
    text = ''
    with open('./static/text.txt') as f:
        lines = f.readlines()
        for line in lines:
            # if line.startswith("第"):
            if "、" in line:
                print(text)
                texts.append(text)
                text = ''
            text += line
        print(text)
        texts.append(text)  # 添加最后一章

    with open('./static/text2.txt', "w") as f:
        for text in reversed(texts):  # 倒序
            f.write(text)
    print(f'{texts}')


# 比较文本中的重复诗词
def learn_method_36():
    texts_112 = []
    with open('./static/text112.txt') as f:
        lines = f.readlines()
        for line in lines:
            if "、" in line:
                start = line.index("、")
                end = line.index(" ")
                text = line[start + 1:end]
                texts_112.append(text)
    texts_155 = []
    with open('./static/text75+80.txt') as f:
        lines = f.readlines()
        for line in lines:
            if "、" in line:
                start = line.index("、")
                end = line.index(" ")
                text = line[start + 1:end]
                texts_155.append(text)
    text_equal = []
    text_equal_not = []
    text = ''
    with open('./static/text150.txt') as f:
        lines = f.readlines()
        for line in lines:
            if "、" in line:  # 此行是否有特定标识，有的话，处理之前收集的文本：text
                add_text(text, text_equal, text_equal_not, texts_112, texts_155)
                text = ''  # 处理完成后，重置文本：text
            text += line  # 收集文本
        # 循环结束后，对比最后一次收集的文本
        add_text(text, text_equal, text_equal_not, texts_112, texts_155)

    print(f"相同的诗有{len(text_equal)}首：{text_equal}")
    print(f"不相同的诗有{len(text_equal_not)}首：{text_equal_not}")
    # 生成相同诗词的文件
    with open('./static/text_equal.txt', "w") as f:
        for text in text_equal:
            f.write(text)
    # 生成不相同诗词的文件
    with open('./static/text_equal_not.txt', "w") as f:
        for text in text_equal_not:
            f.write(text)


# text              对比的文本
# text_equal        不相同文本组成的数组
# text_equal_not    不相同文本组成的数组
# texts_112         对比的文本数组
# texts_155         对比的文本数组
def add_text(text, text_equal, text_equal_not, texts_112, texts_155):
    if not text:
        return
    try:
        # 根据特定的规则截取出当前文本需要对比的名称
        start = text.index("、")
        end = text.index(" ")
        name = text[start + 1:end]
        if name in texts_112 or name in texts_155:
            text_equal.append(text)
        else:
            text_equal_not.append(text)
    except Exception as e:
        print(f"{text}")
        print(f"错误=={e}")


# 下载文件
def download():
    url = 'https://my.linlongyun.com/api/signassistant/static/excel/2024-01-22/c0890d9d4e86212e1374249af4e4a01c_import_error.xlsx'  # 你要下载的文件的URL
    file_name = 'static.txt'  # 你想要保存的文件名

    response = requests.get(url, stream=True)
    response.raise_for_status()  # 如果请求返回的状态码不是200，则会抛出HTTPError异常

    with open(file_name, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):  # 使用块大小为8KB读取响应内容
            if chunk:  # 如果块大小大于0
                f.write(chunk)


# 十六进制计算
def hex_cal():
    print(f'十进制 转成 十六进制=={hex(12)}')
    a = 0x790
    b = 0x79A
    c = 0x7d0
    d = 0x7da
    print(f'十进制 转成 十六进制=={a}')
    print(f"{hex(a)}")
    for i in range(0, 20):
        a = a + 10
        print(hex(a))
        a = a + 54
        print(hex(a))
def generate_random_string(length=12):
    characters = string.ascii_letters + string.digits + '!@#$%&*'
    # print(f"characters == {characters}")
    random_string = ''.join(secrets.choice(characters) for _ in range(length))
    print(f"random_string == {random_string}")
    return random_string


def md5(password):
    h = hashlib.md5()
    h.update(password.encode("utf8"))
    password = h.hexdigest()
    print(f"password == {password}")

def max_subarray_sum(nums):
    current_sum = max_sum = nums[0]
    start = end = start_temp = 0
    for i in range(1, len(nums)):
        if current_sum >= 0:
            current_sum += nums[i]
        else:
            current_sum = nums[i]
            start_temp = i

        if current_sum > max_sum:
            max_sum = current_sum
            start, end = start_temp, i
    return nums[start:end + 1], max_sum


def max_subarray_sum1(nums):
    current_sum = max_sum = nums[0]
    start = end = s = 0
    for i in range(1, len(nums)):
        if current_sum < 0:
            current_sum = nums[i]
            s = i
        else:
            current_sum += nums[i]
        if current_sum > max_sum:
            max_sum = current_sum
            start, end = s, i
    return nums[start:end + 1], max_sum


def max_array():
    #  从一个整数数列中如何找到和最大的连续子串
    # nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    nums = [1, 2, -2, 3, -3, -1, 4, -1, 2, 1, -5, 4]
    # nums = [-10, 1, 2, 3, 4, -1, 2, -5, -23, 2, 7, -21]
    # nums = [3, -2, 7, -1, 4]
    subarray, max_sum = max_subarray_sum(nums)
    print("子数组:", subarray)
    print("最大和:", max_sum)
    subarray, max_sum = max_subarray_sum1(nums)
    print("子数组:", subarray)
    print("最大和:", max_sum)


def learn_method_test():
    # print('python的数据类型分为：整数，浮点数，字符串，布尔值，还有个特殊值 None（空值）---------------------------------------')
    # learn_method_01()
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
    pass


def learn_method():
    print("方法测试------------------------------------------------")
    learn_method_test()
    # max_array()
