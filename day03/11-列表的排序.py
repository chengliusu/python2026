# 作者: 橙流苏
# 2026年07月24日17时39分17秒
# 强扭的瓜不甜，但解渴


name_list = ['zhangsan', 'lisi', 'wangwu', 'wangxiaoer']
num_list = [6, 8, 4, 1, 10]

# 升序
name_list.sort()
print(name_list)        # ['lisi', 'wangwu', 'wangxiaoer', 'zhangsan']
num_list.sort()
print(num_list)         # [1, 4, 6, 8, 10]

# 降序
name_list.sort(reverse=True)
print(name_list)        # ['zhangsan', 'wangxiaoer', 'wangwu', 'lisi']
num_list.sort(reverse=True)
print(num_list)         # [10, 8, 6, 4, 1]

# 逆序（反转）    反转并非降序
# 执行一下示例时需要将上述升序和降序屏蔽
name_list.reverse()
print(name_list)        # ['wangxiaoer', 'wangwu', 'lisi', 'zhangsan']
num_list.reverse()
print(num_list)         # [10, 1, 4, 8, 6]
