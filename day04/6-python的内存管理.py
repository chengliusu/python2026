# 作者: 橙流苏
# 2026年07月25日15时22分23秒
# 强扭的瓜不甜，但解渴


a = 2
b = 2
print(a is b)   # True
a = 'hello'
print(id(a))    # 4372136032
del a
b = 'hello'
print(id(b))    # 4372136032
