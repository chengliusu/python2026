# 作者: 橙流苏
# 2026年07月26日18时10分18秒
# 强扭的瓜不甜，但解渴


class Cat(object):
    """
    这是一个猫类
    """
    # 对象初始化时会被自动调用
    def __init__(self, new_name):
        print('这是一个初始化方法')
        self.name = new_name

    def eat(self):
        print(f'{self.name}爱吃鱼')

    def drink(self):
        print(f'{self.name}在喝水')

    # 对象被从内存中销毁前，会被自动调用
    def __del__(self):
        print(f'{self.name}对象被销毁')

    def __str__(self):
        """
        返回对象的描述信息，print函数输出使用
        :return:
        """
        return f'对象{self.name}'


def main():
    tom = Cat('Tom')
    tom.drink()
    tom.eat()
    lazy_cat = Cat('懒猫')
    print('-' * 50)
    print(id(tom))  # 4659812816
    print(id(lazy_cat))     # 4659812864
    print(tom is lazy_cat)      # False
    # tom.name = 'Tom' 不规范编程，不要在类外面给对象增加属性
    print(tom.name)
    print('-' * 50)
    print(tom)  # 对象Tom


if __name__ == '__main__':
    main()
    print('程序结束')