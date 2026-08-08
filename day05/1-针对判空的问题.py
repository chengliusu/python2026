# 作者: 橙流苏
# 2026年07月25日17时22分26秒
# 强扭的瓜不甜，但解渴


# 容器是空就是假，不可以用==False去对应
lst = []
if not lst:
    print('空列表')
else:
    print('非空列表')

if {}:
    print('非空字典')
else:
    print('空字典')

# 空的容器和None是不想等的
