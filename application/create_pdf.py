import io

import img2pdf
import os

from PIL import Image

from application import tools


def create_pdf(image_path='static/pdf_images', save_path='static/pdf_new', file_name='人教版数学一年级上册预习卡'):
    """
    Description: 根据图片列表生成 pdf_new 文件，图片需要以数字命名
    * @param image_path 图片路径
    * @param save_path pdf保存路径
    * @param file_name pdf文件名
    """
    # 1.地址检查
    tools.check_path(save_path)
    # path = '../static/pdf_images'
    # 2.获取图片
    images = [
        image_path + "/" + file_str  # 最终返回
        for file_str in os.listdir(image_path)  # 循环
        if os.path.isfile(image_path + "/" + file_str) and os.path.splitext(file_str)[1] == '.png'  # 返回条件
    ]
    print('图片列表  ==', images)
    # 3.图片重排序，图片是数字名称，非数字会报错
    images.sort(key=lambda x: int(x.split('/')[-1].split('.')[0]))
    print('图片列表，重排序  ==', images)
    # pdf_images = sorted(pdf_images, key=lambda x: int(x.split('/')[-1].split('.')[0]))
    # print('图片列表，重排序  ==', pdf_images)

    # 文件路径
    file_path = save_path + '/' + file_name + '.pdf_new'
    # 4.将多个图像转换为PDF
    with open(file_path, "wb") as f:
        # img2pdf.AlphaChannelError: This function must not be called on pdf_images with alpha
        # 不能处理有 alpha 通道的图片
        f.write(img2pdf.convert(images))
        # 将单个图像转换为PDF
        # f.write(img2pdf.convert("image.jpg"))


def create_pdf_two(image_path='static/pdf_images', save_path='static/pdf_new', file_name=''):
    """
    Description: 根据图片列表生成多个正反 pdf_new 文件，图片需要以数字命名，并且根据奇偶分成两个数组，然后以10个为一组
    * @param image_path 图片路径
    * @param save_path pdf保存路径
    * @param file_name pdf文件名
    """
    # 1.地址检查
    tools.check_path(save_path)
    # 2.获取图片
    images = [
        image_path + "/" + file_str  # 最终返回
        for file_str in os.listdir(image_path)  # 循环
        if os.path.isfile(image_path + "/" + file_str) and os.path.splitext(file_str)[1] == '.png'  # 返回条件
    ]
    print('图片列表  ==', images)
    # 3.图片重排序，图片是数字名称，非数字会报错
    images.sort(key=lambda x: int(x.split('/')[-1].split('.')[0]))
    # pdf_images.sort(key=lambda x: int(x.split('/')[-1].split('.')[0].split('_')[1]))
    print('图片列表，重排序  ==', images)
    # pdf_images = sorted(pdf_images, key=lambda x: int(x.split('/')[-1].split('.')[0]))
    # print('图片列表，重排序  ==', pdf_images)

    # 4.间隔一个取出奇偶数组
    images_1 = images[::2]  # 从零开始，间隔一个，取出全部数据，取 下标为偶数 的所有数据
    images_2 = images[1::2]  # 从1开始，间隔一个，取出全部数据，取 下标为奇数 的所有数据
    print("images_1", len(images_1), images_1)
    print("images_2", len(images_2), images_2)

    # 5.按十个一组划分
    image_zheng = [images_1[i:i + 10] for i in range(0, len(images_1), 10)]
    image_fan = [images_2[i:i + 10] for i in range(0, len(images_2), 10)]
    # print("image_zheng", len(image_zheng), image_zheng)
    # print("image_fan", len(image_fan), image_fan)

    # 6.正面的PDF
    for i in range(0, len(image_zheng)):
        print("image_zheng", len(image_zheng[i]), image_zheng[i])
        file_path = save_path + '/' + file_name + str(i + 1) + '_正面.pdf_new'  # 正面文件路径
        with open(file_path, "wb") as f:
            f.write(img2pdf.convert(image_zheng[i]))

    # 7.反面PDF
    for i in range(0, len(image_fan)):
        print("image_fan", len(image_fan[i]), image_fan[i])
        file_path = save_path + '/' + file_name + str(i + 1) + '_反面.pdf_new'  # 反面面文件路径
        with open(file_path, "wb") as f:
            f.write(img2pdf.convert(image_fan[i]))


def create_pdf_interval_two(image_path='static/pdf_images', save_path='static/pdf_new', file_name=''):
    """
    Description: 根据图片列表生成正方面两个 pdf_new 文件，图片需要以数字命名，每页两张图片的打印方式
    * @param image_path 图片路径
    * @param save_path pdf保存路径
    * @param file_name pdf文件名
    """
    # 1.地址检查
    tools.check_path(save_path)
    # 2.获取图片
    images = [
        image_path + "/" + file_str  # 最终返回
        for file_str in os.listdir(image_path)  # 循环
        if os.path.isfile(image_path + "/" + file_str) and os.path.splitext(file_str)[1] == '.png'  # 返回条件
    ]
    print('图片列表  ==', images)
    # 3.图片重排序，图片是数字名称，非数字会报错
    images.sort(key=lambda x: int(x.split('/')[-1].split('.')[0]))
    # pdf_images.sort(key=lambda x: int(x.split('/')[-1].split('.')[0].split('_')[1]))
    print('图片列表，重排序  ==', images)
    # pdf_images = sorted(pdf_images, key=lambda x: int(x.split('/')[-1].split('.')[0]))
    # print('图片列表，重排序  ==', pdf_images)

    # 4.每组两个取出正反数组
    images_1 = []
    images_2 = []
    count = 0
    for i in range(0, len(images)):
        print(i)
        if count < 2:
            images_1.append(images[i])
        else:
            images_2.append(images[i])
        count += 1
        if count == 4:
            count = 0
    print("images_1", len(images_1), images_1)
    print("images_2", len(images_2), images_2)

    # 5.将多个图像转换为PDF
    file_path = save_path + '/' + file_name + '_正面.pdf_new'  # 正面文件路径
    with open(file_path, "wb") as f:
        f.write(img2pdf.convert(images_1))

    # 6.反面PDF
    file_path = save_path + '/' + file_name + '_反面.pdf_new'  # 反面面文件路径
    with open(file_path, "wb") as f:
        f.write(img2pdf.convert(images_2))


def create_pdf_alpha(image_path='static/pdf_images', save_path='static/pdf_new', file_name='人教版数学一年级上册预习卡'):
    tools.check_path(save_path)
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
    file_path = save_path + '/' + file_name + '.pdf_new'
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
