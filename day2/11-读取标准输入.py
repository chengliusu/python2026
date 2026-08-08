# 作者: 橙流苏
# 2026年07月18日10时09分23秒
# 知不足而奋进，望远山而前行


def change_alpha():
    a = input('请输入内容')
    print(a)
    print(type(a))

    # 大写转小写
    print(chr(ord(a) + 32))


def change_type():
    a = input('请输入数字')      # 14.56
    print(int(a) + 5)     # 这里字符串14.56只能先转为浮点型，不能直接转为int型变量


# change_alpha()
change_type()
