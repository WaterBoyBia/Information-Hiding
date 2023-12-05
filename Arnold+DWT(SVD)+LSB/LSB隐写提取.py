import numpy as np
import PIL.Image as Image



def lsb_embed(pic_src,file_src,num):
    # 读取图片的像素信息
    picture = Image.open('{}'.format(pic_src))
    pic_data = np.array(picture)

    # 读取要隐写的文件
    with open('{}'.format(file_src), encoding="utf-8") as file:
        secrets = file.read()

    # 将图片拷贝一份，作为最终的图片数据
    im_data = np.array(picture.copy()).ravel().tolist()

    def cover_lsb(bin_index, data):
       
        res = []
        for i in range(8):
            data_i_bin = bin(data[i])[2:].zfill(8)
            if bin_index[i] == '0':
                data_i_bin = data_i_bin[0:7] + '0'
            elif bin_index[i] == '1':
                data_i_bin = data_i_bin[0:7] + '1'
            res.append(int(data_i_bin, 2))
        return res

    pic_idx = 0
    # 采用LSB隐写技术，横向取数据，每次取9个数据，改变8个像素最低位
    res_data = []
    for i in range(len(secrets)):
        # 拿到隐写文件的字符ascii数值, 并转换为二进制,填充成八位
        index = ord(secrets[i])
        bin_index = bin(index)[2:].zfill(8)
        # 对数据进行LSB隐写，替换操作
        res = cover_lsb(bin_index, im_data[pic_idx * 8: (pic_idx + 1) * 8])
        pic_idx += 1
        res_data += res
    # 对剩余未填充的数据进行补充填充，防止图像无法恢复
    res_data += im_data[pic_idx * 8:]

    # 将新生成的文件进行格式转换并保存，此处一定保存为压缩的png文件
    new_im_data = np.array(res_data).astype(np.uint8).reshape((pic_data.shape))
    res_im = Image.fromarray(new_im_data)
    res_im.save(f'output/LSB_DWT_Arn_flag.png')
    print(f"已生成隐写结果output/LSB_DWT_Arn_flag.png")

def lsb_extract(pic_src,file_src,num):
    # 打开隐写文件
    picture = Image.open('{}'.format(pic_src))
    pic_datas = np.array(picture).ravel().tolist()

    str_len = int(file_src)
    # print('字符的长度为：', str_len)

    # 将图片拷贝一份，作为最终的图片数据
    im_data = np.array(picture.copy()).ravel().tolist()

    def lsb_decode(data):
        '''
        :param bin_index:  当前字符的ascii的二进制
        :param data: 取出数组像素的八个数值
        :return: LSB隐写后的字符
        '''
        str = ''
        for i in range(len(data)):
            # print(bin(data[i])[2:])
            data_i_bin = bin(data[i])[2:][-1]
            str += data_i_bin
        return str

    pic_idx = 0
    # 采用LSB隐写技术，横向取数据，每次取9个数据，改变8个像素最低位
    res_data = []

    for i in range(str_len):
        # 拿到第i个数据,转换成二进制
        data = im_data[i * 8: (i + 1) * 8]
        data_int = lsb_decode(data)
        # 找到最低位
        res_data.append(int(data_int, 2))

    # 将二进制数据转换成ASCII
    str_data = ''
    for i in res_data:
        temp = chr(i)
        str_data += temp
    print(f"提取成功，输出下列解密结果{num}")
    print(str_data)
    print()
    # with open('secret_out.txt', 'w',encoding="utf-8") as file:
    #     file.write(str_data)
    # print('已保存在secret_out.txt中')


if __name__ == '__main__':
    while True:
        choice = input("请输入数字选择功能：1.隐写 2.提取 3.退出 ：")
        if choice=='1':

            # img_src = input("输入要隐写的图片名：")
            # file_src = input("输入隐写的内容文件名：")

            img_src = "output/DWT_Arn_flag.png"
            file_src = "input/Keys.txt"

            lsb_embed(img_src,file_src,1)


        elif choice=='2':
            img_src = input("输入要提取的图片名：")
            file_src = input('请输入信息长度：')

            lsb_extract(img_src,file_src,1)

        else:
            break

