import re
from tkinter import W
from tkinter.filedialog import SaveFileDialog
from scipy.io import wavfile
from scipy.fftpack import dct, idct, fft, fftfreq, ifft
# import pywt
import numpy as np
import matplotlib.pyplot as plt
import wave

def draw_time(path, filename):
    f = wave.open(path, 'rb')
    params = f.getparams()
    params = f.getparams()
    # 通道数、采样字节数、采样率、采样帧数
    nchannels, sampwidth, framerate, nframes = params[:4]
    voiceStrData = f.readframes(nframes)
    waveData = np.fromstring(voiceStrData, dtype=np.short)  # 将原始字符数据转换为整数
    # 音频数据归一化
    waveData = waveData * 1.0/max(abs(waveData))
    # 将音频信号规整乘每行一路通道信号的格式，即该矩阵一行为一个通道的采样点，共nchannels行
    waveData = np.reshape(waveData, [nframes, nchannels]).T  # .T 表示转置
    f.close()

    time = np.arange(0, nframes)*(1.0/framerate)
    plt.plot(time, waveData[0, :], c='b')
    plt.xlabel('time')
    plt.ylabel('am')
    plt.savefig('./%s.jpg' % filename)
    plt.show()

if __name__ == "__main__":
   

    alpha = 0.1
    block_size = 4
    # 1.数据读取
    samplerate_wm, data_wm = wavfile.read("flag.wav")
    # data_wm = np.where(data_wm < np.mean(data_wm),0, 1)  # watermark进行(归一化的)二值化
    samplerate_bg, data_bg = wavfile.read("carrier.wav")
    #若无法平均分块，也就是说数组大小不是块的大小的整数倍，给数组后面加适当的零，使其变成块大小的整数倍
    if((np.shape(data_bg)[0] % block_size) != 0):
        data_bg = np.r_[data_bg, np.zeros(
            block_size-(np.shape(data_bg)[0] % block_size))]
    #在单声道和双声道的处理上有所不同，将单声道音频转为双声道，方便统一处理
    if(data_bg.ndim == 1):
        a = np.array(np.zeros(data_bg.shape[0])).T
        data_bg = np.c_[np.array([data_bg]).T, a]
    print(np.shape(data_wm), np.shape(data_bg))

    
    draw_time("flag.wav","flag")
    draw_time("flag_ext","flag_ext")
    draw_time("carrier.wav","carrier")
    draw_time("result.wav","result")