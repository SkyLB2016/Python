import asyncio
import time

import aiohttp
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.1234.567 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml',
    'Connection': 'keep-alive',
    'Accept-Language': 'en-US,en;q=0.9',

    # 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:138.0) Gecko/20100101 Firefox/138.0',
    # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    # 'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    # 'Accept-Encoding': 'gzip, deflate, br, zstd',
    # 'Connection': 'keep-alive',
    # 'Referer': 'https://www.24kxs.cc/book/4/4589/26534184.html',
    # 'Cookie': 'bcolor=; font=; size=; fontcolor=; width=',
    # 'Upgrade-Insecure-Requests': '1',
    # 'Sec-Fetch-Dest': 'document',
    # 'Sec-Fetch-Mode': 'navigate',
    # 'Sec-Fetch-Site': 'same-origin',
    # 'Sec-Fetch-User': '?1',
    # 'Priority': 'u=0, i',
    # 'TE': 'trailers'
}


def get_content(url='', file_name=''):
    # 爬取的网址 以及 文件名
    url = 'https://www.24kxs.cc/book/4/4589/'
    base_url = 'https://www.24kxs.cc/'
    file_name = "pcl"
    start = 307
    asyncio.run(get_chapter_list(url, base_url, file_name, start))
    # url = 'https://www.24kxs.cc/book/3598/3598044/'
    # base_url = 'https://www.24kxs.cc/'
    # file_name = "剑仙"
    # start = 0
    # end=10000
    # asyncio.run(get_chapter_list(url, base_url, file_name, start,end))


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
    # chapter_list = soup.select('.all-chapters li a')
    # chapter_list = soup.select('.all ul li a')
    chapter_list = soup.find('div', class_='listmain').find_all('a')
    # print("chapter_list",chapter_list)

    # 存储章节信息
    chapters = []

    for chapter in chapter_list:
        chapter_name = chapter.text.strip()
        chapter_url = base_url + chapter['href']
        chapters.append([chapter_name, chapter_url])
    chapters = chapters[12:]
    chapters = chapters[start:end]
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
            f.write(chapter[1])
            f.write("\n")
            f.write(chapter[2])
            f.write("\n")
            f.write("\n")
    lines = []
    with open(output_file, 'r') as f:
        lines = f.readlines()
    print('行数  ', len(lines))
    with open(output_file, 'w', encoding='utf-8') as f:
        for line in lines:
            if 'www.24kxs.cc' not in line:
                f.write(line)
                # f.write('#\n#    ' + line)


async def get_chapter(semaphore, session, index, name, url):
    async with semaphore:
        try:
            async with session.get(url, headers=headers, ssl=False) as response:
                time.sleep(0.125)
                if response.status == 200:
                    html = await response.text(errors='ignore')
                    # 解析HTML
                    soup = BeautifulSoup(html, 'html.parser')
                    # print("soup", soup)
                    # 查找文章标题
                    title = soup.find('h1').text.strip()
                    print(title)
                    # 查找文章内容
                    content_div = soup.find('div', class_='showtxt')
                    # print(content_div)
                    # content_div = soup.find('div', id='content')
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