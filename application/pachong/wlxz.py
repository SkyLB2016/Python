import requests
from bs4 import BeautifulSoup


# 爬取 4小说 网站文本爬取
# url = "http://www.4xiaoshuo.info/188/188360/"
#
def get_content():
    # url = "http://www.4xiaoshuo.info/188/188360/"
    url = "http://www.4xiaoshuo.info/188/188619/"
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
    # print(chapters[3][1])
    # 打印结果
    for i, chapter in enumerate(chapters):
        print(f"Chapter {i + 1}: {chapter[0]} - {chapter[1]}")
        chapter.append(save_chapter(chapter[1]))

    # # 保存到文件
    output_file = "static/cjgm.txt"
    with open(output_file, 'w', encoding='utf-8') as f:
        for chapter in chapters:
            f.write(chapter[0])
            f.write(chapter[2])
            f.write("\n")


def save_chapter(url):
    # 发送HTTP请求
    response = requests.get(url)
    # if response.status_code == 200:
    response.raise_for_status()  # 检查请求是否成功
    # 解析HTML
    soup = BeautifulSoup(response.text, 'html.parser')
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
    return text_content
