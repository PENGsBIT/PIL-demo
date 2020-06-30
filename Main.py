# -*-coding:utf-8-*-
import os

from PIL import Image

from CircleProfilePhoto import circleProfilePhoto
from Resize import getResultArray

if __name__ == "__main__":
    inputpath = "./待处理图片"
    outpath = "./已处理好图片"
    for file in os.listdir(inputpath):
        if file:
            circleProfilePhoto(os.path.join(inputpath, file), outpath,file)
    # getResultArray()
