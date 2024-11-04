import fitz  # PyMuPDF

from application import tools


def convert_pdf_to_images(pdf_file, out_path):
    """
    Description: 把 pdf 文件转成图片
    * @param pdf_file pdf_new 文件路径
    * @param out_path 图片保存路径
    """
    tools.check_path(out_path)
    # 1.打开PDF文件
    pdf_document = fitz.open(pdf_file)

    for page_number in range(len(pdf_document)):
        # 2.获取页面
        page = pdf_document[page_number]

        # 3.定义渲染的分辨率
        zoom_x = 2  # 水平缩放系数
        zoom_y = 2  # 垂直缩放系数
        mat = fitz.Matrix(zoom_x, zoom_y)  # 缩放系数

        # 4.渲染页面为图像
        pix = page.get_pixmap(matrix=mat, alpha=False)

        # 5.保存图像到指定文件夹
        pix.save(f"{out_path}/{page_number + 1}.png")
