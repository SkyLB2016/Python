import fitz  # PyMuPDF

from application import tools


def convert_pdf_to_images(pdf_file, out_path, offset=1, zoom_x=2.0, zoom_y=2.0):
    """
    Description: 把 pdf 文件转成图片
    * @param pdf_file pdf_new 文件路径
    * @param out_path 图片保存路径
    * @param offset 文件后缀开始位置（拆解多个pdf文件时的时候会用到）
    * @param zoom_x = 2  # 水平缩放系数
    * @param zoom_y = 2  # 垂直缩放系数
    """
    tools.check_path(out_path)
    # 1.打开PDF文件
    pdf_document = fitz.open(pdf_file)
    index = 0
    for page_number in range(len(pdf_document)):
        # 2.获取页面
        page = pdf_document[page_number]

        # 3.定义渲染的分辨率
        mat = fitz.Matrix(zoom_x, zoom_y)  # 缩放系数

        # 4.渲染页面为图像
        pix = page.get_pixmap(matrix=mat, alpha=False)

        # 5.保存图像到指定文件夹
        index = page_number + offset
        pix.save(f"{out_path}/{index}.png")
    return index


def convert_pdf_to_mat(pdf_file, out_path, offset=1):
    """
    Description: 把 pdf 文件转成图片
    * @param pdf_file pdf_new 文件路径
    * @param out_path 图片保存路径
    * @param offset 文件后缀开始位置（拆解多个pdf文件时的时候会用到）
    """
    return convert_pdf_to_images(pdf_file, out_path, offset=offset, zoom_x=1.4, zoom_y=1.4)


def convert_a4_to_a5(pdf_file, out_path, offset=1):
    """
    Description: 把 pdf 文件转成图片
    * @param pdf_file pdf_new 文件路径
    * @param out_path 图片保存路径
    * @param offset 文件后缀开始位置（拆解多个pdf文件时的时候会用到）
    """
    tools.check_path(out_path)
    # 1.打开PDF文件
    pdf_document = fitz.open(pdf_file)
    index = 0
    for page_number in range(len(pdf_document)):
        # 2.获取页面
        page = pdf_document[page_number]
        a4 = [595.28, 841.89]
        a5 = [420.94, 595.28]
        # 3.定义渲染的分辨率
        zoom_x = a5[0] / a4[0]  # 水平缩放系数
        zoom_y = a5[0] / a4[0]  # 垂直缩放系数
        mat = fitz.Matrix(zoom_x, zoom_y)  # 缩放系数

        # 4.渲染页面为图像
        pix = page.get_pixmap(matrix=mat, alpha=False)

        # 5.保存图像到指定文件夹
        index = page_number + offset
        pix.save(f"{out_path}/{index}.png")
    return index
