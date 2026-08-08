# 作者: 橙流苏
# 2026年07月24日06时59分01秒
# 强扭的瓜不甜，但解渴

# 1. 执行到需要全局变量时，全局变量必须被定义了
# 2. 就近原则
def demo1():
    global num
    print(num)
    num = 2
    print(f'demo1函数里边 修改后{num}')


num = 10
print(f'函数调用前{id(num)}')
demo1()
print(f'函数调用后{num}, 地址{id(num)}')
