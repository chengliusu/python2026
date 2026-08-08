# 作者: 橙流苏
# 2026年07月27日12时23分04秒
# 强扭的瓜不甜，但解渴


class Tool:
    count = 0  # 类属性，类似于类的全局变量

    def __init__(self, name):
        # 定义对象属性（实例属性）并赋值
        self.name = name
        # 类属性自增
        Tool.count += 1

    # 实例方法可以调用类属性、类方法、实例属性、实例方法
    def func(self):
        print(f'{self.name}可以做很多事情')

    # 类方法只能调用类属性、类方法
    @classmethod
    def show_tool_count(cls):
        """
        当你不使用对象属性，只使用类属性、类方法时
        :return:
        """
        print(cls.count)

    # 静态方法，既不使用实例属性、实例方法，也不使用类属性、类方法
    @staticmethod
    def help():
        """
        不使用对象属性，也不使用类属性
        :return:
        """
        print(f'这是一个工具类，作用是实例化各种工具对象')


if __name__ == '__main__':
    tool1 = Tool('斧子')
    print(Tool.count)
    tool2 = Tool('锤子')
    print(Tool.count)
    del tool1
    print(Tool.count)   # 删除之后的count值仍为2

    # Tool.name = '工具类'，不要在类外给类增加属性，属性分散各处，可读性差
    # 当用对象名添加对象属性时，即使对象属性与类属性名称相同，两者也属于不同属性
    # Python中实例对象查找属性时，遵循‘先找实例自己的属性，找不到再找类的属性'的规则

    # 不需要传递cls参数，与self一致
    Tool.show_tool_count()
    Tool.help()