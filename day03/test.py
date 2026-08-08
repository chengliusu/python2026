# 作者: 橙流苏
# 2026年07月22日21时43分41秒
# 强扭的瓜不甜，但解渴


name = "小明"
age = 18
print(f"姓名：{name}，年龄：{age:>10d}")       # 这里应该使用可读性更好的规范型写法>10d而非>10

# 数值控制
pi = 3.1415926
print(f"π = {pi:.2f}")  # 保留2位小数 3.14
print(f"{123:06d}")  # 补零，占6位：000123
print(f"{123:>8d}")  # 右对齐，占8格
print(f"{123:<8d}")  # 左对齐
print(f"{123:^8d}")  # 居中

name_list = ['zhangsan', 'lisi', 'wangwu']
for i in name_list:
    print(i)
print(i)