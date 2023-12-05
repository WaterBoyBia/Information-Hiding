# 文件说明

**/audio_in/result.wav**

载体音频

**/audio_out/result_stego.wav**

隐写了DCT参数的音频

**audioload.m**

音频加载函数

**audiosave.m**

音频保存函数

**echo_dec.m**

提取函数

**echo_enc_single.m**

嵌入函数

**getBits.m**

获取文本比特

**mixer.m**

将回声和原音频混合

**conf.txt**

DCT参数

**data_embedding.m**

将数据嵌入音频

**data_extracting.m**

将数据从音频中提取

# 解密可能需要的参数

length of frames = 4*1024

delay rate for bit0 = 150

delay rate for bit1 = 200

loength of conf.txt = 881176