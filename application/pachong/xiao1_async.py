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
    # url = "https://www.ruwen5.org/dushu/111910077/"
    # base_url = "https://www.ruwen5.org"
    # file_name = "仙帝大人今天也在都市努力躺平"
    # asyncio.run(get_chapter_list(url, base_url, file_name, 0, 100))
    # url = "https://www.ruwen5.org/dushu/111769663/"
    # base_url = "https://www.ruwen5.org"
    # file_name = "喂,修仙界有人诈骗1"
    # asyncio.run(get_chapter_list(url, base_url, file_name, 0, 300))
    #
    # url = "https://www.ruwen5.org/dushu/111328462/"
    # base_url = "https://www.ruwen5.org"
    # file_name = "山神娘娘"
    # asyncio.run(get_chapter_list(url, base_url, file_name, 0, 300))

    # url = "https://www.ruwen5.org/dushu/111915804/"
    # base_url = "https://www.ruwen5.org"
    # file_name = "异界求生"
    # asyncio.run(get_chapter_list(url, base_url, file_name, 0, 300))
    # url = "https://www.ruwen5.org/dushu/111905803/"
    # base_url = "https://www.ruwen5.org"
    # file_name = "火箭"
    # asyncio.run(get_chapter_list(url, base_url, file_name, 0, 300))
    file_name = "山神娘娘"
    # file_name = "山神娘娘"
    get_text("里栖",file_name)


def get_text(text='', file_name=''):
    # 输出地址
    src_file = f"static/txt/{file_name}.txt"
    # 发送HTTP请求
    with open(src_file, 'r') as f:
        lines = f.readlines()
    print('行数  ', len(lines))
    output_file = f"static/txt/{file_name}-{text}.txt"
    with open(output_file, 'w', encoding='utf-8') as f:
        for line in lines:
            if text in line:
                f.write('#    \n')
                f.write(line)
async def get_chapter_list(url='', base_url='', file_name='', start=0, end=9999):
    # 输出地址
    output_file = f"static/txt/{file_name}.txt"
    # 发送HTTP请求
    response = requests.get(url, headers=headers)
    # response.encoding = response.apparent_encoding  # 自动检测编码

    # if response.status_code == 200:
    response.raise_for_status()  # 检查请求是否成功
    # 解析HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    # print("soup", soup)
    # 查找目录列表
    # chapter_list = soup.select('.box_con dl dd a')
    chapter_list = soup.select('.inner dl dd a')
    # chapter_list = soup.select('.all ul li a')
    # print("chapter_list", chapter_list)
    print("chapter_list", len(chapter_list))

    # 存储章节信息
    chapters = []

    for chapter in chapter_list:
        chapter_name = chapter.text.strip()
        # title = chapter.get_text(strip=True)
        chapter_url = base_url + chapter['href']
        chapters.append((chapter_name, chapter_url))
        chapters.append(['', chapter_url.replace('.html', '_2.html')])
        chapters.append(['', chapter_url.replace('.html', '_3.html')])
        # chapters.append(['', chapter_url.replace('.html', '_4.html')])
        # chapters.append(['', chapter_url.replace('.html', '_5.html')])
        # chapters.append(['', chapter_url.replace('.html', '_6.html')])
        # chapters.append(['', chapter_url.replace('.html', '_7.html')])
        # chapters.append(['', chapter_url.replace('.html', '_8.html')])
        # chapters.append(['', chapter_url.replace('.html', '_9.html')])

    # print("chapters", chapters)
    print("chapters", len(chapters))
    # chapters = chapters[108:]
    chapters = chapters[36:]
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
    exits_text = []
    # 保存到文件
    with open(output_file, 'w', encoding='utf-8') as f:
        for chapter in results:
            f.write(chapter[1])
            f.write("\n")
            # f.write(chapter[2])
            # f.write("\n")
            line_list = str(chapter[2]).split('\n')
            for i in range(0, len(line_list)):
                line_text = line_list[i].strip()
                if i == 0:
                    if line_text in exits_text:
                        # print("重复", line_text)
                        break
                    else:
                        exits_text.append(line_text)
                f.write(line_text)
                f.write("\n")

    lines = []
    with open(output_file, 'r') as f:
        lines = f.readlines()
    print('行数  ', len(lines))
    # output_file = f"static/txt/{file_name}1.txt"
    with open(output_file, 'w', encoding='utf-8') as f:
        for line in lines:
            if '\n' != line and '本章未完，点击下一页继续阅读。' not in line:
                # f.write('\n')
                # f.write(line)
                f.write('#    \n')
                f.write('#    ' + line)


async def get_chapter(semaphore, session, index, name, url):
    async with semaphore:
        try:
            async with session.get(url, ssl=False, headers=headers) as response:
                time.sleep(0.25)
                if response.status == 200:
                    html = await response.text()
                    # 解析HTML
                    soup = BeautifulSoup(html, 'html.parser')
                    # print("soup", soup)
                    # 查找文章标题
                    title = soup.find('h1').text.strip()
                    print(title)
                    # # 查找目录列表
                    # content_div = soup.find('div', id='booktxt')
                    # content_div = soup.find('div', id='content')
                    content_div = soup.find('div', id='BookText')
                    # print(content_div)
                    text_content = content_div.get_text(strip=False, separator='\n')
                    # text_content = content_div.get_text()
                    # print(text_content)

                    return index, name, text_content
                else:
                    print("response.status==", response.status)
                    return index, name, "获取失败"

        except Exception as e:
            print(f"失败 {name}:{url}: {e}")
            return index, name, "获取失败"
