# 作者: 橙流苏
# 2026年07月25日15时34分29秒
# 强扭的瓜不甜，但解渴


def demo(num, num_list):
    print('函数内部代码')

    num += num  # 等价与 num = num + num （数字、字符串、元组属于不可变数据类型）

    # num_list.extend(num_list)由于是调用方法，所以不会修改变量的引用
    # 函数执行结束后，外部数据同样会发生变化
    num_list += [4, 5, 6]   # 列表、字典、集合属于可变数据类型  != num_list + [4, 5, 6]

    print(num)
    print(num_list)
    print('函数代码完成')


gl_num = 9
gl_list = [1, 2, 3]
demo(gl_num, gl_list)
print(gl_num)   # 9
print(gl_list)  # [1, 2, 3, 4, 5, 6]
