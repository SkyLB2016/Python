#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from application import create_pdf, learn
from application.pdf_to_image import convert_pdf_to_images
from application.pdf_to_image1 import convert_pdf_to_images1

# 控制台输入操作
# s = input('birth: ')
# birth = int(s)
# if birth < 2000:
#     print('00前')
# else:
#     print('00后')

# print('时间类型转换----------------------------------')
# time_format()
# print("json的loads与dumps方法应用")
# learn_json()

learn.learn_method()
# 爬取网站图片
# 网站URL
# url = "https://mp.weixin.qq.com/s/A4k3fSQEjTxgKhuq5E0fYw"
# pachong_rj.download_images(url, save_folder="static/images")

# 生成pdf
# create_pdf.create_pdf(image_path='static/images', file_name='人教版数学一年级上册预习卡')
# create_pdf.create_pdf(image_path='static/images', file_name='人教版数学一年级上册预习卡2')
# create_pdf.create_pdf(image_path='static/images', file_name='人教版数学一年级上册预习卡3')
# create_pdf.create_pdf_alpha(image_path='static/images', file_name='人教版数学一年级上册预习卡3')


# pdf转成图片
# convert_pdf_to_images('static/english.pdf', 'static/english')
# 这个不好用
# convert_pdf_to_images1('static/english.pdf', 'static/english')

# 把生成的图片拆分成两个pdf，一个存正面，一个存反面
create_pdf.create_pdf_interval(image_path='static/english', file_name='英语')
