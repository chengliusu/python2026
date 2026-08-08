# 作者: 橙流苏
# 2026年07月24日23时33分56秒
# 强扭的瓜不甜，但解渴


def check_type():
    """
    判断字符串类型
    :return:
    """
    s1 = 'abc*'
    print(s1.isalnum())     # False
    s2 = '123'
    print(s2.isdecimal())       # True
    print('-' * 50)
    print(s2.isdigit())     # True


def str_find():
    """
    字符串查找与替换
    :return:
    """
    s1 = 'abcdefgcdef'
    print(s1.find('cd', 4))     # 返回找到字符串的起始下标
    s2 = s1.replace('cd', 'CD', 1)      # 第三个参数是控制替换次数的
    print(s2)


def str_split_join():
    """
    分割与连接
    :return:
    """
    s1 = 'abc bcd 我很帅'
    print(s1.split())                           # ['abc', 'bcd', '我很帅']（默认空格，返回列表）
    s1 = 'abc,bcd,我很帅'
    print(s1.split(','))                        # ['abc', 'bcd', '我很帅']（逗号分隔，返回列表）
    s2 = 'abc\nbcd\nefg'
    print(s2.splitlines())                      # ['abc', 'bcd', 'efg']

    print('-' * 50)
    s3 = 'abc\r\nbcd\r\nefg'
    # splitlines([keepends]) 按照换行符切割字符串 \n,\r,\r\n全部兼容
    print(s3.splitlines(True))                  # ['abc\r\n', 'bcd\r\n', 'efg']（参数keepends=False(默认)：切割后舍弃换行符号）
    print('-' * 50)
    str_list = ['a', 'b', 'c', 'd']
    print(','.join(str_list))                   # a,b,c,d
    print(type(','.join(str_list)))             # <class 'str'>


def study_r():
    """
    \r和\n的区别
    :return:
    """
    s = 'abc\r\nd'
    print(s)


def str_slice():
    """
    字符串的切片
    :return:
    """
    num_str = '0123456789'
    # 与列表相同，都是左闭右开
    # 1. 截取从 2 ～ 5 位置的字符串
    print(num_str[2:6])
    # 2. 截取从 2 ～ '末尾' 的字符串
    print(num_str[2:])
    # 3. 截取从'开始' ~ 5 位置的字符串
    print(num_str[:6])
    # 4. 截取完整的字符串
    print(num_str[:])
    # 5. 从开始位置，每隔一个字符截取字符串
    print(num_str[::2])
    # 6. 从索引 1 开始，每隔一个取一个
    print(num_str[1::2])
    # 倒序切片
    # -1 表示倒数第一个字符
    print(num_str[-1])
    # 7. 截取从 2 ～ '末尾-1' 的字符串
    print(num_str[2:-1])
    # 8. 截取字符串末尾两个字符
    print(num_str[-2:])
    # 9. 字符串的逆序（面试题）
    print(num_str[::-1])


def list_slice():
    # 强制类型转换
    my_list = list('0123456789')
    print(my_list)                              # ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    print(my_list[2:6])                         # ['2', '3', '4', '5']


def index_count():
    hello_str = 'heallo hello'

    # 1. 统计字符串长度
    print(len(hello_str))       # 12
    # 2. 统计某一个小（子）字符串出现的次数
    print(hello_str.count('llo'))       # 2
    print(hello_str.count('abc'))       # 0
    # 3. 某一个子字符串出现的位置
    print(hello_str.index('llo'))       # 3
    # 注意：如果使用index方法传递的子字符串不存在，程序会报错
    print(hello_str.index('abc'))       # ValueError: substring not found


if __name__ == '__main__':
    # check_type()
    # str_find()
    # str_split_join()
    # study_r()
    # str_slice()
    list_slice()
    # index_count()
