import io
import shutil

import img2pdf
import os

from PIL import Image

from application import tools
from application.pdf import pdf_to_image


def create_pdf(file_name):
    """
    Description: 根据图片列表生成一个 pdf_new 文件，图片需要以数字命名
    * @param image_path 图片路径
    * @param save_path pdf保存路径
    * @param file_name pdf文件名
    """
    image_path = f'static/pdf_images/{file_name}'
    save_path = f'static/pdf_new/{file_name}'
    file_name = file_name
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
    file_path = save_path + '/' + file_name + '.pdf'
    # 4.将多个图像转换为PDF
    with open(file_path, "wb") as f:
        # img2pdf.AlphaChannelError: This function must not be called on pdf_images with alpha
        # 不能处理有 alpha 通道的图片
        f.write(img2pdf.convert(images))
        # 将单个图像转换为PDF
        # f.write(img2pdf.convert("image.jpg"))


# def create_pdf_two(image_path, save_path, file_name, group=10):
def create_pdf_two(image_path, save_path, file_name, type_mode=1, group=20):
    """
    Description: 课本模式：根据图片列表生成多个正反 pdf_new 文件，图片需要以数字命名，并且根据奇偶分成两个数组，然后以10个为一组
    * @param image_path 图片路径
    * @param save_path pdf保存路径
    * @param file_name pdf文件名
    * @param type_mode 1课本模式（反正面共两页），2试卷模式（反正面共四页）
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

    # 4.根据 type_mode 选择模式
    if type_mode == 1:
        # 课本模式：一张两页，正方各一页，十个一组，一个存正面，一个存反面
        images_1 = images[::2]  # 从零开始，间隔一个，取出全部数据，取 下标为偶数 的所有数据
        images_2 = images[1::2]  # 从1开始，间隔一个，取出全部数据，取 下标为奇数 的所有数据
        print("images_1", len(images_1), images_1)
        print("images_2", len(images_2), images_2)
    else:
        # 试卷模式：一张四页，正反各两页，十个一组，一个存正面，一个存反面
        images_1 = []
        images_2 = []
        count = 0
        for i in range(0, len(images)):
            # print(i)
            if count < 2:
                images_1.append(images[i])
            else:
                images_2.append(images[i])
            count += 1
            if count == 4:
                count = 0
        print("images_1", len(images_1), images_1)
        print("images_2", len(images_2), images_2)

    # 5.按十个一组划分
    image_zheng = [images_1[i:i + group] for i in range(0, len(images_1), group)]
    image_fan = [images_2[i:i + group] for i in range(0, len(images_2), group)]

    # 6.正面的PDF
    for i in range(0, len(image_zheng)):
        print(f"image_zheng：正面第{i + 1}个", len(image_zheng[i]), image_zheng[i])
        file_path = f"{save_path}/{file_name}_{i + 1}_正面.pdf"  # 正面文件路径
        with open(file_path, "wb") as f:
            f.write(img2pdf.convert(image_zheng[i]))

    # 7.反面PDF
    for i in range(0, len(image_fan)):
        print(f"image_fan：反面第{i + 1}个", len(image_fan[i]), image_fan[i])
        file_path = f"{save_path}/{file_name}_{i + 1}_反面.pdf"  # 反面文件路径
        with open(file_path, "wb") as f:
            f.write(img2pdf.convert(image_fan[i]))


def create_pdf_two1(image_path, save_path, file_name, group=10):
    """
    Description: 试卷模式：根据图片列表生成多个正反 pdf_new 文件，图片需要以数字命名，每页两张图片的打印方式，然后以10个为一组
    例如：有 12345678 八页分为 1256，3478 两组
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
        # print(i)
        if count < 2:
            images_1.append(images[i])
        else:
            images_2.append(images[i])
        count += 1
        if count == 4:
            count = 0
    print("images_1", len(images_1), images_1)
    print("images_2", len(images_2), images_2)

    # 5.按十个一组划分
    image_zheng = [images_1[i:i + group] for i in range(0, len(images_1), group)]
    image_fan = [images_2[i:i + group] for i in range(0, len(images_2), group)]

    # 6.正面的PDF
    for i in range(0, len(image_zheng)):
        print(f"image_zheng：正面第{i + 1}个", len(image_zheng[i]), image_zheng[i])
        file_path = save_path + '/' + file_name + str(i + 1) + '_正面.pdf'  # 正面文件路径
        with open(file_path, "wb") as f:
            f.write(img2pdf.convert(image_zheng[i]))

    # 7.反面PDF
    for i in range(0, len(image_fan)):
        print(f"image_fan：反面第{i + 1}个", len(image_fan[i]), image_fan[i])
        file_path = save_path + '/' + file_name + str(i + 1) + '_反面.pdf'  # 反面面文件路径
        with open(file_path, "wb") as f:
            f.write(img2pdf.convert(image_fan[i]))


def check_path(path):
    if not os.path.exists(path):
        os.makedirs(path)
    return path


def move_file():
    dir_path = 'static/pdf_old'
    list_file = [
        dir_path + "/" + file_str
        for file_str in os.listdir(dir_path)
        if os.path.isfile(dir_path + "/" + file_str) and os.path.splitext(file_str)[1] == '.pdf'
    ]
    # print(list_file)
    print(len(list_file))
    # 是否需要移动兵筛选
    dir_path_1 = check_path('static/pdf_old/答案')
    dir_path_2 = check_path('static/pdf_old/正文')
    # shutil.rmtree('static/pdf_old/答案')
    for file in list_file:
        if file.__contains__('答案'):
            # shutil.copy(file, dir_path_1)
            shutil.move(file, dir_path_1)
        else:
            # shutil.copy(file, dir_path_2)
            shutil.move(file, dir_path_2)
        print(file)


def many_file():
    # move_file()
    # pdf 转图片
    # dir_path = 'static/pdf_old/正文'
    # list_file = [
    #     dir_path + "/" + file_str
    #     for file_str in os.listdir(dir_path)
    #     if os.path.isfile(dir_path + "/" + file_str) and os.path.splitext(file_str)[1] == '.pdf'
    # ]
    # print(len(list_file))
    # list_file.sort()
    # index = 0
    # list_file_1 = list_file[6:]
    # list_file_2 = list_file[:6]
    # out_path = 'static/pdf_images/正文'
    # for file in list_file_1:
    #     print(file)
    #     index = pdf_to_image.convert_pdf_to_images(file, out_path, index + 1)
    #     print(index)
    # for file in list_file_2:
    #     print(file)
    #     index = pdf_to_image.convert_pdf_to_images(file, out_path, index + 1)
    #     print(index)

    image_path = 'static/pdf_images/正文'
    save_path = 'static/pdf_new/阅读'
    # type_mode，1课本模式，2试卷模式
    create_pdf_two(image_path, save_path, "寒假阅读理解", 1)


def main():
    file_name = '一（下）语文高频考点通关密卷'
    # pdf_to_img(file_name)
    image_to_pdf(file_name, 2)

    # file_name = '一年级数学下册人教版25春'
    # pdf_to_img(file_name)
    # type_mode，1课本模式，2试卷模式
    # image_to_pdf(file_name, 2)
    # image_to_pdf(file_name, 2,group=40)
    # 生成一个pdf
    # create_pdf(file_name)


def pdf_to_img(file_name):
    # 1.pdf_new 转成图片
    print("pdf文件拆分成图片")
    pdf_file = f'static/pdf_old/{file_name}.pdf'
    out_path = f'static/pdf_images/{file_name}'
    pdf_to_image.convert_pdf_to_images(pdf_file, out_path)
    # pdf_to_image.convert_a4_to_a5(pdf_file, out_path)


#
def image_to_pdf(file_name, type_mode=1, group=20):
    # 图片路径，
    image_path = f'static/pdf_images/{file_name}'
    # 保存路径
    save_path = f'static/pdf_new/{file_name}'
    # 2.图片生成一个pdf
    # create_pdf(file_name)

    # 2.图片生成正方多个个pdf
    create_pdf_two(image_path, save_path, file_name, type_mode, group)
