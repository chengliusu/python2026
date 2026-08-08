# 作者: 橙流苏
# 2026年07月18日10时08分17秒
# 知不足而奋进，望远山而前行

a = 1
b = 1

print(id(a))    # a和b的地址一致
print(id(b))

a = 2
c = 2
print(id(a))    # a相当于又挂在2数据上
print(id(c))

a = 123456789123456789123
print(a)

print(type(a))
