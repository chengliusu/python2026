# 作者: 橙流苏
# 2026年08月04日15时35分03秒
# 强扭的瓜不甜，但解渴


import os


def seek_start():
    """
    相对于开头（文件起始位置）进行偏移
    :return:
    """
    file = open('file1', mode='r+', encoding='utf-8')
    # 相对于开头偏移5个字节，注意汉字的偏移是3的整数倍
    file.seek(5, os.SEEK_SET)

    # 从当前光标位置往后读取5个字符
    text = file.read(5)
    print(text)
    file.close()


# todo still unfinished
def seek_end():
    """
    相对于文件尾部进行偏移
    :return:
    """
    file = open('file1', mode='r+', encoding='utf-8')
    # seek(offset, whence)：相对于文件末尾偏移0个字节，已经到文件末尾，offset只能是0
    file.seek(0, os.SEEK_END)

    # 读取前五个字符(文本模式)或五个字节（二进制格式）
    text = file.read(5)                                     # 此时文件已经不能读到任何东西，输出的只有换行而已

    print(text)
    file.close()


def seek_cur():
    """
    相对于当前位置不动
    :return:
    """
    file = open('file1', mode='r+', encoding='utf-8')
    # file4.seek(offset, whence)：offset=0：偏移0字节
    # 从当前位置偏移0字节；光标位置不变，原地不动
    file.seek(0, os.SEEK_CUR)
    text = file.read(5)
    print(text)
    file.close()


def seek_b_cur():
    """
    在b模式下，读取到的是字节流，读取图片、音频、视频
    :return:
    """
    file = open('file1', mode='rb+')
    # 文本模式下offset只能为非负值，往后移；二进制模式下才可以往前偏，二进制模式下offset才能为负值
    file.seek(5, os.SEEK_CUR)
    file.seek(-2, os.SEEK_CUR)
    # file4.seek(-3, os.SEEK_END)
    b = file.read()
    print(b)
    file.close()


def copy_file():
    file1 = open('baidu.png', mode='rb+')
    file2 = open('baidu_copy.png', mode='wb')
    b = file1.read()
    file2.write(b)
    file1.close()
    file2.close()


if __name__ == '__main__':
    # seek_start()
    # seek_end()
    # seek_cur()
    # seek_b_cur()
    copy_file()
