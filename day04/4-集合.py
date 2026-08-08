# 作者: 橙流苏
# 2026年07月25日14时10分07秒
# 强扭的瓜不甜，但解渴


def use_set():
    set1 = set()                                        # 定义一个空集合
    print(type(set1))                                   # <class 'set'>

    set2 = {1, 2, 3, 4, 5}                              # 不支持随机访问

    fruits = {'apple', 'banana', 'cherry'}
    fruits.add('orange')
    print(fruits)                                       # {'orange', 'apple', 'banana', 'cherry'}

    fruits = {'apple', 'banana', 'cherry'}
    x = fruits.copy()                                   # 浅拷贝
    print(id(x))                                        # 4498453696
    print(id(fruits))                                   # 4498454368

    x = {'apple', 'banana', 'cherry'}
    y = {'google', 'microsoft', 'apple'}
    z = x.difference(y)
    print(f'差集{z}')                                    # 差集{'banana', 'cherry'}

    x = {'apple', 'banana', 'cherry'}
    y = {'google', 'microsoft', 'apple'}
    x.difference_update(y)
    print(x)                                            # {'banana', 'cherry'}
    print('-' * 50)
    fruits = {'apple', 'banana', 'cherry'}
    fruits.discard('banana')
    print(fruits)                                       # {'apple', 'cherry'}
    print('-' * 50)
    x = {'a', 'b', 'c'}
    y = {'c', 'd', 'e'}
    z = {'f', 'g', 'c'}
    result = x.intersection(y, z)
    print(result)                                       # {'c'}
    print('-' * 50)
    x = {'apple', 'banana', 'cherry'}
    y = {'google', 'runoob', 'apple'}
    z = x.symmetric_difference(y)
    print(z)                                            # {'banana', 'runoob', 'google', 'cherry'}
    print('-' * 50)
    x = {'apple', 'banana', 'cherry'}
    y = {'google', 'runoob', 'apple'}
    z = x.union(y)
    print(z)                                            # {'apple', 'banana', 'runoob', 'google', 'cherry'}

    print('apple' in z)                                 # True

    print(x - y)                                        # {'banana', 'cherry'}
    print(x | y)                                        # {'banana', 'cherry', 'apple', 'google', 'runoob'}
    print(x & y)                                        # {'apple'}
    print(x ^ y)                                        # {'banana', 'cherry', 'google', 'runoob'}


def use_generator():
    """
    使用生成式
    :return:
    """
    my_tuple = tuple(x for x in range(10))              # 元组生成式
    print(my_tuple)                                     # (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
    my_set = {x for x in 'abracadabra' if x not in 'abc'}
    print(my_set)                                       # {'r', 'd'}
    print(len(my_set))                                  # 2


if __name__ == '__main__':
    # use_set()
    use_generator()