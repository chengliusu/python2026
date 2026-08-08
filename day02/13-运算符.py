# 作者: 橙流苏
# 2026年07月18日11时17分27秒
# 知不足而奋进，望远山而前行


def use_sum():
    """
    学习算术运算符
    :return:
    """
    a = 5 / 2  # 2.5
    print(a)
    a = 5 // 2  # 2
    print(a)


def use_compare():
    print(3 > 5)  # False


def use_logic():
    """
    使用逻辑运算符
    :return:
    """
    # a and b规则：1、如果a为假值（0，空字符串、None、空列表等），直接返回a
    # 2、如果a为真值，返回后面的b
    print(3 and 5)
    # a or b规则：1、如果a为真值，直接返回a
    # 2、如果a为假值，返回后面的b
    print(0 or 3)


def use_logic2():
    """
    短路运算目的是不想写if
    :return:
    """
    a = False

    # a and print('hello')
    print(a and print('hello'))
    a = True
    # a or print('你可以看到or')
    print(a or print('你可以看到or'))


def use_bit():
    """
    位运算练习
    :return:
    """
    print(5 & 7)
    print(5 | 7)
    print(~5)
    print(5 ^ 7)  # 按位异或
    # 左移永远是乘2（左移没有丢弃，一直变大）
    print(5 << 1)
    print(-5 << 1)
    print('-' * 50)
    # 右移正数高位补0，负数高位1，低位丢弃(python只有整数，没有无符号型整数和有符号型整数)
    print(5 >> 1)
    print(-6 >> 1)  # 减一除二
    # 异或特点
    print(5 ^ 0)
    print(5 ^ 5)


# use_sum()
# use_compare()
# use_logic()
use_logic2()
# use_bit()
# 帮我写一个快排

