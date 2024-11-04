#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import asyncio

from application import learn
from application.pachong import xiao_async, 爱阅读_async
from application.pdf import create_pdf, pdf_to_image

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
# asyncio.run(xiao_async.get_content())
# asyncio.run(爱阅读_async.get_content())

# pdf 工具
create_pdf.main()

