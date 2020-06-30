# -*-coding:utf-8-*-
import numpy as np
from PIL import Image
from scipy import misc


def resize(img):
    # img = Image.open(cirFileName)
    # w, h = img.size
    # # 去掉浮点，防报错
    # w, h = round(w * 0.2), round(h * 0.2)
    img = img.resize((200, 200), Image.ANTIALIAS).convert("RGBA")
    return img


def getResultArray():
    fileName = "1.png"
    imgBeforeExpand = misc.imread(fileName, flatten=False, mode='YCbCr')
    imgBeforeExpand = imgBeforeExpand / 255.0
    # imgBeforeExpand = np.uint8(imgBeforeExpand*255)
    # h, w = imgBeforeExpand.shape[:2]
    # print(imgBeforeExpand.shape)
    h = 150
    w = 160
    data = list()
    data.append(misc.imresize(imgBeforeExpand[:, :, 0], [h, w], 'bicubic', mode="F")[:, :, None])
    data.append(misc.imresize(imgBeforeExpand[:, :, 1], [h, w], 'bicubic', mode="F")[:, :, None])
    data.append(misc.imresize(imgBeforeExpand[:, :, 2], [h, w], 'bicubic', mode="F")[:, :, None])
    data_out = np.concatenate(data, axis=2)
    data_out[data_out > 1] = 1.0
    data_out = np.uint8(data_out * 255)
    img = misc.toimage(arr=data_out, mode="YCbCr")
    return img
