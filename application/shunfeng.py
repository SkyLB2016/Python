# -*- coding: utf-8 -*-
"""
@Time    : 2024/10/10 18:25
@Author  : sky
@Email   : your-email@example.com
@File    : shunfeng.py
@Description: 
"""
import datetime

import requests
import xlrd
import zipfile
import os
import asyncio
import aiohttp


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


# 限制并发数量
semaphore = asyncio.Semaphore(10)  # 限制最多同时10个请求


# 读取Excel文件
async def analysis_excel_body(dir_path):
    try:
        excel_cursor = xlrd.open_workbook('file/江西兴助网络科技有限公司_202409.xlsx', encoding_override='utf8')
        sheets = excel_cursor.sheet_names()
        print("sheets", sheets)
        sheet_cursor = excel_cursor.sheet_by_index(0)
        rows = sheet_cursor.nrows
        print('共' + str(rows - 1) + '人')
        # excel_result = []
        task_all = []
        async with aiohttp.ClientSession() as session:
            tasks = []
            for rows_number in range(rows):
                # 取出整行数据
                row = sheet_cursor.row_values(rows_number)
                # 排除第0行
                if rows_number == 0: continue
                # excel_result.append(row)
                # 每个人的文件目录名
                user_path = row[1] + "-" + row[4] + "-" + row[5]
                # 每个人的保存路径
                save_path = dir_path + '/' + user_path
                # 检查目录
                check_path(save_path)
                # 文件夹内包含4个文件，分别为 身份证正面图片、身份证反面图片、身份证手持图片、协议信息，文件命名规则：姓名 - 手机号 - 身份证号 - 链接对应的表头【例：张旭 - 133156523 - 130324200 - 身份证正面图片.jpg】
                # 添加任务
                tasks.append(
                    asyncio.create_task(save_file(session, user_path + "-身份证正面图片.jpg", row[6], save_path)))
                tasks.append(
                    asyncio.create_task(save_file(session, user_path + "-身份证反面图片.jpg", row[7], save_path)))
                tasks.append(
                    asyncio.create_task(save_file(session, user_path + "-身份证手持图片.jpg", row[8], save_path)))
                tasks.append(asyncio.create_task(save_file(session, user_path + "-协议信息.pdf_new", row[9], save_path)))
            # print('第', rows_number, '人')
            # 开始执行
            await asyncio.gather(*tasks)
        # print(excel_result)
        print('共' + str(rows - 1) + '人')
    except Exception as e:
        print(e)


async def save_file(session, name, url, save_path):
    if url is None or url.strip() == "":
        return
    async with semaphore:
        try:
            async with session.get(url, ssl=False) as response:
                if response.status == 200:
                    # 下载数据
                    file_name = os.path.join(save_path, str(name))
                    with open(file_name, 'wb') as file:
                        while True:
                            chunk = await response.content.read(1024)
                            if not chunk:
                                break
                            file.write(chunk)
                    print(f'保存路径 {file_name}')
                else:
                    print(f"Failed to download {url}, status code: {response.status}")
        except Exception as e:
            print(f"Error downloading {url}: {e}")


def create_zip(dir_path):
    stamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # 获取要压缩的文件列表
    files_to_zip = [
        dir_path + "/" + file_str  # 最终返回
        for file_str in os.listdir(dir_path)  # 循环
        if os.path.isdir(dir_path + "/" + file_str)
    ]
    print("文件总数", len(files_to_zip))

    # 生成所有人的压缩包
    dir_zip_path = dir_path + "-zip/"
    check_path(dir_zip_path)
    for i in range(0, len(files_to_zip)):
        path = files_to_zip[i]
        # print("path", path)
        files = [
            path + "/" + file_str  # 最终返回
            for file_str in os.listdir(path)  # 循环
            if os.path.isfile(path + "/" + file_str)
        ]
        create_zip_file(dir_zip_path + path.split('/')[1] + '.zip', files)

    # 获取每个人的压缩包
    files_to_zip = [
        dir_zip_path + file_str  # 最终返回
        for file_str in os.listdir(dir_zip_path)  # 循环
        if os.path.isfile(dir_zip_path + file_str)
    ]
    print("zip 文件总数", len(files_to_zip))
    # 按500份为一组
    file_list = [files_to_zip[i:i + 500] for i in range(0, len(files_to_zip), 500)]
    print("共分为", len(file_list), "组")
    for i in range(0, len(file_list)):
        print("文件数量", len(file_list[i]))
        create_zip_file(dir_path + "-" + stamp + "-" + str(i + 1) + '.zip', file_list[i])


def create_zip_file(dir_name, files_to_zip):
    try:
        # 创建ZIP文件
        with zipfile.ZipFile(dir_name, 'w') as zipf:
            for file in files_to_zip:
                if os.path.isfile(file):
                    zipf.write(file)
                    # print(11111111111, file)
                elif os.path.isdir(file):
                    for root, dirs, files in os.walk(file):
                        for f in files:
                            zipf.write(os.path.join(root, f))
                            # print(2222222222222222, f)
        print("ZIP文件创建成功")
    except FileNotFoundError as e:
        print(f"文件未找到: {e}")
    except zipfile.BadZipFile as e:
        print(f"无效的ZIP文件: {e}")
    except Exception as e:
        print(f"发生错误: {e}")


def check_dir(dir_path):
    # 要压缩的文件列表
    files_to_zip = [
        dir_path + "/" + file_str  # 最终返回
        for file_str in os.listdir(dir_path)  # 循环
        if os.path.isdir(dir_path + "/" + file_str)
    ]
    print(len(files_to_zip))
    ddd = os.listdir(dir_path)
    print(len(ddd))
    for file in files_to_zip:
        if os.path.isdir(file):
            ddd = os.listdir(file)
            if len(ddd) < 3:
                print(file)


start_time = datetime.datetime.now()
start_stamp = start_time.timestamp()
print(start_time)
dir_path = '众包骑士信息'
# 启动事件循环
asyncio.run(analysis_excel_body(dir_path))
create_zip(dir_path)
# check_dir(dir_path)

end_time = datetime.datetime.now()
end_stamp = end_time.timestamp()
time_stamp = end_stamp - start_stamp
print()
print("开始时间", start_time)
print("结束时间", end_time)
print("耗费时间", int(time_stamp), "秒")
print("耗费时间", int(int(time_stamp) / 60), "分", int(time_stamp) % 60, '秒')
