# 作者: 橙流苏
# 2026年07月24日14时14分27秒
# 强扭的瓜不甜，但解渴


name_list = ['张三', '李四', '王五', '王小二', '张三']

# len(length 长度）函数可以统计列表中元素的总数
list_len = len(name_list)
print(f'列表中包含 {list_len} 个元素')

# count 方法可以统计列表中某一个数据出现的次数
count = name_list.count('张三')
print(f'张三出现了 {count} 次')

# 从列表中删除第一次出现的数据，如果数据不存在，程序会报错
name_list.remove('张三')

print(name_list)