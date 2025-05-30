import asyncio
import time

import aiohttp
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.1234.567 Safari/537.36',
    # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Accept': 'text/html,application/xhtml+xml',
    'Connection': 'keep-alive',
    'Accept-Language': 'en-US,en;q=0.9'
}


def get_content(url='', file_name=''):
    # 爬取的网址 以及 文件名
    url = "https://www.egpic.cn/txt/9VfDHK.html"
    base_url = "https://www.egpic.cn/"
    file_name = "侯门老祖"
    asyncio.run(get_chapter_list(url, base_url, file_name, 0,100))


async def get_chapter_list(url='', base_url='', file_name='', start=0, end=9999):
    # 输出地址
    output_file = f"static/txt/{file_name}.txt"
    # 发送HTTP请求
    response = requests.get(url,headers=headers)
    response.encoding = response.apparent_encoding  # 自动检测编码

    # if response.status_code == 200:
    response.raise_for_status()  # 检查请求是否成功
    # 解析HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    # print("soup", soup)
    # 查找目录列表
    chapter_list = soup.select('.box_con dl dd a')
    # chapter_list = soup.select('.all ul li a')
    # print("chapter_list", chapter_list)
    print("chapter_list", len(chapter_list))

    # 存储章节信息
    chapters = []

    for chapter in chapter_list:
        chapter_name = chapter.text.strip()
        # title = chapter.get_text(strip=True)
        chapter_url = chapter['href']
        chapters.append((chapter_name, chapter_url))
        # chapter_url = chapter_url.replace('.html', '_2.html')
        # chapters.append(['', chapter_url])

    # print("chapters", chapters)
    print("chapters", len(chapters))
    # chapters = chapters[9:]
    chapters = chapters[start:end]
    # 限制并发数量
    semaphore = asyncio.Semaphore(10)  # 限制最多同时10个请求

    async with aiohttp.ClientSession() as session:
        tasks = []
        for i, chapter in enumerate(chapters):
            print(f"Chapter {i + 1}: {chapter[0]} - {chapter[1]}")
            # chapter.append(get_chapter(i, chapter[0], chapter[1]))
            tasks.append(asyncio.create_task(get_chapter(semaphore, session, i, chapter[0], chapter[1])))
        results = await asyncio.gather(*tasks)
    # print(results)
    print("异步任务个数", len(results))
    # 保存到文件
    with open(output_file, 'w', encoding='utf-8') as f:
        for chapter in results:
            f.write(chapter[1])
            f.write("\n")
            f.write(chapter[2])
            f.write("\n")

    lines = []
    with open(output_file, 'r') as f:
        lines = f.readlines()
    print('行数  ', len(lines))
    with open(output_file, 'w', encoding='utf-8') as f:
        for line in lines:
            f.write('#    \n')
            f.write('#    ' + line)


async def get_chapter(semaphore, session, index, name, url):
    async with semaphore:
        try:
            response = requests.get(url, headers=headers)
            response.encoding = response.apparent_encoding  # 自动检测编码

            if response.status_code != 200:
                print("response.status==", response.status_code)
                return index, name, "获取失败"
            response.raise_for_status()  # 检查请求是否成功
            # 解析HTML
            soup = BeautifulSoup(response.text, 'html.parser')
            # print("soup", soup)
            # 查找文章标题
            # title = soup.find('h1').text.strip()
            # print(title)
            # # 查找目录列表
            # content_div = soup.find('div', id='booktxt')
            content_div = soup.find('div', id='content')
            # soup = soup.find('div', class_='content_read')
            # soup = soup.find('div', class_='box_con')
            # content_div = soup.find('div', id='content')
            # print(content_div)
            text_content = content_div.get_text(strip=False, separator='\n')
            # text_content = content_div.get_text()
            # print(text_content)
            return index, name, text_content
        except Exception as e:
            print(f"失败 {name}:{url}: {e}")
            return index, name, "获取失败"
        # finally:semaphore
