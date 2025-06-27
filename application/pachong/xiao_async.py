import asyncio

import aiohttp
import requests
from bs4 import BeautifulSoup

# curl 'https://www.24kxs.cc/book/4/4589/' --compressed -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:138.0) Gecko/20100101 Firefox/138.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' -H 'Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2' -H 'Accept-Encoding: gzip, deflate, br, zstd' -H 'Connection: keep-alive' -H 'Referer: https://www.24kxs.cc/book/4/4589/26534184.html' -H 'Cookie: bcolor=; font=; size=; fontcolor=; width=' -H 'Upgrade-Insecure-Requests: 1' -H 'Sec-Fetch-Dest: document' -H 'Sec-Fetch-Mode: navigate' -H 'Sec-Fetch-Site: same-origin' -H 'Sec-Fetch-User: ?1' -H 'Priority: u=0, i' -H 'TE: trailers'
# google-chrome --remote-debugging-port=9223 --user-data-dir=/opt/ChromeProfile2 --no-sandbox
# google-chrome --remote-debugging-port=8687 --user-data-dir=/var/chrome-profile --no-sandbox
# 命令行启动 Chrome（确保关闭所有已运行实例）
# /path/to/chrome --remote-debugging-port=8687 --user-data-dir=/tmp/chrome-profile
# usr/bin/google-chrome
# DevTools listening on ws://127.0.0.1:9223/devtools/browser/e949bf00-aac2-4529-9886-0a236e8ece34

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.1234.567 Safari/537.36',
    # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Accept': 'text/html,application/xhtml+xml',
    'Connection': 'keep-alive',
    'Accept-Language': 'en-US,en;q=0.9'
}

# 爬取 4小说 网站文本爬取
def get_content(url='', file_name=''):
    # 爬取的网址 以及 文件名
    # url = "http://www.4xiaoshuo.org/198/198862/"
    # file_name = "没钱修什么仙"
    # asyncio.run(get_chapter_list(url, file_name, 299))
    url = "http://www.4xiaoshuo.org/162/162265/"
    file_name = "仙人"
    start = 2271
    end = start + 4
    asyncio.run(get_chapter_list(url, file_name, start, end))

async def get_chapter_list(url='', file_name='', start=0, end=9999):
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
    chapter_list = soup.find('div', class_='listmain').find_all('a')
    # chapter_list = soup.select('.box_con dl dd a')
    # print("chapter_list",chapter_list)

    # 存储章节信息
    chapters = []

    for chapter in chapter_list:
        chapter_name = chapter.text.strip()
        chapter_url = url + chapter['href']
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
            if '请记住本书首发域名' not in line:
                # f.write(line)
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
#   利大于弊。
#     
#    非常时期，别只盯着次要矛盾不放。
#     
#    全是好处而没有副作用，天底下哪有这种好事？
#     
#    此次国君会晤之后，牟国得到苍晏支持，与贝迦的战斗更加迂回但坚决。
#     
#    两个大国之间的激烈战争，并没像很多人期待的那样迅速结束，它从秋天打到来年春天，然后又到了盛夏，还没有一点儿要停手的意思。		
