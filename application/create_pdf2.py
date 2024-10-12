import os
from PIL import Image
from reportlab.lib.pagesizes import A3
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas

def create_pdf():
    path = '../static/pdf_images'
    # os.listdir('.')
    images = [path + "/" + d for d in os.listdir(path) if
              os.path.isfile(path + "/" + d) and os.path.splitext(d)[1] == '.png']
    print('图片列表  ==', images)
    images.sort()
    print('图片列表，重排序  ==', images)
    # AC=(A3[0],A3[1])
    # A3 = (297*mm,420*mm)

    # AC = (330*mm,480*mm)
    AC = (370*mm,500*mm)

    # 创建一个新的PDF画布
    c = canvas.Canvas("../static/output.pdf_new", pagesize=AC)

    # 打开图像并获取其尺寸
    image_path = '../static/pdf_images/10.png'
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
