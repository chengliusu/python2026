# 作者: 橙流苏
# 2026年07月23日16时25分48秒
# 强扭的瓜不甜，但解渴


def no_change(num):
    print(f"num = {num}, num的地址{id(num)}")
    # 函数内的局部变量只存活在函数执行期间，外部无法读取
    num = 5
    print(f"修改num后num={num}, num的地址{id(num)}")


a = 10

print(f'调用函数前a的地址{id(a)}')
no_change(a)
print(f'调用函数后a的值{a}')


def change(new_list):
    print(f'赋值前，new_list的地址{id(new_list)}')
    new_list[0] = 10
    print(f'赋值后，new_list的地址{id(new_list)}')


my_list = [1, 2, 3]     # 可变数据类型
print(f'调用change之前{my_list}, 地址{id(my_list)}')
change(my_list)
print(f'调用change之后{my_list}, 地址{id(my_list)}')
