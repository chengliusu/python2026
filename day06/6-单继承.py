# 作者: 橙流苏
# 2026年07月26日22时37分16秒
# 强扭的瓜不甜，但解渴


class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print('吃。。。')

    def drink(self):
        print('喝。。。')

    def run(self):
        print('跑。。。')

    def sleep(self):
        print('睡。。。')


# 不继承时后不需要加括号
# 继承后子类拥有父类所有属性和方法（可以直接访问父类的公有属性和公有方法）
class Dog(Animal):
    def __init__(self, name, color):
        # 在python中super是一个特殊的类
        # super()就是使用super类创建出来的对象
        # 父类的实例属性不会自动创建，需要调用父类的init初始化方法才能创建
        # 但父类的方法可以自动继承
        super().__init__(name)  # 子类对象调用父亲的init
        self.color = color

    def bark(self):
        print(f'{self.name}汪汪叫{self.color}--')

    def run(self):
        super().run()
        print(f'{self.name}跑得快')


class XiaoTianQuan(Dog):
    def __init__(self, name, color, age):
        # 父类对象调用父亲的init
        super().__init__(name, color)
        self.age = age

    def fly(self):
        print(f'{self.name}飞天--{self.color}--{self.age}')


if __name__ == '__main__':
    wangcai = Dog('旺财', '黄色')
    wangcai.bark()
    wangcai.run()
    xiaotianquan = XiaoTianQuan('啸天犬', '黑色', 20)
    xiaotianquan.fly()
