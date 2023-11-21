import functools
import json
import logging
import os
import types
from collections.abc import Iterable
from functools import reduce
from io import StringIO, BytesIO

from model.Chain import Chain
from model.Animal import Animal
from model.Cat import Cat
from model.Person import Person
from model.Student import Student
from model.Student1 import Student1
from model.custom import Custom
import hashlib


def learn_method_01():
    print("learn_method_01")
    print('python的数据类型分为：整数，浮点数，字符串，布尔值，还有个特殊值 None（空值）-----------------------')
    # name =input('please enter your name:')
    name = "username"
    print("print的输出", name)

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
    print(f"单除号/，会得到浮点数：10 / 3：=={10 / 3}")
    print(f"双除号//，也叫地板除，除数和被除数都为整数，会向下取整，得到整数：11 // 3=={11 // 3}")
    print(f"双除号//，也叫地板除，除数和被除数有一个整数，会向下取整，得到整值的浮点数：11.3 // 3=={11.3 // 3}")
    print(f"双除号//，也叫地板除，除数和被除数有一个整数，会向下取整，得到整值的浮点数：11 // 3.0=={11 // 3.0}")


def learn_method_02():
    print("learn_method_02")
    print('字符编码转换-------------------------------')
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
    print("learn_method_03")
    print('字符串格式化，是字符串与变量的格式化拼接----------------------------------')
    name = '拼接的是字符串变量：world'
    money = 88.0
    money1 = 99
    print('字符串与变量拼接，%s，（字符）' % name)
    print('字符串与变量拼接，%s，（字符），花了%f元（数字）' % (name, money))
    print('字符串与变量拼接，%s，（字符），花了%d元（数字）' % (name, money1))
    print('字符串与变量拼接，%s，（字符），花了%s元（字符）' % (name, money))
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
    print("learn_method_04")
    print('list与tuple----------------------------------')
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

    # 用大扩号定义的 list，添加用add(),移除用remove(),和用中括号定义的list 不一样。
    # print('用大扩号定义的list，添加用add(),移除用remove(),和用 中括号定义的list 不一样，而且输出是乱序的。----------------')
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


def if_else(age):
    if age <= 10:
        print(f'<= 10 years old: {age}')
    elif age > 10 or age < 19:
        print('11~18 years old.')
    else:
        print('大于18 years old.')


def match_case(age):
    match age:
        case x if x < 10:
            print(f'匹配模式1：< 10 years old: {x}')
        case 10:
            print('匹配模式2：10 years old.')
        case 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18:
            print('匹配模式3：11~18 years old.')
        case 19:
            print('匹配模式4：19 years old.')
        case _:
            print('匹配模式：not sure.')


def match_case_01(ars):
    match ars:
        # 如果仅出现gcc，报错:
        case ['gcc']:
            print('匹配模式1：gcc: missing source file(s).')
        # 出现gcc，且至少指定了一个文件:
        case ['gcc', file1, *files]:
            print('匹配模式2：gcc compile: ' + file1 + ', ' + ', '.join(files))
        # 仅出现clean:
        case ['clean']:
            print('匹配模式3：clean')
        case _:
            print('匹配模式4：invalid command.')


def learn_method_05():
    print("learn_method_05")
    print('dict 等同于 map，用大括号定义，内部是 key:value 的形式-------------------------------')
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
    print("learn_method_06")
    print('set集合，是无序的，不重复的，可以直接用大括号定义----------------------------------')
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
    print("learn_method_07")
    print('数据类型转换-------------------------------')
    text = '5678'
    print(f'转成 int 类型=={int(text)}')
    print(f'转成 float 类型=={float(text)}')
    print(f'转成 str 类型=={str(text)}')
    print(f'转成 bool 类型=={bool(text)}')
    print(f'十进制 转成 十六进制=={hex(int(text))}')
    a = abs  # 为 abs 起一个别名，感觉多此一举啊
    print(f'方法别名：为 abs 起一个别名a，感觉多此一举啊a(-1)=={a(-1)}')


def learn_method_08():
    print("learn_method_08")
    print('多个返回值测试--------------------------------------------')
    return 1, 3, 4, 56, 7


def learn_method_09():
    print("learn_method_09")
    print(f'参数对应类型验证=={isinstance(9, (int, float))}')
    print(f'参数对应类型验证=={isinstance(9.0, (int, float))}')
    print(f'参数对应类型验证=={isinstance("9.09.0", (int, float))}')
    print(f'参数对应类型验证=={isinstance("9.09.0", str)}')


def calc1(*args):
    print(f'args=={args}')
    sum = 0
    for x in args:
        print(f'x=={x + x}')
        sum = sum + x * x
    return sum


def learn_method_10():
    print("learn_method_10")
    print('函数定义---------------------')
    print(calc1(1, 3, 5, 7))
    print('自定义可变参数-------------------------------------------')
    tr = (1, 3, 5, 7)
    print(calc1(*tr))
    print(calc1(*(1, 3, 5, 7)))


def learn_method_11():
    print("learn_method_11")
    print('自定义关键字参数，没看出有什么用-------------------------------------------')
    Custom.person('李彬', 33, gender='man', city='北京', year=2023)
    distAndMap = {'city': '北京', 'job': '开发'}
    Custom.person('李彬', 33, gender='man', **distAndMap)
    Custom.person1('李彬', 33, city='北京', job=2023)
    Custom.person2('李彬', 33, 12, 3, 4, city='北京', job=2023)
    Custom.person3('李彬', 33, job=2023)
    print('自定义可变参数与关键字参数共用-------------------------------------------')


def ride(n):
    return ride_iter(n, 1)


def ride_iter(num, result):
    if num == 1:
        return result
    return ride_iter(num - 1, num * result)


# 递归函数，尾部调用
def learn_method_12():
    print("learn_method_12")
    print('递归函数-------------------------------------------')
    print(f'输出1到10的乘积=={ride(10)}')
    print(f'输出1到10的乘积=={ride_iter(10, 1)}')
    print(f'输出1到10的乘积=={1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10}')


def learn_method_13():
    print("learn_method_13")
    print('切片操作符-------------------------------------------')
    numbers = [0, 1, 2, 3, 4, 5, 6, 7]
    print('输出numbers[3:7]==', numbers[3:7])
    print('输出numbers[-2:]，最后两个==', numbers[-2:])
    print('输出numbers[-5:-2]==', numbers[-5:-2])
    print('输出numbers[-5:]==', numbers[-5:])
    print('输出numbers[-7:-4]==', numbers[-7:-4])

    numbers = list(range(100))  # 一百以内的list(0-99)
    print(f'type=={type(numbers)}')
    print('输出numbers[60:70]==', numbers[60:70])
    print('输出numbers[60:70:2]，输出从位置60开始的，间隔1个的数==', numbers[60:70:2])
    print('输出numbers[61:70:2]==', numbers[61:70:2])

    print("输出从位置1开始的，间隔1个的数")
    print('输出numbers[1::2]==', numbers[1::2])
    print("输出全部")
    print('输出numbers==', numbers)
    print('输出numbers[:]==', numbers[:])

    text = 'ABCDEFGH'
    print('输出text[:]==', text[:])
    print('输出text[:3]==', text[:3])
    print('输出text==', text)


def learn_method_14():
    print("learn_method_14")
    print('循环，迭代，Iterable---------------------------------------------------------------')
    numbers = list(range(100))  # 一百以内的list(0-99)
    print(isinstance(numbers, Iterable))
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
    print("learn_method_15")
    print('列表生成式，以中括号[]为准，繁琐的一比---------------------------------------------')
    print('01.生成1-8的2次方的list==', [x * x for x in range(1, 9)])
    print('02.生成1-8中偶数2次方的list==', [x * x for x in range(1, 9) if x % 2 == 0])
    print('03.生成1-8中奇数2次方的list==', [x * x for x in range(1, 9) if x % 2 == 1])
    print('04.生成 123 和 abc 数字和字母组成的list==', [a + b for a in '123' for b in 'abc'])
    print('05.生成1-3与 1 到 5，各数相加组成的list==', [(a + b) for a in range(1, 4) for b in range(1, 6)])
    print('06.生成当前目录下的文件和文件夹组成的list==', [dir for dir in os.listdir('.')])
    print('06,小括号，会转成 generator，是个需要迭代的对象', (d for d in os.listdir('.')))
    dict_map = {'username': "刘一", 'phone': "18531022252", 'addresses': "北京市"}
    print('07.生成字典dict的kv组成的list==', [k + '=' + v for k, v in dict_map.items()])
    print('08.生成1-8中奇数为负，偶数为正，组成的list==', [x if x % 2 == 0 else -x for x in range(1, 9)])
    print('09.生成1-8中奇数为负，偶数为正，同时乘以原数组成的list==',
          [x * (x if x % 2 == 0 else -x) for x in range(1, 9)])
    print('10.生成1-8中奇数为负，偶数为正，2次方，组成的list==',
          [(x if x % 2 == 0 else -x) * (x if x % 2 == 0 else -x) for x in range(1, 9)])
    print('11.列表生成器 ', ((x if x % 2 == 0 else -x) * (x if x % 2 == 0 else -x) for x in range(1, 9)))


def learn_method_16():
    print("learn_method_16")
    print('列表生成器 generator，以小括号 ()为准-----------------------------')
    print('列表生成式是直接生成集合列表，容量确定。生成器是生成一个对象，一边循环 ，一边计算生成下一个使用元素')
    gene = ((x if x % 2 == 0 else -x) * (x if x % 2 == 0 else -x) for x in range(1, 9))
    print('11.列表生成器 ', gene)
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
    print('06', (d for d in os.listdir('.')))


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
    print("learn_method_17")
    print('MD5加密第一种------------------------------')
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


def ff(x):
    return x % 2 == 1


def learn_method_18():
    print("learn_method_18")
    print('map()，reduce()，filter()，sorted()方法的使用---------------------------------------------')
    nums = [9, 3, 8, 3, 1]
    m = map(str, nums)
    print(f'map()生成一个 iterator 惰性序列=={type(m)}')
    print(f'把 map 转成一个字符串 list=={list(m)}')
    print('map()只接收一个参数的方法==', list(map(add, nums)))
    print('reduce()方法，接收两个参数的方法', reduce(add1, nums))
    print('map()字符串转编码集，并生成list,1234==', list(map(ord, '1234')))
    print('map()字符串转编码集，并生成list,ABCD==', list(map(ord, 'ABCD')))
    print('map()字符串转数字编码，并生成list,abcd==', list(map(ord, 'abcd')))
    print(f'filter()条件筛选，筛选出奇数，并组成list=={list(filter(ff, nums))}')
    print(f'filter()条件筛选，筛选出奇数，并组成list=={next(filter(ff, nums))}')
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
    print("learn_method_19")
    print('闭包的使用，函数作为返回值---------------------------------------------------------------------')
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
    print("learn_method_20")
    # 匿名函数
    print('匿名函数应用,lambda 表示匿名函数，函数的简化-------------------------------------------------')
    print('匿名函数应用==', list(map(lambda x: x * x, [1, 2, 3, 4, 5])))
    print('匿名函数应用==', type(lambda x: x * x))

    # print('方法名==', count.__name__)
    # 偏函数
    print('偏函数应用，functools.partial 定义的函数-------------------------------------------------')
    print('int() 方法默认是十进制转十进制，base等于8时，是8进制转十进制')
    print('255 ==', int('255'))
    print('255 == 转成十进制', int('255', 16))
    print('ff == 转成十进制', int('ff', 16))
    print('1111 == 转成十进制', int('1111', base=2))
    print('20 == 转成十进制', int('20', 8))

    print('偏函数应用，functools.partial 定义的函数-------------------------------------------------')
    int2 = functools.partial(int, base=2)
    print(f'偏函数int2的类型=={type(int2)}')
    print('二进制转十进制=', int2('11111111'))
    print(max(11, 12, 45))
    max2 = functools.partial(max, 99)
    print(f'偏函数max2的类型=={type(max2)}')
    print(max2(11, 12, 45))


def learn_method_21():
    print("learn_method_21")
    print("装饰器模式有待研究，暂时不予考虑--------------------------")


def learn_method_22():
    print("learn_method_22")
    print('自定义类，属性-------------------------------------------------')
    stu = Student1('李彬', '男', 33, 88)
    stu.print_stu()
    print(stu.__str__())
    stu.set_name("旺旺")
    print(stu.__str__())
    stu = Student('李彬', '男', 33, 88)
    stu.print_stu()
    print(stu.__str__())
    stu.set_name("旺旺")
    print(stu.__str__())
    # 集成与多态
    print('集成与多态-----------------------------------------------------------------')
    cat = Cat('猫', '雄', 4)
    ani = Animal('猫', '雄', 4)
    print(cat.print_ani())
    print('猫是动物', isinstance(cat, Animal))
    print('动物是猫，但类不是猫', isinstance(ani, Cat))
    list1 = [2]
    print("list1是集合", isinstance(list1, list))


def learn_method_23():
    print("learn_method_23")
    # type()应用
    print('type()，dir(),hasattr,getattr,setattr 方法使用，获取类型-------------------------------------------------')
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
    stu = Student1('李彬', '男', 33, 88)
    print('是否有name属性', hasattr(stu, 'name'))
    print('是否有name属性', hasattr(stu, '__name'))
    print('获取name属性的值', getattr(stu, 'name'))
    print('给stu设置name的属性，并赋值', setattr(stu, 'name', "张三"))
    print('获取name属性的值', getattr(stu, 'name'))
    print('给stu设置name1的属性，并赋值', setattr(stu, 'name1', "李四"))
    print('获取name1属性的值', getattr(stu, 'name1'))


def learn_method_24():
    print("learn_method_24")
    print('MethodType动态绑定方法-------------------------------------------------------')
    stu = Student1('李彬', '男', 33, 88)
    stu.get_age = types.MethodType(get_age, stu)
    stu.set_age = types.MethodType(set_age, stu)
    stu.set_age(67)
    print(stu.age)
    print(stu.get_age())


def set_age(self, age):
    self.age = age


def get_age(self):
    return self.age


def learn_method_25():
    print("learn_method_25")
    print(
        '自定义类__slots__绑定属性，绑定之后，这各类只能有这几个属性，不能在定义其他属性------------------------------------------------------------')
    per = Person('李彬', 93)
    print(per.name)
    try:
        per.gender = '男'  # 已经限定死了属性，再次定义会报错
    except AttributeError as e:
        print(f"已经限定死了属性，再次定义会报错=={e}")
    per.score = 33
    print('获取 @property 属性定义', per.score)


def learn_method_26():
    print("learn_method_26")
    # 特殊属性
    print('__xxx__ 特殊属性的使用---------------------------------------------------')
    stu = Student('李彬', '男', 33, 88)
    per = Person('李彬', 93)
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
    # for age in Student('李彬', '男', 33, 88):
    #     print(age)


def learn_method_27():
    print("learn_method_27")
    print('文件读写-------------------------------------------------------')
    # n = 1
    # logging.info('n = %d' % n)
    path = './file/Python.txt'
    file1 = open(path)
    print(file1)
    print(file1.read())
    print('读完了，就没有了===', file1.readline())
    file1.close()
    print('第二遍读取-------------------------------------------------------')
    with open(path, 'r') as f:
        for line in f.readlines():
            print(line.strip())  # strip去除末尾的'\n'

    print('第三遍读取，插入内容-------------------------------------------------------')
    text = "天地玄黄，宇宙洪荒"
    with open(path, 'a') as f:
        f.write(text)


def learn_method_28():
    print("learn_method_28")
    print('StringIO操作-------------------------------------------------------')
    str1 = StringIO()
    str1.write('拼接的')
    print(str1.getvalue())
    str1.write('字符串')
    print(str1.getvalue())


def learn_method_29():
    print("learn_method_29")
    print('BytesIO操作-------------------------------------------------------')
    by1 = BytesIO()
    print(f"by1.write('拼接的'.encode('utf-8'))==={by1.write('拼接的'.encode('utf-8'))}")
    print(f"by1.__str__()=={by1.__str__()}")
    print(f"by1.getvalue()=={by1.getvalue()}")
    print(by1.write('字符串'.encode('utf-8')))
    print(f"by1.getvalue()=={by1.getvalue()}")
    print(f"by1.getvalue().decode('utf-8')=={by1.getvalue().decode('utf-8')}")


def learn_method_30():
    print("learn_method_30")
    print('OS系统操作-------------------------------------------------------')
    print('os.name==', os.name)
    print('os.path==', os.path)
    print('os.uname()系统详情==', os.uname())
    print('os.environ，环境变量==', os.environ)
    print('os.environ.get(\'PATH\')==', os.environ.get('PATH'))
    print('当前文件目录的绝对路径==', os.path.abspath('.'))
    # print('创建目录==', os.path.join('.', 'testdir'))
    # print(os.mkdir('./testdir'))
    # print(os.rmdir('./testdir'))
    print('输出当前目录的所有文件和文件夹  ==', [d for d in os.listdir('.')])
    gene = (d for d in os.listdir('.'))
    print('中括号变成小括号，会转成 generator，是个对象===', gene)
    print('中括号变成小括号，会转成 generator，是个对象===', gene.__next__())
    print('输出当前文件夹', [d for d in os.listdir('.') if os.path.isdir(d)])
    print('输出.py结尾的文件', [d for d in os.listdir('.') if os.path.isfile(d) and os.path.splitext(d)[1] == '.py'])
    for d in os.listdir('.'):  # 获取当前目录下的文件和文件夹
        if os.path.isfile(d):  # 是否是文件
            print(f"文件名=={d};转化的数组=={os.path.splitext(d)}")  # 文件名数组化


def obj2dict(temp):
    return {
        'name': temp.name,
        'gender': temp.gender,
        'age': temp.age
    }


def learn_method_31():
    print("learn_method_31")
    print("json的loads与dumps方法应用")
    # print("json.dumps()	将 Python 对象编码成 JSON 字符串")
    # print("json.loads()	将已编码的 JSON 字符串解码为 Python 对象")
    # print("json.dump()	将Python内置类型序列化为json对象后写入文件")
    # print("json.load()	读取文件中json形式的字符串元素转化为Python类型")

    # json.dumps()	将 Python 对象编码成 JSON 字符串
    # json.loads()	将已编码的 JSON 字符串解码为 Python 对象
    # json.dump()	将Python内置类型序列化为json对象后写入文件
    # json.load()	读取文件中json形式的字符串元素转化为Python类型
    d = dict(name='李彬', age=59)
    text = {"name": '李彬', "age": '33'}
    print(f"字典dict: d=={d}")
    print(f"字典dict: text=={text}")
    print(f"type(d) == type(text)=={type(d) == type(text)}")
    json_str = json.dumps(d)
    print(f"json.dumps(d)：字典转字符串 == {json_str}，类型是== {type(json_str)}")
    dict1 = json.loads(json_str)
    print(f"json.loads()：字符串转成字典 == {dict1}，类型是== {type(dict1)}")

    ani = Animal('狗熊', '雄性', 333)
    json_str = json.dumps(ani, default=obj2dict)
    print(f"json.dumps()：将实例对象转成 json 字符串 == {json_str}")

    anis = [ani, ani]
    json_str = json.dumps(anis, default=obj2dict)
    print(f"json.dumps()：将 list集合转成 json数组 字符串 == {json_str}")

    json_str = json.dumps(ani, default=lambda temp: {
        'name': temp.name,
        'gender': temp.gender,
        'age': temp.age
    })
    print(f"json.dumps()：使用自带的 lambda 表达式 格式化json 字符串== {json_str}")

    json_str = json.dumps(ani, default=lambda temp: temp.__dict__)
    print(f"json.dumps()：使用自带的 __dict__ 格式化后的 json 字符串== {json_str}")

    print(f"json.loads()方法把对应的字符串转成对象")
    ani1 = json.loads(json_str, object_hook=lambda temp: Animal(temp['name'], temp['gender'], temp['age']))
    print(f"字符串 生成的对象=={ani1}，类型是=={type(ani1)}")

    stu = Student('李彬', '男', 33, 88)
    json_str = json.dumps(stu, default=Student.stu_dict)
    print(f"格式化后的 json 字符串=={json_str}")

    # 从文件中读取JSON数据
    with open('./file/json.txt', 'r') as f:
        data = json.load(f)
    print(f"从文件中获取的json字符串，是dict格式的，== {data}")
    stu = json.loads(json.dumps(data),
                     object_hook=lambda temp: Student(temp['name'], temp['gender'], temp['age'], temp['score']))
    print(f"输出生成的学生实例== {str(stu)}")
    with open('./file/json.json', 'r') as f:
        data = json.load(f)
    print(f"从文件中获取的json字符串数组，是dict格式的，== {data}")
    stu = json.loads(json.dumps(data),
                     object_hook=lambda temp: Student(temp['name'], temp['gender'], temp['age'], temp['score']))
    print(f"输出生成的学生实例数组== {str(stu)}")

    json_str = json.dumps(stu, default=Student.stu_dict)
    json_dict = json.loads(json_str)
    print("json.dump的文本最好是dict格式的，ensure_ascii为Fasle时输出的是utf_8格式，indent是缩进格式化")
    f = open('./file/dump.json', "w")
    json.dump(json_dict, f, ensure_ascii=False, indent=2)
    f.close()
    f = open('./file/dump.txt', "w")
    json.dump(json_dict, f, ensure_ascii=False, indent=1)
    f.close()
