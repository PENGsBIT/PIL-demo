# -*-coding:utf-8-*-
from PIL import Image
from resize import circleProfilePhoto

if __name__ == "__main__":
    inputpath = "./待处理图片"
    outpath = "./已处理好图片"
    circleProfilePhoto('1.jpg')

