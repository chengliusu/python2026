# 作者: 橙流苏
# 2026年07月23日14时44分53秒
# 强扭的瓜不甜，但解渴


def test1():
    print('*' * 50)
    print('这是test1部分')
    print("*" * 50)


def test2():
    print("-" * 50)
    print("这是test 2部分")
    test1()
    print("这是test2部分")
    print("-" * 50)


test2()