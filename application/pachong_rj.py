import requests
from bs4 import BeautifulSoup
import os

from application import tools


# 爬取 人教版数学一年级上册预习卡 人教版一年级上册口算题卡
def download_images(url, save_folder='../../static/images'):
    # 确保保存图片的文件夹存在
    tools.check_path(save_folder)
    # 发送HTTP请求
    response = requests.get(url)
    if response.status_code == 200:
        # 解析HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        print("soup",soup)

        # 找到所有的<img>标签
        images = soup.find_all('img')
        print("images",images)
        img_count = 9
        # 遍历所有图片
        for img in images:
            # 提取图片链接
            img_src_url = img.get('src')
            print("img_src_url", img_src_url)
            data_src = img.get('data-src')
            print("data_src", data_src)
            # 简单的错误处理，跳过空链接或相对链接
            if data_src and 'http' in data_src:
                # 下载图片
                img_data = requests.get(data_src).content
                # 图片的本地保存路径
                file_name = os.path.join(save_folder, str(img_count) +".png")

                # 写入文件
                with open(file_name, 'wb') as handler:
                    handler.write(img_data)

                print(f'Saved {file_name}')
                img_count += 1
        print("img_count", img_count)


# 网站URL
url = "https://mp.weixin.qq.com/s/A4k3fSQEjTxgKhuq5E0fYw"
download_images(url)