#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import asyncio
import datetime
import hashlib
import string
import random

import bcrypt

from application import learn
from application.pachong import xiao_async, 古诗文, xiao2_async, xiao1_async, text_async
from application.pdf import create_pdf, pdf_to_image, create_pdf2
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
# xiao_async.get_content()
xiao1_async.get_content()
# xiao2_async.get_content()
# 古诗文.get_content()
# text_async.get_content()
# html_async.get_content()
# photo_restoration('static/image/laoye.jpg', 'static/image/laoye_new.jpg')
# restore_photo(
#         input_path="static/image/laoye.jpg",  # 输入文件路径
#         output_color="static/image/laoye_caise.jpg",  # 彩色输出路径
#         output_bw="static/image/laoye_heibai.jpg"  # 黑白输出路径
#     )

# pdf 工具
# 处理单文件
# create_pdf.main()
# create_pdf2.create_pdf('25一下课课贴')
# 处理多文件
# create_pdf.many_file()

# 文本工具
# text_utils.main()
# text_utils.read_dd()

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
# now = datetime.datetime.now()
# print(16376327*0.51)
# a= 1587+ 8334+ 199+ 63+ 320+ 4048+ 455+ 2837+ 103+ 732+ 530+ 3091+ 4179+ 1976+ 3672+ 807+ 2+ 966+ 3015+ 3015+ 930+ 7988+ 1813+ 2883+ 4904+ 1901+ 1312+ 3973+ 1313+ 3870+ 3285+ 1200+ 655+ 3944+ 520+ 6585+ 120+ 53+ 1405+ 2283+ 5594+ 2231+ 3481+ 3902+ 270+ 1320+ 3616+ 1334+ 1372+ 784+ 1023+ 3622+ 255+ 149+ 18+ 278+ 63+ 1664+ 287+ 508+ 432+ 1+ 5864+ 3994+ 615+ 2005+ 2415+ 4422+ 3028+ 16+ 903+ 1487+ 1100+ 3225+ 142+ 741+ 2363+ 407+ 5045+ 4048+ 5+ 1+ 493+ 157+ 2169+ 4171+ 7653+ 722+ 3341+ 1420+ 7056+ 3159+ 1+ 5022+ 1354+ 1633+ 469+ 49+ 53+ 4422+ 64+ 1053+ 2735+ 10+ 6231+ 3824+ 57+ 421+ 213+ 633+ 292+ 292+ 1695+ 429+ 413+ 3077+ 1091+ 2072+ 81+ 778+ 4430+ 1+ 3629+ 1475+ 5817+ 1142+ 875+ 1612
# print(a)

# a = 16576428+39116491
# print(a)
# print(16576428/88888)
# print(15+32+28+26+27+11+17+15+15+18+21+30)
# res = 8.88178419700125E-16
# print(res)
# print(round(res, 3))
# print("{:.2f}".format(res))
# print("直营优选总数据量：", 7920000 + 7599530)
# # 共有8588665条
# print("霖润众包共有：8588665条")
# print("霖珑众包共有：37916492")
# print("众包共有：", 37916492 + 8588665)
# print("重复数据有：", 9497789 - 4088817)
# print("不重复数据共有：", 7920000 + 7599530 - 9497789 + 4088817)
# # INSERT INTO MY_TABLE(`count()`, `sum(count)`) VALUES (4088817, 9497789);
# print("霖珑共有：", 37916492 + 16576428)
# print("霖珑共有：", 54155189)
# print("霖珑共有：", 54492920-54155189)
# print("共有：", 37916492 + 8588665 + 16576428)
