# 作者: 橙流苏
# 2026年07月24日13时50分34秒
# 强扭的瓜不甜，但解渴


name_list = ["zhangsan", "lisi", "wangwu"]

# 1. 取值
print(name_list[0])     # zhangsan
# 查找元素
print(name_list.index('wangwu'))    # 2

# 2. 修改
name_list[1] = '李四'
print(name_list)        # ['zhangsan', '李四', 'wangwu']

# 3. 添加
name_list.append('王五')
print(name_list)        # ['zhangsan', '李四', 'wangwu', '王五']

name_list.insert(1, '王小美')
print(name_list)        # ['zhangsan', '王小美', '李四', 'wangwu', '王五']
# extend 方法可以把其他列表中的完整内容，追加到当前列表的末尾
temp_list = ['孙悟空', '猪八戒', '沙师弟']
name_list.extend(temp_list)
print(name_list)        # ['zhangsan', '王小美', '李四', 'wangwu', '王五', '孙悟空', '猪八戒', '沙师弟']

# 4. 删除
# remove方法可以从列表中删除指定的数据（一次只能移除一个wangwu）
name_list.remove('wangwu')
# pop 方法默认可以把列表中最后一个元素删除
name_list.pop()
# pop 方法可以指定要删除元素的索引
name_list.pop(3)
# clear 方法可以清空列表（地址不变）
name_list.clear()
# del name_list
print(name_list)
name_list.append(3)
print(name_list)

list