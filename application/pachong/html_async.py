import asyncio

import aiohttp
import requests
from bs4 import BeautifulSoup


# 古诗文网站文本爬取
def get_content():
    # 爬取的网址 以及 文件名

    url = "https://quark.alibaba.com/dashboard/downloads.htm?autoDownload=true&reportId=1223726"
    file_name = "knight_task"
    asyncio.run(get_chapter_list(url, file_name))



async def get_chapter_list(url='', file_name=''):
    # 发送HTTP请求
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    # response = requests.get(url, headers=headers)
    response = requests.get(url)
    # if response.status_code == 200:
    response.raise_for_status()  # 检查请求是否成功
    # 解析HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    print("soup", soup)
    # 查找目录列表

    # content_div = soup.find("div", class_="rich_media_content js_underline_content autoTypeSetting24psection")
    # print("content_div", type(content_div))
    # print("content_div", len(content_div))
    # text_content = content_div.get_text(strip=False, separator='\n')
    # # 输出地址
    # output_file = f"static/txt/{file_name}.txt"
    #
    # # 保存到文件
    # with open(output_file, 'w', encoding='utf-8') as f:
    #     f.write(text_content)
    #
    # lines = []
    # with open(output_file, 'r') as f:
    #     lines = f.readlines()
    # lines.pop(0)