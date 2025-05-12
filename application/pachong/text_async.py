import asyncio

import aiohttp
import requests
from bs4 import BeautifulSoup


# 古诗文网站文本爬取
def get_content():
    # 爬取的网址 以及 文件名

    url = "https://mp.weixin.qq.com/s/MQY6Iur9_qf1jiMX2VGPew"
    file_name = "75"
    # asyncio.run(get_chapter_list(url, file_name))
    file_text(file_name)


def file_text(file_name):
    # 输出地址
    output_file = f"static/txt/{file_name}.txt"
    # 读取文件内容
    with open(output_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    poetries = []
    # data = []
    data_text = []
    for line in lines:
        # print('行数  ', len(line))
        if len(line) > 0 and line[0] in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
            if len(data_text) > 0:
                poetries.append(data_text)
            # data=[line]
            data_text = line
        else:
            # data.append(line)
            data_text += line
    poetries.append(data_text)

    output_hua = f"static/txt/含有花的古诗.txt"
    output_月 = f"static/txt/含有月的古诗.txt"
    for poetry in poetries:
        if "花" in poetry:
            with open(output_hua, 'a', encoding='utf-8') as f:
                f.write(poetry)
        if "月" in poetry:
            with open(output_月, 'a', encoding='utf-8') as f:
                f.write(poetry)



async def get_chapter_list(url='', file_name=''):
    # 发送HTTP请求
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    # if response.status_code == 200:
    response.raise_for_status()  # 检查请求是否成功
    # 解析HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    # print("soup", soup)
    # 查找目录列表

    content_div = soup.find("div", class_="rich_media_content js_underline_content autoTypeSetting24psection")
    print("content_div", type(content_div))
    print("content_div", len(content_div))
    text_content = content_div.get_text(strip=False, separator='\n')
    # 输出地址
    output_file = f"static/txt/{file_name}.txt"

    # 保存到文件
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(text_content)

    lines = []
    with open(output_file, 'r') as f:
        lines = f.readlines()
    lines.pop(0)

    with open(output_file, 'w', encoding='utf-8') as f:
        index = 0
        for line in lines:
            text = line.lstrip()
            if text[0] in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
                index = 0
                f.write('\n' + text.replace('\n', "") + '、')
            else:
                if index == 0:
                    f.write(text.replace('\n', "") + "  ")
                    index += 1
                else:
                    f.write(text)
