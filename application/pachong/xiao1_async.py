import asyncio

import aiohttp
import requests
from bs4 import BeautifulSoup


# 爬取 4小说 网站文本爬取
def get_content(url='', file_name=''):
    # 爬取的网址 以及 文件名
    url = "https://www.shshaoshi.com/shi/352598/"
    # url = "http://www.3kdoo.com/Lesen/230/230727/"
    # url = "http://www.156xsw.com/book/230_230717.html"
    # url = "https://www.0794.org/ea/230731/"
    file_name = "hzyh"
    asyncio.run(get_chapter_list(url, file_name, 1110))


async def get_chapter_list(url='', file_name='', start=0):
    # 输出地址
    output_file = f"static/txt/{file_name}.txt"
    # 发送HTTP请求
    response = requests.get(url)
    # if response.status_code == 200:
    response.raise_for_status()  # 检查请求是否成功
    # 解析HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    # print("soup", soup)
    # 查找目录列表
    chapter_list = soup.select('.box_con dl dd a')
    # print("chapter_list", chapter_list)

    # 存储章节信息
    chapters = []

    for chapter in chapter_list:
        chapter_name = chapter.text.strip()
        # title = chapter.get_text(strip=True)
        chapter_url = 'https:' + chapter['href']
        chapters.append((chapter_name, chapter_url))
    # print("chapters", chapters)
    # chapters = chapters[:]
    # chapters = chapters[start:]
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
            async with session.get(url, ssl=False) as response:
                if response.status == 200:
                    html = await response.text()
                    # 解析HTML
                    soup = BeautifulSoup(html, 'html.parser')
                    # print("soup", soup)
                    # 查找文章标题
                    title = soup.find('h1').text.strip()
                    print(title)
                    # # 查找目录列表
                    # content_div = soup.find('div', class_='showtxt')
                    content_div = soup.find('div', id='content')
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
                    print("response.status==", response.status)
                    return index, name, "获取失败"

        except Exception as e:
            print(f"失败 {url}: {e}")
            return index, name, "获取失败"
        # finally:semaphore