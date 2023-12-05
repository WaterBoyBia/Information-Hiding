import cv2
from blind_watermark import WaterMark
import os

os.chdir(os.path.dirname(__file__))
bwm = WaterMark(password_wm=1, password_img=1)
# 读取原图
bwm.read_img(filename='input/bg.png')
# 读取水印
bwm.read_wm('input/flag.jpg')
# 打上盲水印
bwm.embed('output/DWT_flag.png')
wm_shape = cv2.imread('input/flag.jpg', flags=cv2.IMREAD_GRAYSCALE).shape
print(wm_shape)

