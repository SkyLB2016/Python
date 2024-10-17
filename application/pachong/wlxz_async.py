import asyncio

import aiohttp
import requests
from bs4 import BeautifulSoup


# 爬取 万灵仙族 网站文本爬取
async def get_content():
    url = "http://www.4xiaoshuo.info/188/188360/"
    # 发送HTTP请求
    response = requests.get(url)
    # if response.status_code == 200:
    response.raise_for_status()  # 检查请求是否成功
    # 解析HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    # print("soup", soup)

    # 查找目录列表
    chapter_list = soup.find('div', class_='listmain').find_all('a')

    # 存储章节信息
    chapters = []

    for chapter in chapter_list:
        chapter_name = chapter.text.strip()
        chapter_url = url + chapter['href']
        chapters.append([chapter_name, chapter_url])
    chapters = chapters[12:]
    chapters.pop(1013)
    chapters.pop(1011)
    chapters.pop(1003)
    chapters.pop(953)
    chapters.pop(947)
    chapters.pop(899)
    chapters.pop(892)
    chapters.pop(834)
    chapters.pop(827)
    chapters.pop(789)
    chapters.pop(781)
    chapters.pop(730)
    chapters.pop(720)
    chapters.pop(711)
    chapters.pop(705)
    chapters.pop(703)
    chapters.pop(677)
    chapters.pop(644)
    chapters.pop(636)
    chapters.pop(545)
    chapters.pop(323)
    chapters.pop(55)
    # print(chapters[3][1])
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i, chapter in enumerate(chapters):
            print(f"Chapter {i + 1}: {chapter[0]} - {chapter[1]}")
            # chapter.append(get_chapter(i, chapter[0], chapter[1]))
            tasks.append(asyncio.create_task(get_chapter(session, i, chapter[0], chapter[1])))
        results = await asyncio.gather(*tasks)
    # print(results)
    print(len(results))
    # 保存到文件
    output_file = "static/万灵仙族.txt"
    with open(output_file, 'w', encoding='utf-8') as f:
        for chapter in results:
            f.write(chapter[1])
            f.write(chapter[2])
            f.write("\n")


# 限制并发数量
semaphore = asyncio.Semaphore(10)  # 限制最多同时10个请求


async def get_chapter(session, index, name, url):
    async with semaphore:
        try:
            async with session.get(url,ssl=False) as response:
                if response.status == 200:
                    html = await response.text()
                    # 解析HTML
                    soup = BeautifulSoup(html, 'html.parser')
                    # print("soup", soup)
                    # 查找文章标题
                    title = soup.find('h1').text.strip()
                    print(title)
                    # # 查找目录列表
                    content_div = soup.find('div', class_='showtxt')
                    # print(chapter_list)
                    text_content = content_div.get_text(strip=False, separator='\n')
                    # text_content = content_div.get_text()
                    # print(text_content)

                    # # 查找文章内容
                    # content_div = soup.find('div', class_='content')
                    # content_div = soup.find('div', id='content')
                    #
                    # text_content = content_div.get_text(strip=False, separator='\n')
                    # print(text_content)
                    # output_file = "static/chapters1.txt"
                    # with open(output_file, 'w', encoding='utf-8') as f:
                    #     f.write(text_content)
                    return index, name, text_content
                else:
                    print(response.status)

        except Exception as e:
            print(f"失败 {url}: {e}")
