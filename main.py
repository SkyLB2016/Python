#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import asyncio

from application import learn
from application.pachong import xiao_async, xiao1_async, xiao2_async
from application.pdf import create_pdf, pdf_to_image
from application.text import text_utils

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
asyncio.run(xiao_async.get_content())
# asyncio.run(xiao1_async.get_content())


# pdf 工具
# create_pdf.main()

# 文本工具
# text_utils.main()

# ll= [11]
# if 11 in ll:
#     print("存在")
# else:
#     print('不存在')
# ll.remove(11)
# if ll:
#     print('不为空')
# else:
#     print('为空')