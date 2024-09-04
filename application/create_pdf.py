import img2pdf
import os

# 将单个图像转换为PDF
# with open("output.pdf", "wb") as f:
#     f.write(img2pdf.convert("image.jpg"))

path = '../static/images'
images = [path + "/" + d for d in os.listdir(path) if
          os.path.isfile(path + "/" + d) and os.path.splitext(d)[1] == '.png']
print('图片列表  ==', images)
images.sort()
print('图片列表，重排序  ==', images)

# 将多个图像转换为PDF
with open("../static/人教版数学一年级上册预习卡.pdf", "wb") as f:
    img_pdf = img2pdf.convert(images)
    f.write(img_pdf)

