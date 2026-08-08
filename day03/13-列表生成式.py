# 作者: 橙流苏
# 2026年07月24日17时54分56秒
# 强扭的瓜不甜，但解渴

my_list = [x for x in range(10)]
print(my_list)

for k in range(0):
    print(k)

# 2个循环
# [0, 0, 1, 0, 1, 2, 0, 1, 2, 3, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, 7, 0, 1, 2, 3, 4, 5, 6, 7, 8]
# 第一个0是从range(1)开始的，不是从range(0)开始的。所以共有9个0
a = [j for i in range(10) for j in range(i)]
print(a)

# 二维列表
a = [[col * row for col in range(5)] for row in range(5)]
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8], [0, 3, 6, 9, 12], [0, 4, 8, 12, 16]]
print(a)
print(a[1][2])      # 2

# 二维转一维
b = [j for x in a for j in x]       # x 表示每一行的所有数据
print(b)        # [0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 0, 2, 4, 6, 8, 0, 3, 6, 9, 12, 0, 4, 8, 12, 16]

# 使用if
c = [x for x in range(10) if x % 2 == 0]
print(c)        # [0, 2, 4, 6, 8]

# 使用if else
d = [x if x % 2 == 0 else x ** 2 for x in range(10)]
print(d)        # [0, 1, 2, 9, 4, 25, 6, 49, 8, 81]
