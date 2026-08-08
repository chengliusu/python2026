# 作者: 橙流苏
# 2026年07月24日20时49分44秒
# 强扭的瓜不甜，但解渴


def use_dict_base():
    """
    字典基础操作
    :return:
    """
    xiaoming_dict = {'name': '小明'}
    print(id(xiaoming_dict))                # 4297947648
    # 1. 取值
    print(xiaoming_dict['name'])            # 这里name要打引号

    # 2. 增加、修改
    xiaoming_dict['age'] = 18               # 增加age
    print('-' * 50)
    print(xiaoming_dict)                    # {'name': '小明', 'age': 18}
    # 字典为可变数据类型，id 值不变
    print(id(xiaoming_dict))                # 4297947648

    # 如果key存在，会修改已经存在的键值对
    xiaoming_dict['name'] = '小小明'
    print('-' * 50)
    print(xiaoming_dict)

    # 3. 删除
    print(xiaoming_dict.pop('name'))        # 小小明（pop的返回值是删除的键对应的值）
    # del xiaoming_dict['name']
    print(xiaoming_dict)                    # {'age': 18}

    # 4. 统计键值对的数量
    print(len(xiaoming_dict))               # 1

    # 5. 合并字典
    temp_dict = {'height': 1.75, 'age': 20}

    # 字典没有进行运算符的重载
    # xiaoming_dict += temp_dict
    xiaoming_dict.update(temp_dict)
    print('-' * 50)
    print(xiaoming_dict)                    # {'age': 20, 'height': 1.75}
    # 字典清空操作
    xiaoming_dict.clear()
    print('-' * 50)
    print(xiaoming_dict)                    # {}
    # 字典虽然清空，但地址没有改变
    print(id(xiaoming_dict))                # 4297947648
    print('-' * 50)


def use_dict_iter():
    """
    字典遍历
    :return:
    """
    xiaoming_dict = {'name': '小明', 'qq': '123456', 'phone': '10086'}
    # 迭代遍历字典
    # 变量k是每一次循环中，获取到的键值对的key {key: value}
    for k in xiaoming_dict:
        print(k, xiaoming_dict[k])
    print('-' * 50)
    for k, v in xiaoming_dict.items():
        print(f'键 {k}: 值{v}')
    print('-' * 50)

    # k键 v值
    # for kv in xiaoming_dict.items():
    #       print(kv)
    for k in xiaoming_dict.keys():
        print(k)
    print('-' * 50)
    for v in xiaoming_dict.values():
        print(v)


def use_list_dict():
    """
    列表套字典
    :return:
    """
    card_list = [{'name': '张三', 'qq': '12345', 'phone': '110'}, {'name': '李四', 'qq': '54321', 'phone': '10086'}]    # 列表套字典写法
    for card in card_list:
        print(card)


# 拆包
def use_unpack_package():
    k, v, w = (1, 2, 3)
    print(k, v, w)


if __name__ == '__main__':
    # use_dict_base()
    # use_dict_iter()
    use_list_dict()
    # use_unpack_package()
