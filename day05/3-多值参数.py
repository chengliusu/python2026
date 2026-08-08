# 作者: 橙流苏
# 2026年07月26日00时27分45秒
# 强扭的瓜不甜，但解渴


# 多值参数，就是参数个数不确定，必须是下面的写法
def demo2(*args, **kwargs):
    print(f'demo2-{args}')
    print(f'demo2-{kwargs}')


# *args 位置参数，打包成元组；**kwargs 关键字参数，打包成字典
def demo(*args, **kwargs):
    print(args)
    print(kwargs)
    demo2(*args, **kwargs)


demo(1, 2, 3, 4, name='小明', age=19)
