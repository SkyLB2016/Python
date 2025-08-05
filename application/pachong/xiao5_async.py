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
    url = "https://www.220book.com/chapter/RLAH.html"
    base_url = "https://www.220book.com"
    file_name = "sssj"
    asyncio.run(get_chapter_list(url, base_url, file_name,  0,100))
    url = "https://www.220book.com/chapter/4344.html"
    base_url = "https://www.220book.com"
    file_name = "yezhu"
    asyncio.run(get_chapter_list(url, base_url, file_name,  0,100))

async def get_chapter_list(url='', base_url='', file_name='', start=0, end=9999):
    # 输出地址
    output_file = f"static/txt/{file_name}.txt"
    # 发送HTTP请求=
    response = requests.get(url, headers=headers)
    # if response.status_code == 200:
    response.raise_for_status()  # 检查请求是否成功
    # 解析HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    # print("soup", soup)

    # 查找目录列表
    chapter_list = soup.find('div', class_='list list3 chapListBody').find_all('a')
    print("chapter_list",chapter_list)

    # 存储章节信息
    chapters_old = []

    for chapter in chapter_list:
        chapter_name = chapter.text.strip()
        chapter_url = base_url + chapter['href']
        chapters_old.append([chapter_name, chapter_url])
    # chapters_old = chapters_old[12:]
    chapters = chapters_old[start:end]

    # chapters = []
    # for chapter in chapters_old:
    #     chapters.append([chapter[0], chapter[1]])
    #     chapters.append(['', chapter[1].replace('.html', '_2.html')])


    # 限制并发数量
    semaphore = asyncio.Semaphore(10)  # 限制最多同时10个请求

    async with aiohttp.ClientSession() as session:
        tasks = []
        for i, chapter in enumerate(chapters):
            print(f"Chapter {i + 1}: {chapter[0]} - {chapter[1]}")
            tasks.append(asyncio.create_task(get_chapter(semaphore, session, i, chapter[0], chapter[1])))
        results = await asyncio.gather(*tasks)
    # print(results)
    print("异步任务个数", len(results))
    # 保存到文件
    with open(output_file, 'w', encoding='utf-8') as f:
        index = 0
        for chapter in results:
            # if str(chapter[2]) is None:
            #         continue
            f.write(chapter[1])
            f.write("\n")
            f.write(chapter[2])
            f.write("\n")
            # if str(chapter[1]).startswith('0'):
            #     f.write(f"第{index + 1}章{chapter[1]}")
            #     f.write(chapter[2])
            #     f.write("\n")
            #     index += 1

    lines = []
    with open(output_file, 'r') as f:
        lines = f.readlines()
    print('行数  ', len(lines))
    with open(output_file, 'w', encoding='utf-8') as f:
        for line in lines:
            if '\n' != line:
                # f.write(line)
                f.write('#    \n')
                f.write('#    ' + line)


async def get_chapter(semaphore, session, index, name, url):
    async with semaphore:
        try:
            async with session.get(url, ssl=False, headers=headers) as response:
                if response.status == 200:
                    html = await response.text()
                    # 解析HTML
                    soup = BeautifulSoup(html, 'html.parser')
                    # print("soup", soup)
                    # 查找文章标题
                    title = soup.find('h1').text.strip()
                    print(title)

                    # 查找文章内容
                    # content_div = soup.find('div', class_='showtxt')
                    # print(content_div)
                    content_div = soup.find('div', id='content')
                    # print(content_div)
                    text_content = content_div.get_text(strip=False, separator='\n')
                    # text_content = content_div.get_text()
                    # print(text_content)

                    return index, name, text_content
                else:
                    print("response.status==", response.status)
                    return index, name, "获取失败"

        except Exception as e:
            print(f"失败 {name}：{url}: {e}")
            return index, name, "获取失败"
        # finally:semaphore