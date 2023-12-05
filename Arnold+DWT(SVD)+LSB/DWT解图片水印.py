from blind_watermark import WaterMark

# 获取用户输入的两个数字
# num1 = int(input("水印的宽: "))
# num2 = int(input("水印的长: "))

num1 = 601
num2 = 601

# 将输入的数字转化为元组
wm_shape = (num1, num2)


# 解水印
bwm1 = WaterMark(password_wm=1, password_img=1)
# 注意需要设定水印的长宽wm_shape
bwm1.extract('output/DWT_flag.png', wm_shape=wm_shape, out_wm_name='output/wm_extracted.png', mode='img')
