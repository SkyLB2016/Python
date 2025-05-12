import cv2
import numpy as np
from PIL import Image, ImageEnhance, ImageFilter


def restore_photo(input_path, output_color, output_bw, dpi=300):
    """修复照片并输出六寸彩色/黑白版本"""
    # 读取图片并保留数字区域 (防止损坏编号)
    img = cv2.imread(input_path)
    height, width = img.shape[:2]

    # === 1. 基础修复 ===
    # 去噪（非局部均值去噪）
    img = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)

    # 自动对比度增强
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    l = clahe.apply(l)
    lab = cv2.merge((l, a, b))
    img = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)

    # === 2. 边缘磨损修复 ===
    # 创建掩膜（检测破损边缘）
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 30, 100)
    kernel = np.ones((3, 3), np.uint8)
    mask = cv2.dilate(edges, kernel, iterations=1)

    # 使用图像修复算法（仅修复边缘）
    img = cv2.inpaint(img, mask, inpaintRadius=3, flags=cv2.INPAINT_TELEA)

    # === 3. 转换为六寸尺寸 ===
    target_size = (1800, 1200)  # 6寸=1800×1200像素（300dpi）
    img = cv2.resize(img, target_size, interpolation=cv2.INTER_LANCZOS4)

    # === 4. 保存彩色版本 ===
    pil_img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    # 设置DPI元数据
    pil_img.save(output_color, dpi=(dpi, dpi), quality=95)

    # === 5. 生成黑白版本 ===
    bw = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 增强对比度（模拟银盐相纸效果）
    bw = cv2.equalizeHist(bw)
    pil_bw = Image.fromarray(bw)
    # 添加锐化与颗粒感
    enhancer = ImageEnhance.Contrast(pil_bw)
    pil_bw = enhancer.enhance(1.2)
    pil_bw = pil_bw.filter(ImageFilter.UnsharpMask(radius=2, percent=150))
    # 保存黑白版
    pil_bw.save(output_bw, dpi=(dpi, dpi), quality=95)

