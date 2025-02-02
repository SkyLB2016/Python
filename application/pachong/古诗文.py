import asyncio

import aiohttp
import requests
from bs4 import BeautifulSoup


# 古诗文网站文本爬取
def get_content():
    # 爬取的网址 以及 文件名

    url = "https://www.gushiwen.cn/gushi/tangshi.aspx"
    file_name = "唐诗三百首"
    asyncio.run(get_chapter_list(url, file_name))
    # 古诗三百
    asyncio.run(get_chapter_list("https://www.gushiwen.cn/gushi/sanbai.aspx"))
    # 宋词三百
    asyncio.run(get_chapter_list("https://www.gushiwen.cn/gushi/songsan.aspx"))

    url = "https://www.gushiwen.cn/gushi/xiaoxue.aspx"
    file_name = "小学古诗文"
    asyncio.run(get_chapter_list(url, file_name))
    # 初中古诗文
    asyncio.run(get_chapter_list("https://www.gushiwen.cn/gushi/chuzhong.aspx"))
    # 高中古诗文
    asyncio.run(get_chapter_list("https://www.gushiwen.cn/gushi/gaozhong.aspx"))
    # 小学文言文
    asyncio.run(get_chapter_list("https://www.gushiwen.cn/wenyan/xiaowen.aspx"))
    # 初中文言文
    asyncio.run(get_chapter_list("https://www.gushiwen.cn/wenyan/chuwen.aspx"))
    # 高中文言文
    asyncio.run(get_chapter_list("https://www.gushiwen.cn/wenyan/gaowen.aspx"))
    # 诗经
    asyncio.run(get_chapter_list("https://www.gushiwen.cn/gushi/shijing.aspx"))
    # asyncio.run(get_chapter_list(""))


async def get_chapter_list(url='', file_name=''):
    # 爬取的网址 以及 文件名
    # url = "https://www.gushiwen.cn/gushi/xiaoxue.aspx"
    # file_name = "小学古诗文"
    # url = "https://www.gushiwen.cn/gushi/tangshi.aspx"
    # file_name = "唐诗三百首"

    # 发送HTTP请求
    response = requests.get(url)
    # if response.status_code == 200:
    response.raise_for_status()  # 检查请求是否成功

    # 解析HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    # print("soup", soup)
    file_name = soup.find('h1').text.strip()
    print(file_name)

    # 输出地址
    output_file = f"static/txt/{file_name}.txt"

    # 查找目录列表
    # chapter_list = soup.find('div', class_='sons').find('div', class_='typecont')
    # print("chapter_list",chapter_list)
    # chapter_list = soup.find('div', class_='sons').find_all('div',class_='typecont')
    # print("chapter_list",chapter_list[0])
    # print("chapter_list",chapter_list[1])
    # for chapter in chapter_list:
    #     print(chapter)
    chapter_list = soup.find('div', class_='sons').find_all('a')
    # print("chapter_list",chapter_list)

    # 存储章节信息
    chapters = []

    for chapter in chapter_list:
        chapter_name = chapter.text.strip()
        if 'href' not in chapter.attrs:
            chapters.append([chapter_name, ""])
            continue
        chapter_url = 'https://www.gushiwen.cn' + chapter['href']
        chapters.append([chapter_name, chapter_url])
    # chapters = chapters[:1]
    # 限制并发数量
    semaphore = asyncio.Semaphore(10)  # 限制最多同时10个请求

    async with aiohttp.ClientSession() as session:
        tasks = []
        for i, chapter in enumerate(chapters):
            # print(f"Chapter {i + 1}: {chapter[0]} - {chapter[1]}")
            tasks.append(asyncio.create_task(get_chapter(semaphore, session, i, chapter[0], chapter[1])))
        results = await asyncio.gather(*tasks)
    # print(results)
    num = len(results)
    print("异步任务个数", num)
    # 保存到文件
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(file_name)
        f.write("\n")
        f.write(str(num)+'首')
        f.write("\n\n\n")
        for i, chapter in enumerate(results):
            # f.write(chapter[1])
            f.write(str(i + 1) + "、")
            f.write(chapter[2])
            f.write("\n")
            f.write("\n")
    #
    # lines = []
    # with open(output_file, 'r') as f:
    #     lines = f.readlines()
    # print('行数  ', len(lines))
    # with open(output_file, 'w', encoding='utf-8') as f:
    #     for line in lines:
    #         f.write('#    ' + line)


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
                    # title = soup.find('h1').text.strip()
                    # print(title)
                    content_div = soup.find('div', id='sonsyuanwen', class_='sons').find('div', class_='cont')
                    text_content = content_div.get_text(strip=True, separator='\n')
                    # print(text_content)

                    # # # 查找目录列表
                    # content_div = soup.find('div', id='sonsyuanwen', class_='sons')
                    # # print(content_div)
                    # content_div = content_div.find('div', id='zhengwenef9cd9ba44bb')
                    # # print(content_div)
                    # text_content = content_div.get_text(strip=True, separator='\n')
                    # # text_content = content_div.get_text()
                    # print(text_content)
                    return index, name, text_content
                else:
                    print("response.status==", response.status)
                    print(f"失败{name}; {url}:status:{response.status}")
                    return index, name, f"{name}\n获取失败"

        except Exception as e:
            print(f"失败：{name}; {url}: {e}")
            return index, name, f"{name}\n获取失败"
        # finally:semaphore
        #