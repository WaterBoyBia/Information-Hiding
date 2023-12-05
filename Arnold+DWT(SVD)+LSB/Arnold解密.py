import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def arnold_decode(image, shuffle_times, a, b):
    """ decode for rgb image that encoded by Arnold
    Args:
        image: rgb image encoded by Arnold
        shuffle_times: how many times to shuffle
    Returns:
        decode image
    """
    # 1:创建新图像
    decode_image = np.zeros(shape=image.shape)
    
    # 2：计算N
    h, w = image.shape[0], image.shape[1]
    N = h # 或N=w
    
    # 3：遍历像素坐标变换
    for time in range(shuffle_times):
        for ori_x in range(h):
            for ori_y in range(w):
                # 按照公式坐标变换
                new_x = ((a*b+1)*ori_x + (-b)* ori_y)% N
                new_y = ((-a)*ori_x + ori_y) % N
                #黑白水印提取
                decode_image[new_x, new_y] = image[ori_x, ori_y]
                #彩色水印提取
                # decode_image[new_x, new_y,:] = image[ori_x, ori_y,:]
    return decode_image


# 指定JPG文件路径
input_image_path = input("输入图片名：")

# 加载图像
original_image = np.array(Image.open(input_image_path))

# 设置Arnold置换参数
shuffle_times = int(input("输入打乱次数："))
a = int(input("输入参数1："))
b = int(input("输入参数2："))

# 对图像进行Arnold置换
arnold_encoded_image = arnold_decode(original_image, shuffle_times, a, b)

# 保存Arnold编码后的图像
output_image_path = input("输入保存图片名：")
Image.fromarray(arnold_encoded_image.astype(np.uint8)).save(output_image_path)
