import io

import img2pdf
import os

from PIL import Image

from application import tools


def create_pdf(image_path='static/images', save_path='static/pdf', file_name='人教版数学一年级上册预习卡'):
    tools.check_path(save_path)
    # path = '../static/images'
    images = [
        image_path + "/" + file_str  # 最终返回
        for file_str in os.listdir(image_path)  # 循环
        if os.path.isfile(image_path + "/" + file_str) and os.path.splitext(file_str)[1] == '.png'  # 返回条件
    ]
    print('图片列表  ==', images)
    images.sort(key=lambda x: int(x.split('/')[-1].split('.')[0]))
    print('图片列表，重排序  ==', images)
    # images = sorted(images, key=lambda x: int(x.split('/')[-1].split('.')[0]))
    # print('图片列表，重排序  ==', images)

    # 文件路径
    file_path = save_path + '/' + file_name + '.pdf'
    # 将多个图像转换为PDF
    with open(file_path, "wb") as f:
        # img2pdf.AlphaChannelError: This function must not be called on images with alpha
        # 不能处理有 alpha 通道的图片
        f.write(img2pdf.convert(images))
        # 将单个图像转换为PDF
        # f.write(img2pdf.convert("image.jpg"))


def create_pdf_interval(image_path='static/images', save_path='static/pdf', file_name=''):
    tools.check_path(save_path)
    # path = '../static/images'
    images = [
        image_path + "/" + file_str  # 最终返回
        for file_str in os.listdir(image_path)  # 循环
        if os.path.isfile(image_path + "/" + file_str) and os.path.splitext(file_str)[1] == '.png'  # 返回条件
    ]
    print('图片列表  ==', images)
    images.sort(key=lambda x: int(x.split('/')[-1].split('.')[0]))
    # images.sort(key=lambda x: int(x.split('/')[-1].split('.')[0].split('_')[1]))
    print('图片列表，重排序  ==', images)
    # images = sorted(images, key=lambda x: int(x.split('/')[-1].split('.')[0]))
    # print('图片列表，重排序  ==', images)

    images_1 = images[::2]  # 从零开始，间隔一个，取出全部数据，取 下标为偶数 的所有数据
    images_2 = images[1::2]  # 从1开始，间隔一个，取出全部数据，取 下标为奇数 的所有数据
    print("images_1", len(images_1), images_1)
    print("images_2", len(images_2), images_2)

    # 文件路径
    file_path = save_path + '/' + file_name + '_正面.pdf'
    # 将多个图像转换为PDF
    with open(file_path, "wb") as f:
        f.write(img2pdf.convert(images_1))

    file_path = save_path + '/' + file_name + '_反面.pdf'
    # 将多个图像转换为PDF
    with open(file_path, "wb") as f:
        f.write(img2pdf.convert(images_2))


def create_pdf_alpha(image_path='static/images', save_path='static/pdf', file_name='人教版数学一年级上册预习卡'):
    tools.check_path(save_path)
    # path = '../static/images'
    images = [
        image_path + "/" + file_str  # 最终返回
        for file_str in os.listdir(image_path)  # 循环
        if os.path.isfile(image_path + "/" + file_str) and os.path.splitext(file_str)[1] == '.png'  # 返回条件
    ]
    print('图片列表  ==', images)
    images.sort()
    print('图片列表，重排序  ==', images)

    for img in images:
        process_image(img)
    # 文件路径
    file_path = save_path + '/' + file_name + '.pdf'
    # 将多个图像转换为PDF
    with open(file_path, "wb") as f:
        f.write(img2pdf.convert(images))


def process_image(image_path):
    image = Image.open(image_path)
    if image.mode == 'RGBA':
        # 有 alpha 通道的重新处理一下图片
        # 使用BytesIO将图片保存为bytes
        image_stream = io.BytesIO()
        image.save(image_stream, format='PNG')  # 或者其他格式，如'PNG'
        image_bytes = image_stream.getvalue()
        image_stream = io.BytesIO(image_bytes)
        image = Image.open(image_stream)
        image.save(image_path)
        print(image_path)
        # image.show()
