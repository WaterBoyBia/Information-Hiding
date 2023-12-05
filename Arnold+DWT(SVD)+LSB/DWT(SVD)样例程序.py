import cv2
import numpy as np

def embed_watermark_svd_dwt(host_image_path, watermark_image_path, output_path, alpha_svd=0.1, alpha_dwt=0.1):
    # 读取主图像和水印图像
    host_image = cv2.imread(host_image_path)
    watermark_image = cv2.imread(watermark_image_path, cv2.IMREAD_GRAYSCALE)

    # 将水印图像调整为与主图像相同的大小
    watermark_image = cv2.resize(watermark_image, (host_image.shape[1], host_image.shape[0]))

    # 将水印图像进行奇异值分解
    U, S, Vt = np.linalg.svd(watermark_image, full_matrices=False)

    # 嵌入水印
    watermarked_U = U + alpha_svd * S[:, None] * Vt

    # 重构水印图像
    watermarked_image_svd = np.dot(watermarked_U, Vt)

    # 将水印图像进行小波变换
    host_image_YCrCb = cv2.cvtColor(host_image, cv2.COLOR_BGR2YCrCb)
    Y_channel = host_image_YCrCb[:,:,0]
    coeffs = cv2.dwt2(Y_channel, 'bior1.3')
    LL, (LH, HL, HH) = coeffs

    # 将SVD嵌入的水印进行DWT嵌入到LL子带
    LL += alpha_dwt * watermarked_image_svd

    # 将修改后的LL子带与其他子带重组
    coeffs_embedded = (LL, (LH, HL, HH))
    host_image_YCrCb[:,:,0] = cv2.idwt2(coeffs_embedded, 'bior1.3')

    # 将图像转回BGR格式
    watermarked_image = cv2.cvtColor(host_image_YCrCb, cv2.COLOR_YCrCb2BGR)

    # 保存水印嵌入后的图像
    cv2.imwrite(output_path, watermarked_image)

# 主程序
host_image_path = 'path/to/host_image.jpg'
watermark_image_path = 'path/to/watermark_image.png'
output_image_path = 'path/to/output_image.jpg'

# 嵌入水印
embed_watermark_svd_dwt(host_image_path, watermark_image_path, output_image_path)
