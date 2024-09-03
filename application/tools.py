# 检查文件夹是否存在,不存在生成
import os


def check_path(path):
    if os.path.exists(path):
        return
    paths = path.split('/')
    temp = ""
    for text in paths:
        if not text:
            continue
        temp = f"{temp}{text}/"
        if not os.path.exists(temp):
            os.mkdir(temp)
