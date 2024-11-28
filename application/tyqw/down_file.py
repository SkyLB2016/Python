# -*- coding: utf-8 -*-
"""
@Time    : 2024/11/7 11:31
@Author  : sky
@Email   : your-email@example.com
@File    : down_file.py
@Description: 
"""
import os

import requests
from urllib.parse import urlparse

from application import tools


def get_task_id():
    api_key = os.environ.get("DASHSCOPE_API_KEY")
    # print(api_key)

    # 1.定义URL
    url = 'https://dashscope.aliyuncs.com/api/v1/services/aigc/text2image/image-synthesis'
    # 2.定义请求头，常见的头部包括 `Content-Type` 和 `Authorization`。
    headers = {
        "Sec-Fetch-Dest": "image",
        'X-DashScope-Async': 'enable',
        'Content-Type': 'application/json',
        # 'Authorization': 'Bearer sk-57134a934d3d4d2d99d84d2812f88424'
        'Authorization': f'Bearer {api_key}'
    }
    # 3.定义POST请求参数
    data = {
        "model": "wanx-v1",
        # "model": "FindAgent",
        "input": {
            # "prompt": "中国美少女，长腿内衣，翘臀，高分辨率，增加细节，细节强化，正面视角，肤若凝脂，面如冠玉，极高分辨率，清晰度强化，山水间"
            "prompt": "中国美少女，长腿内衣，坐姿，叉开腿，高分辨率，增加细节，细节强化，正面视角，肤若凝脂，面如冠玉，精致的脸部比例，极高分辨率，清晰度强化，室内"
        },
        "parameters": {
            "style": "<auto>",
            # "size": "720*1280",
            "size": "1024*1024",
            "n": 1
        }
    }
    # 4.发送POST请求，并传递 URL、头部和数据。
    response = requests.post(url, headers=headers, json=data)
    # 5.检查响应状态码
    if response.status_code == 200:
        # 6.打印响应内容
        # print(response.json())
        content = response.json()
        task_id = content['output']['task_id']
        # print(task_id)
        return task_id
    else:
        # 打印响应内容
        # print(f'请求失败，状态码: {response.status_code}')
        print(f'请求失败，状态码: {response.status_code}', response.text)


def get_image_url(task_id):
    # 1.定义URL
    # url_template = 'https://dashscope.aliyuncs.com/api/v1/tasks/{task_id}'
    # url = url_template.format(task_id=task_id)
    url = f'https://dashscope.aliyuncs.com/api/v1/tasks/{task_id}'
    # 2.定义请求头，常见的头部包括 `Content-Type` 和 `Authorization`。
    headers = {
        'X-DashScope-Async': 'enable',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer sk-57134a934d3d4d2d99d84d2812f88424'
    }
    # 3.定义 GET 请求参数
    # params = {
    #     'task_id': task_id
    # }
    # 4.发送POST请求，并传递 URL、头部和数据。
    # response = requests.get(url, headers=headers,params=params)
    response = requests.get(url, headers=headers)
    # 5.检查响应状态码
    if response.status_code == 200:
        # 6.打印响应内容
        # print(response.json())
        content = response.json()
        output = content['output']
        if 'results' in output:
            url = output['results'][0]['url']
            print("url", url)
            return url
        else:
            print(output)
        return None
    else:
        # 打印响应内容
        print(f'请求失败，状态码: {response.status_code}', response.text)


# 下载文件
def dowmload_image(image_url, dir=''):
    # 目标 URL
    # 解析 URL 以提取文件名
    parsed_url = urlparse(image_url)
    path = parsed_url.path
    file_name = path.split('/')[-1]
    # 如果文件名中包含查询参数，去除查询参数部分
    if '?' in file_name:
        file_name = file_name.split('?')[0]

    # 定义保存文件的路径
    file_path = "../../static/ty_images/" + dir + "/"
    tools.check_path(file_path)
    file_path = file_path + file_name
    # 发送 GET 请求
    response = requests.get(image_url)

    # 检查请求是否成功
    if response.status_code == 200:
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print(f'文件已成功下载并保存为 {file_path}')
    else:
        print(f'请求失败，状态码: {response.status_code}')
        print('响应内容:', response.text)


# task_ids = []
# for i in range(0, 32):
#     id = get_task_id()
#     if id:
#         task_ids.append(id)
# print(task_ids)
# print(len(task_ids))
task_ids = ['2153b2ba-01c9-400d-bef9-80c733ae4d14']
print(len(task_ids))
error_ids = []
for id in task_ids:
    url = get_image_url(id)
    if url:
        dowmload_image(url, '')
    else:
        error_ids.append(id)
print(error_ids)
