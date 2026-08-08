# 作者: 橙流苏
# 2026年08月08日13时40分57秒
# 强扭的瓜不甜，但解渴

import sys

# argument vector(参数列表)
print(type(sys.argv))                       # <class 'list'>
# 此时这个列表只有一个数据 -> 该模块文件路径
print(sys.argv)     # ['/Users/qingjiabu/PycharmProjects/python_code2025/day07/7-python程序如何传参.py']
# 右上方 7-python程序如何传参 -> Edit Configurations -> Script Parameters -> 123 abc（填写参数，此时列表就有三个数据了）
# ['/Users/qingjiabu/PycharmProjects/python_code2025/day07/7-python程序如何传参.py', '123', 'abc']


def write_hello(file_path):
    file = open(file_path, 'w+', encoding='utf-8')
    file.write('流苏天下无敌！')
    file.close()


if __name__ == '__main__':
    # 右上方 7-python程序如何传参 -> Edit Configurations -> Script Parameters -> 流苏天下无敌！（填写参数，此时列表就有2个数据了
    write_hello(sys.argv[1])
