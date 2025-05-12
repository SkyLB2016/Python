# -*- coding: utf-8 -*-
"""
@Time    : 2025/3/23 23:11
@Author  : 李彬
@Email   : your-email@example.com
@File    : image.py
@Description:
"""
import RealESRGAN
import cv2
import numpy as np
import torch
from PIL import ImageDraw
from PIL.Image import Image


def protect_number_repair(img_path):
    # 加载时保留Alpha通道（如果有数字水印区域标注）
    img = cv2.imread(img_path)
    h, w = img.shape[:2]

    # 手动划定数字区域（示例坐标需根据实际调整）
    number_roi = [(50, h - 100), (w - 50, h - 20)]  # 假设数字在底部中间区域

    # 创建保护蒙版
    mask = np.zeros(img.shape[:2], np.uint8)
    cv2.rectangle(mask, number_roi[0], number_roi[1], 255, -1)

    # 分区域修复：仅处理非数字区域
    damaged = cv2.bitwise_and(img, img, mask=~mask)
    repaired = cv2.inpaint(damaged, mask, 3, cv2.INPAINT_TELEA)

    # 合并保留区域
    final = cv2.bitwise_or(repaired, cv2.bitwise_and(img, img, mask=mask))
    return final



def ai_enhance(img_path):
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = RealESRGAN(device, scale=4)
    model.load_weights('weights/RealESRGAN_x4.pth')

    img = Image.open(img_path).convert('RGB')
    sr_img = model.predict(img)
    return sr_img