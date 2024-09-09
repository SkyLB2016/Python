import fitz  # PyMuPDF

from application import tools


def convert_pdf_to_images(pdf_path, output_folder):
    tools.check_path(output_folder)
    # 打开PDF文件
    pdf_document = fitz.open(pdf_path)

    for page_number in range(len(pdf_document)):
        # 获取页面
        page = pdf_document[page_number]

        # 定义渲染的分辨率
        zoom_x = 2  # 水平缩放系数
        zoom_y = 2  # 垂直缩放系数
        mat = fitz.Matrix(zoom_x, zoom_y)  # 缩放系数

        # 渲染页面为图像
        pix = page.get_pixmap(matrix=mat, alpha=False)

        # 保存图像到指定文件夹
        output_path = f"{output_folder}/{page_number + 1}.png"
        pix.save(output_path)
