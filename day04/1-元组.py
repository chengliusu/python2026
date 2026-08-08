# 作者: 橙流苏
# 2026年07月24日18时51分06秒
# 强扭的瓜不甜，但解渴


def use_tuple():
    # 元组数据元素不能修改
    info_tuple = ('zhangsan', 18, 1.75, 'zhangsan')
    # 元组属于可迭代对象
    for i in info_tuple:
        print(i)

    print('-' * 50)
    # 元组中元素第一次出现的下标索引
    print(info_tuple.index('zhangsan'))

    # 2. 统计计数
    print(info_tuple.count('zhangsan'))

    # 统计元组中包含元素的个数
    print(len(info_tuple))


def use_str():
    """
    格式化字符串
    :return:
    """
    info_tuple = ('小明', 21, 1.85)

    # 格式化字符串后面的'()'本质上就是元组
    print('%s 年龄是 %d 身高是 %.2f' % info_tuple)
    # f-string 不能直接解包元组，需要手动取值
    print(f'{info_tuple[0]} 年龄是 {info_tuple[1]}, 身高是 {info_tuple[2]:.2f}')


def use_tuple_error():
    # 此为list列表类型
    a = [1]
    print(type(a))      # <class 'list'>

    # todo 如果没有（逗号，）则为int型，否则为tuple元组类型
    b = (7,)    # 定义一个元素的元组
    print(type(b))      # <class 'tuple'>
    for i in b:
        print(i)        # 7

    # b = (7)
    # print(type(b))        <class 'int'>

    # 类似于进行强制类型转换
    c = a
    a = list(b)
    print(f'a的类型为{type(a)}')        # a的类型为<class 'list'>
    b = tuple(c)
    print(f'b的类型为{type(b)}')        # b的类型为<class 'tuple'>


if __name__ == '__main__':
    # use_tuple()
    # use_str()
    use_tuple_error()