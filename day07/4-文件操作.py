# 作者: 橙流苏
# 2026年08月04日15时07分52秒
# 强扭的瓜不甜，但解渴


def open_r():
    """
    读取文件
    :return:
    """
    # open('文件名', '访问方式', '编码方式')
    # r：以只读方式打开文件。文件的指针将会放在文件的开头，这是默认模式。如果文件不存在，将会抛出异常
    file = open('file2.txt', mode='r', encoding='utf-8')

    # 默认以字符串的方式读出
    text = file.read()
    print(text)

    # 每次打开以后会占用内存空间，要使用close关闭文件、释放空间
    file.close()


def open_rw():
    """
    读取文件，写文件
    :return:
    """
    # r+：以读写方式打开文件。文件的指针将会放在文件的开头。如果文件不存在，抛出异常（写入时，文件位置指针会跳转到尾部）
    file = open('file2.txt', mode='r+', encoding='utf-8')
    print(type(file))                                   # <class '_io.TextIOWrapper'>
    text = file.read()
    print(text)
    file.write('world')
    file.close()


def open_w():
    """
    练习w模式
    :return:
    """
    # w：以只写方式打开文件。如果文件存在会被覆盖。如果文件不存在，创建新文件。
    file = open('file3', mode='w', encoding='utf-8')
    print(type(file))                           # <class '_io.TextIOWrapper'>

    file.write('橙流苏不喜欢学习！')
    file.close()


def open_a():
    """
    练习a模式，每次写的时候写到文件末尾
    :return:
    """
    # a以追加方式打开文件。若文件存在，文件指针将会放在文件结尾。如果文件不存在，创建新文件进行写入。
    file = open('file1', mode='a', encoding='utf-8')
    file.write('流苏天下无敌！')
    file.close()


def use_readline():
    # 省略mode -> 默认mode='r'，只读文本模式
    file = open('file2.txt', encoding='utf-8')

    while True:
        text = file.readline()
        if not text:
            break
        # 每读取一行的末尾已经有了一个'/n'，故应将end=''
        print(text, end='')

    file.close()


if __name__ == '__main__':
    # open_r()
    # open_rw()
    # open_w()
    # open_a()
    use_readline()
