# 作者: 橙流苏
# 2026年07月26日00时20分44秒
# 强扭的瓜不甜，但解渴


def print_info(name, title='', gender=True):
    """
    :param name: 职位
    :param title: 班上同学的名字
    :param gender: True 男生 False 女生
    :return:
    """
    gender_text = '男生'

    if not gender:
        gender_text = '女生'

    print(f'{title}{name}是{gender_text}')


# 提示：在指定缺省参数的默认值时，应该使用最常见的值作为默认值
print_info('小明')
print_info('老王', title='班长')
print_info('小美', '学习委员', False)
print('-' * 50)
print_info('小美', gender=False, title='学习委员')