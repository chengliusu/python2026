# 作者: 橙流苏
# 2026年07月26日20时34分44秒
# 强扭的瓜不甜，但解渴


class HouseItem:
    # 对象初始化时，会被自动调用
    def __init__(self, name, area):
        """
        初始化方法
        :param name: 家具名称
        :param area: 家具占地面积
        """
        self.name = name
        self.area = area

    # 返回对象描述信息，print函数输出使用
    def __str__(self):
        return f'{self.name}占地面积{self.area:.2f}'


class House:
    # 对象初始化时，被自动调用
    def __init__(self, house_type, area):
        """
        房子初始化方法
        :param houe_type: 房子户型
        :param area: 房子占地面积
        """
        self.house_type = house_type
        self.area = area
        self.free_area = area   # 剩余可用面积
        self.items_list = []    # 家具列表

    # 放回对象描述信息，print函数输出使用
    def __str__(self):
        # 户型：两室一厅
        # 总面积：30[剩余22.5]
        # 家具：['席梦思', '衣柜', '餐桌']
        return f'户型：{self.house_type}\n总面积：{self.area}[剩余{self.free_area}]\n家具：{self.items_list}'

    # 方法中第一个参数必须时self
    # item: HouseItem 后面的HouseItem 为纯注解，没有任何意义。只是为了方便后面写代码时方便联想
    def add_item(self, item: HouseItem):
        if item.area > self.free_area:
            print('房子没空间了，放家具失败')
            return
        # 2. 计算剩余面积
        self.free_area -= item.area
        # 3. 将家具名称追加到名称列表中
        self.items_list.append(item.name)


if __name__ == '__main__':
    bed = HouseItem('席梦思', 4)
    wardrobe = HouseItem('衣柜', 2)
    table = HouseItem('餐桌', 1.5)
    print(bed)
    print(wardrobe)
    print(table)
    house = House('两室一厅', 30)
    house.add_item(bed)
    house.add_item(wardrobe)
    house.add_item(table)
    print(house)