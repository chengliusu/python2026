# 作者: 橙流苏
# 2026年07月25日14时48分49秒
# 强扭的瓜不甜，但解渴


def list_set_slice():
    test_list = [1, 2, 3, 4, 5, 6]
    test_list[3:3] = ['x', 'y', 'z']    # 往列表中插入一个列表(从下标 3 开始插入3个数据)
    print(test_list)


def list_compare():
    a = [1, 2, 3]
    b = [1, 2, 3]
    print(a == b)   # 判断内容是否相同
    print(a is b)   # is运算符是判断两个对象的地址是否一致，一致是True


def use_method():
    """
    容器的一些方法
    :return:
    """
    a = (1, 2, 3)
    b = ('a', 'b', 'c')

    # 将多个序列按位置配对，返回迭代器
    print(list(zip(a, b)))      # [(1, 'a'), (2, 'b'), (3, 'c')]

    # 配对好的元组序列可以直接转字典，第一个元素做key，第二个value
    print(dict(zip(b, a)))      # {'a': 1, 'b': 2, 'c': 3}

    # 如何使用enumerate（序列，start = 0）同时获取 索引+值，生成（下标，元素）元组；这里默认下标从0开始，也可以start=1改为下标从1开始
    seasons = ['Spring', 'Summer', 'Fall', 'Winter']
    list2 = list(enumerate(seasons))
    print(list2)        # [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]

    my_dict = dict(list2)
    print({v: k for k, v in my_dict.items()})       # {'Spring': 0, 'Summer': 1, 'Fall': 2, 'Winter': 3}


if __name__ == '__main__':
    # list_set_slice()
    # list_compare()
    use_method()