# 作者: 橙流苏
# 2026年07月25日15时24分08秒
# 强扭的瓜不甜，但解渴


def measure():
    """
    掌握返回多个值时，如何取处理
    :return:
    """
    print('开始测量')
    temp = 39
    wetness = 10
    print('测量结束')

    # python函数永远只能返回一个对象；所谓多个返回值只是语法糖：把多个对象打包成一个元组对象返回
    # 函数逗号分割多个返回数据，自动封装为元组返回
    return temp, wetness


ret1 = measure()
print(ret1)
a = 10
b = 5
a, b = b, a
print(a, b)