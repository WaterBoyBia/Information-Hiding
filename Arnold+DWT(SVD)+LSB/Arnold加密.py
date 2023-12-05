import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def arnold_encode(image, shuffle_times, a, b):
    """ Arnold shuffle for rgb image
    Args:
        image: input original rgb image
        shuffle_times: how many times to shuffle
    Returns:
        Arnold encode image
    """
    # 1:创建新图像
    arnold_image = np.zeros(shape=image.shape)

    # 2：计算N
    h, w = image.shape[0], image.shape[1]
    N = h   # 或N=w

    # 3：遍历像素坐标变换
    for time in range(shuffle_times):
        for ori_x in range(h):
            for ori_y in range(w):
                # 按照公式坐标变换
                new_x = (1 * ori_x + b * ori_y) % N
                new_y = (a * ori_x + (a * b + 1) * ori_y) % N

                # 将新坐标限制在图像范围内
                new_x = int((new_x + h) % h)
                new_y = int((new_y + w) % w)

                arnold_image[new_x, new_y, :] = image[ori_x, ori_y, :]

    return arnold_image

# 指定JPG文件路径
# input_image_path = input("输入图片名：")
input_image_path = "input/flag.jpg"

# 加载图像
original_image = np.array(Image.open(input_image_path))

# 设置Arnold置换参数
shuffle_times = int(input("输入打乱次数："))
a = int(input("输入参数1："))
b = int(input("输入参数2："))

# 对图像进行Arnold置换
arnold_encoded_image = arnold_encode(original_image, shuffle_times, a, b)

# 保存Arnold编码后的图像
# output_image_path = input("输入保存图片名：")
output_image_path = "output/Arn_flag.jpg"
Image.fromarray(arnold_encoded_image.astype(np.uint8)).save(output_image_path)
