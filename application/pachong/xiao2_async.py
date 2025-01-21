import asyncio

import aiohttp
import requests
from bs4 import BeautifulSoup


# 爬取 4小说 网站文本爬取
async def get_content(url='', file_name=''):
    # 爬取的网址 以及 文件名
    # url = "https://m.lewensw.org/985/985528/"
    # # url = "https://m.lewensw.org/297/985528_2/"
    # # url = "https://m.lewensw.org/297/985528_1/"
    # file_name = "曾经"

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
    chapter_list = soup.find('ul', class_='chapter').find_all('a')
    print("chapter_list", chapter_list)

    # 存储章节信息
    chapters = []
    # url = "https://m.lewensw.org/books/985528/86824532.html"
    # url = "https://m.lewensw.org/books/985528/86824532_2.html"

    for chapter in chapter_list:
        chapter_name = chapter.text.strip()
        chapter_url = 'https://m.lewensw.org' + chapter['href']
        chapters.append([chapter_name, chapter_url])
        chapter_url = chapter_url.replace('.html', '_2.html')
        chapters.append(['', chapter_url])
    # chapters = chapters[19:]
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

    # lines = []
    # with œ   f.write('#    ' + line)


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
                    content_div = soup.find('div', id='nr_hpurgj')
                    content_div = soup.find('div', class_='nr_nr')
                    content_div = soup.find('div', id='ccc')
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
