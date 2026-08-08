# 作者: 橙流苏
# 2026年07月26日00时35分45秒
# 强扭的瓜不甜，但解渴


import sys

sys.setrecursionlimit(100000)


# 为啥要递归：递归实现的难度比循环要低
# 1. 找到递归方式
# 2. 编写结束条件
def sum_numbers(num):
    print(num)
    # 递归出口（结束条件）很重要，否则会出现死循环
    if num == 1:
        return
    sum_numbers(num - 1)


def f(n):
    # 结束条件
    if n == 1:
        return 1
    return n + f(n - 1)


def step(n):
    if n == 1 or n == 2:
        return n
    return step(n - 1) + step(n - 2)


if __name__ == '__main__':
    # sum_numbers(3)
    # print(f(100))
    for i in range(1, 10):
        print(step(i))
