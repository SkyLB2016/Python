import io

import requests
from PIL import Image
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
        # print("soup", soup)

        # 找到所有的<img>标签
        images = soup.find_all('img')
        print("img标签的数量", len(images))
        img_count = 9
        # 遍历所有图片
        for img in images:
            # 提取图片链接
            # img_src_url = img.get('src')
            # print("img_src_url", img_src_url)
            data_src = img.get('data-src')
            print("data_src", data_src)
            # 简单的错误处理，跳过空链接或相对链接
            if data_src and 'https' in data_src:
                # 下载 获取图片数据
                img_data = requests.get(data_src).content

                # 第一种方法：转成图片再保存
                # 使用io.BytesIO将bytes数据转换为文件对象
                # image_stream = io.BytesIO(img_data)
                # # 使用Pillow的Image.open()函数从文件对象中加载图片
                # image = Image.open(image_stream)
                # if image.format != 'PNG':
                #     continue
                # 图片的本地保存路径
                # file_name = os.path.join(save_folder, str(img_count) + ".png")
                # image.save(file_name)

                # 第二种方法：直接把 bytes 数组 img_data 写入文件中
                file_name = os.path.join(save_folder, str(img_count) + ".png")
                with open(file_name, 'wb') as handler:
                    handler.write(img_data)
                print(f'Saved {file_name}')
                img_count += 1
        print("img_count", img_count)

# 网站URL
# url = "https://mp.weixin.qq.com/s/A4k3fSQEjTxgKhuq5E0fYw"
# download_images(url, save_folder='../../static/images')
