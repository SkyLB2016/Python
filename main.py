#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from application import pachong_rj
from application import create_pdf
from application.learn import learn  # 只导入 learn01 中对应的 learn_method 方法。

# 控制台输入操作
# s = input('birth: ')
# birth = int(s)
# if birth < 2000:
#     print('00前')
# else:
#     print('00后')

# print('python的数据类型分为：整数，浮点数，字符串，布尔值，还有个特殊值 None（空值）---------------------------------------')
# learn.learn_method_01()
# print('字符编码转换-------------------------------')
# learn.learn_method_02()
# print('字符串格式化，是字符串与变量的格式化拼接----------------------------------')
# learn.learn_method_03()

# print('python 内置的数据列表类型：list 与 tuple----------------------------------')
# learn.learn_method_04()

# print('python 的字典集合：distmap ----------------------------------')
# learn.learn_method_05()

# print('set集合----------------------------------')
# learn.learn_method_06()

# print('数据类型转换----------------------------------')
# learn.learn_method_07()

# print('时间类型转换----------------------------------')
# time_format()

# print('函数多个返回值测试,其实返回的是一个tuple 类型，可以单个变量逐个接收，也可以接收整个tuple--------------')
# x, y, z, a, b = learn.learn_method_08()
# print(x)
# print(y)
# print(z)
# print(a)
# b = learn.learn_method_08()
# print(b)

# print(f'参数对应类型验证=={isinstance(9, (int, float))}')
# learn.learn_method_09()
# print('函数定义，默认参数，可变参数，关键字参数，命名关键字参数，以及组合---------------------')
# learn.learn_method_10()
# print('去除字符串中空字符的几种方法---------------')
# learn.learn_method_11()
# print('递归函数-------------------------------------------')
# learn.learn_method_12()
# print('切片操作符-------------------------------------------')
# learn.learn_method_13()
# print('循环，迭代，Iterable---------------------------------------------------------------')
# learn.learn_method_14()
# print('列表生成式，以中括号[]为准，繁琐的一比---------------------------------------------')
# learn.learn_method_15()

# print('列表生成器 generator，以小括号 ()为准-----------------------------')
# learn.learn_method_16()

# print('MD5加密------------------------------')
# learn.learn_method_17()

# print('map，reduce，filter，sorted方法的使用---------------------------------------------')
# learn.learn_method_18()

# print('闭包的使用---------------------------------------------------------------------')
# learn.learn_method_19()

# print('匿名函数应用,lambda 表示匿名函数，函数的简化-------------------------------------------------')
# learn.learn_method_20()

# print("装饰器模式-----------------------------------------")
# learn.learn_method_21()

# print('自定义类，属性-------------------------------------------------')
# print('集成与多态-----------------------------------------------------------------')
# learn.learn_method_22()

# print('type()，dir(),hasattr,getattr,setattr 方法使用，获取类型-----------------------------------------------------------------')
# learn.learn_method_23()

# print('MethodType动态绑定方法-------------------------------------------------------')
# learn.learn_method_24()

# print('自定义类__slots__绑定属性，绑定之后，这各类只能有这几个属性，不能在定义其他属性------------------------------------------------------------')
# learn.learn_method_25()

# print('__xxx__ 特殊属性的使用---------------------------------------------------')
# learn.learn_method_26()

# print('文件读写-------------------------------------------------------')
# learn.learn_method_27()

# print('StringIO操作-------------------------------------------------------')
# learn.learn_method_28()

# print('BytesIO操作-------------------------------------------------------')
# learn.learn_method_29()

# print('OS系统操作-------------------------------------------------------')
learn.learn_method_30()

# print("json的loads与dumps方法应用")
# learn_json()

learn.learn_method()
# 爬取网站图片
# 网站URL
# url = "https://mp.weixin.qq.com/s/A4k3fSQEjTxgKhuq5E0fYw"
# pachong_rj.download_images(url, save_folder="static/images")

# 生成pdf
# create_pdf.create_pdf(image_path='static/images', file_name='人教版数学一年级上册预习卡')
create_pdf.create_pdf_alpha(image_path='static/images', file_name='人教版数学一年级上册预习卡1')
