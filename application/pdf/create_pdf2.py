import os
from PIL import Image
from reportlab.lib.pagesizes import A3,A5
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
# 不好用
def create_pdf(file_name):
    image_path = f'static/pdf_images/{file_name}'
    save_path = f'static/pdf_new/{file_name}'
    # os.listdir('.')
    # 2.获取图片
    images = [
        image_path + "/" + file_str  # 最终返回
        for file_str in os.listdir(image_path)  # 循环
        if os.path.isfile(image_path + "/" + file_str) and os.path.splitext(file_str)[1] == '.png'  # 返回条件
    ]
    print('图片列表  ==', images)
    images.sort()
    print('图片列表，重排序  ==', images)
    AC=(A5[0],A5[1])
    # A3 = (297*mm,420*mm)

    # AC = (330*mm,480*mm)
    # AC = (370*mm,500*mm)

    # 创建一个新的PDF画布
    c = canvas.Canvas(f"{save_path}/{file_name}.pdf", pagesize=AC)

    # 打开图像并获取其尺寸
    image_path = image_path+'/1.png'
    image = Image.open(image_path)
    width, height = image.size

    # 计算图像在页面上的位置
    left_margin = (AC[0] - width) / 2
    bottom_margin = (AC[1] - height) / 2

    # 单个图片生成pdf
    # 将图像绘制到PDF画布上
    # # c.drawImage(image_path, left_margin, bottom_margin, width=width, height=height)
    # c.drawImage(image_path, 0, 0, width=width, height=height)
    # # # 保存PDF文件
    # c.showPage()

    # 多张图片生成pdf
    for img in images:
        im = Image.open(img)
        width, height = im.size
        print(img, width, height)
        # 计算图像在页面上的位置
        # c.drawImage(img, left_margin, bottom_margin, width=width, height=height)
        c.drawImage(img, 0, 0, width=width, height=height)
        c.showPage()
    c.save()
