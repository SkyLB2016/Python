#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import asyncio
import datetime

from application import create_pdf, learn, pdf_to_image, dateutils, pc_wenben_async, pc_wenben_async2

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
# pachong_rj.download_images(url, save_folder="static/pdf_images")
# 专项专用
# pc_wenben.get_content()
asyncio.run(pc_wenben_async.get_content())
asyncio.run(pc_wenben_async2.get_content())

# url='https://www.92yanqing.com/read/76564/'
# asyncio.run(pc_wenben_async3.get_content(url))

# 图片生成pdf
# create_pdf.create_pdf(image_path='static/pdf_images', file_name='人教版数学一年级上册预习卡')
# create_pdf.create_pdf_alpha(image_path='static/pdf_images', file_name='人教版数学一年级上册预习卡3')


# pdf_new 转成图片
# pdf_to_image.convert_pdf_to_images('static/english.pdf_new', 'static/english')

# 把生成的图片按奇偶拆分成多个 pdf_new，一个存正面，一个存反面
# create_pdf.create_pdf_two(image_path='static/english', file_name='英语')
# 把生成的图片按 每页两个 图片的模式拆分成两个pdf，一个存正面，一个存反面
# create_pdf.create_pdf_two1(image_path='static/yuwen', file_name='语文')

# print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
# print(datetime.datetime.now().timestamp())
# dateutils.time_format()
