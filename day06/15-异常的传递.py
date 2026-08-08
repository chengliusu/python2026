# 作者: 橙流苏
# 2026年07月27日13时57分42秒
# 强扭的瓜不甜，但解渴


def demo1():
    num = int(input('请输入一个整数：'))
    print('I am demo1')
    return num


def demo2():
    num2 = demo1()
    print('I am demo2')
    return num2


# 利用异常的传递性，在主程序捕获异常
try:
    print(demo2())
except Exception as result:
    print(f'未知错误 {result}')  # invalid literal for int() with base 10: 'asdafa'
