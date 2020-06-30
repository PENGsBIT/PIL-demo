# -*-coding:utf-8-*-
import os
import random

from PIL import Image, ImageDraw, ImageFont

from NameCrawler import randomName
from Resize import resize
import logging


def circleProfilePhoto(imgPath, outpath, imgName):
    # CMYK/RGBA 转换颜色格式（CMYK用于打印机的色彩，RGBA用于显示器的色彩）
    bacImg = Image.open('background.png').convert("RGBA")
    width = bacImg.size[0]
    height = bacImg.size[1]
    cir_path = outpath+'/'+imgName + '.png'
    ima = Image.open(imgPath).convert("RGBA")
    size = ima.size
    # print("photo size" + str(size))
    ima = resize(ima)
    size = ima.size
    # 因为是要圆形，所以需要正方形的图片
    r2 = min(size[0], size[1])
    if size[0] != size[1]:
        ima = ima.resize((r2, r2), Image.ANTIALIAS)
    # 最后生成圆的半径
    r3 = int(r2 / 2)
    imb = Image.new('RGBA', (r3 * 2, r3 * 2), (255, 255, 255, 0))
    pima = ima.load()  # 像素的访问对象
    pimb = imb.load()
    r = float(r2 / 2)  # 圆心横坐标

    for i in range(r2):
        for j in range(r2):
            lx = abs(i - r)  # 到圆心距离的横坐标
            ly = abs(j - r)  # 到圆心距离的纵坐标
            l = (pow(lx, 2) + pow(ly, 2)) ** 0.5  # 三角函数 半径
            if l < r3:
                pimb[i - (r - r3), j - (r - r3)] = pima[i, j]
    icon = imb
    # icon.show()
    r, g, b, a = icon.split()
    bacImg.paste(icon, (50, 190), mask=a)
    bacImg=drawTXT(bacImg)
    # bacImg.show()
    # 质量为85效果最好
    bacImg.save(cir_path, optimize=True, quality=85)

def drawTXT(bacImg):
    # add text
    userName = randomName()
    draw = ImageDraw.Draw(bacImg)
    # 文字大小
    word_size = 40
    # 黑体
    word_css = "C:\\Windows\\Fonts\\simhei.ttf"
    # 设置字体，如果没有，也可以不设置
    font = ImageFont.truetype(word_css, word_size)
    draw.text((270, 260), userName, (255, 255, 255), font=font)  # 设置位置坐标 文字 颜色 字体
    userName = "和卡HL002"+str(random.randint(3000, 9999))
    word_size = 35
    word_css = "C:\\Windows\\Fonts\\simhei.ttf"
    font = ImageFont.truetype(word_css, word_size)
    draw.text((270, 320), userName, (255, 255, 255), font=font)  # 设置位置坐标 文字 颜色 字体
    return bacImg
