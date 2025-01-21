import asyncio
import time

import aiohttp
import requests
from bs4 import BeautifulSoup


# 爬取 4小说 网站文本爬取
def get_content(url='', file_name=''):
    # 爬取的网址 以及 文件名
    url = "https://www.libahao.com/"
    file_name = "s"
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
    chapter_list = soup.select('.all-chapters li a')
    # print("chapter_list", chapter_list)

    # 存储章节信息
    chapters = []

    for chapter in chapter_list:
        chapter_name = chapter.text.strip()
        # title = chapter.get_text(strip=True)
        chapter_url = "https://www.libahao.com" + chapter['href']
        chapters.append((chapter_name, chapter_url))
        chapter_url = chapter_url.replace('.html', '_1.html')
        chapters.append(['', chapter_url])
        chapter_url = chapter_url.replace('.html', '_2.html')
        chapters.append(['', chapter_url])
        chapter_url = chapter_url.replace('.html', '_3.html')
        chapters.append(['', chapter_url])

    # https://www.libahao.com/book/12364394_5644/1.html
    # https://www.libahao.com/book/12364394_5644/1.html

    # print("chapters", chapters)
    print("chapters", len(chapters))
    chapters = chapters[0:]
    chapters = chapters[0:400]
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
            # f.write('#    \n')
            f.write('#    ' + line)
            # if '请记住本书首发域名' not in line:
            #     f.write(line)



async def get_chapter(semaphore, session, index, name, url):
    async with semaphore:
        try:
            async with session.get(url, ssl=False) as response:
                time.sleep(3)
                if response.status == 200:
                    html = await response.text()
                    # 解析HTML
                    soup = BeautifulSoup(html, 'html.parser')
                    # print("soup", soup)
                    # 查找文章标题
                    title = soup.find('h2').text.strip()
                    print("title",title)
                    # # 查找目录列表
                    content_div = soup.find('div', class_='chapter-content')
                    # content_div = soup.find('div', id='chapterContent')
                    # print("content_div",content_div)
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

# google-chrome --remote-debugging-port=9223 --user-data-dir=/opt/ChromeProfile2 --no-sandbox
#
# DevTools listening on ws://127.0.0.1:9223/devtools/browser/e949bf00-aac2-4529-9886-0a236e8ece34


# Tenant_Id 6aee9db666ec2e407ef7878e85e750ee 企微/钉钉平台ID ww1ef9f6229cdc59c5
# 公司简称 上海二十冶建设有限公司
# @乔月 @李彬 冲4000条短信、
# Tenant_Id 4ab4f2b2e2fcd8ea49b36b63b6d1365b 企微/钉钉平台ID ding0b96b7ba96557f3335c2f4657eb6378f
# 公司简称 浙江光珀智能
# @李彬 将 系统管理员权限 和 所有发薪数据 转移给李奇轩（钉钉ID：021121024426159824，手机号：13735815773）