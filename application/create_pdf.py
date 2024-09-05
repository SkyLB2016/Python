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
    images.sort()
    print('图片列表，重排序  ==', images)

    # 文件路径
    file_path = save_path + '/' + file_name + '.pdf'
    # 将多个图像转换为PDF
    with open(file_path, "wb") as f:
        # img2pdf.AlphaChannelError: This function must not be called on images with alpha
        # 不能处理有 alpha 通道的图片
        f.write(img2pdf.convert(images))
        # 将单个图像转换为PDF
        # f.write(img2pdf.convert("image.jpg"))
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