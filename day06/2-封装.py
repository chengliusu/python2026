# 作者: 橙流苏
# 2026年07月26日18时22分14秒
# 强扭的瓜不甜，但解渴


class Person:
    """
    人类
    """
    # 对象被初始化时，会被自动调用
    def __init__(self, new_name, new_weight):
        # 在类内定义对象属性（相当于定义加赋值）
        self.name = new_name
        self.weight = new_weight

    def run(self):
        self.weight -= 0.5
        print(f'{self.name}跑步了，体重减去0.5公斤，现有体重{self.weight}')

    def eat(self):
        self.weight += 1
        print(f'{self.name}吃饭了，体重增加1公斤，现有体重{self.weight}')

    # 返回对象的描述信息，print函数输出使用
    def __str__(self):
        """
        因为该函数是别人调用的，必须返回str（字符串）类型
        :return:
        """
        return f'我的名字叫{self.name} 体重{self.weight}公斤'


if __name__ == '__main__':
    elephant = Person('大象', 80)
    elephant.run()
    elephant.eat()
    print(elephant)
    tiger = Person('老虎', 45)
    tiger.eat()
    tiger.run()