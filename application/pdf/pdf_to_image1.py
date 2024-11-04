from pdf2image import convert_from_path

from application import tools


def convert_pdf_to_images1(pdf_path, output_folder):
    tools.check_path(output_folder)

    # 将PDF转换为图像列表
    pages = convert_from_path(pdf_path, dpi=300, first_page=1, last_page=None)
    # pages = convert_from_path(pdf_path)

    for i, page in enumerate(pages):
        # 保存图像到指定文件夹
        output_path = f"{output_folder}/{i + 1}.png"
        page.save(output_path, 'JPEG')
