# 作者: 橙流苏
# 2026年07月24日17时46分06秒
# 强扭的瓜不甜，但解渴

name_list = ['张三', '李四', '王五', '王小二']

# 使用迭代遍历列表
"""
    顺序的从列表中依次获取数据，每一次循环过程中，数据都会保存在 my_name 这个变量中，在循环体内部
    可以访问到当前这一次获取到的数据
    
for my_name in name_list:
    print(f'我的名字叫 {my_name}')
"""
# 如果遍历，可以用for
# 如果修改，或者删除，建议使用while
for my_name in name_list:
    print(f'我的名字叫{my_name}')

print('-' * 50)
print(my_name)

print('-' * 50)
i = 0
while i < len(name_list):
    print(name_list[i])
    i += 1