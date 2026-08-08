# 作者: 橙流苏
# 2026年08月08日14时07分46秒
# 强扭的瓜不甜，但解渴


def read_conf():
    """
    读取配置
    :return:
    """
    file = open('file6', 'r+', encoding='utf-8')
    # text_info是字符串，不是字典
    text_info = file.read()
    print(text_info)
    # print(text_info['ip'])

    # eval()：将字符串当成有效表达式来求值并返回计算结果
    my_dict = eval(text_info)
    print(my_dict)                          # {'ip': '192.168.1.100', 'username': 'root', 'password': '123'}
    print(type(my_dict))                    # <class 'dict'>
    file.close()


if __name__ == '__main__':
    read_conf()