# 作者: 橙流苏
# 2026年07月23日16时14分44秒
# 强扭的瓜不甜，但解渴


def print_line(char, times):
    print(char * times)
    # print(num)    不合理的写法


# 把业务逻辑封装进main()函数，不再判断里直接堆代码
def main():
    a = '*'
    times = 50
    num = 100
    print_line(a, times)


def func():
    print('这是第二个内部代码')


# 正常if条件里的变量属于全局变量（if不是函数、不是类，不创建新作用域）
# python中只有两种产生局部作用域：1、def 函数（） 2、class 类
# if/for/while/try 都不会开辟独立作用域
if __name__ == '__main__':  # python 一切皆模块
    main()
    func()
