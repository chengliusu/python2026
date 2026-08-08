# 作者: 橙流苏
# 2026年07月27日12时06分23秒
# 强扭的瓜不甜，但解渴


class Dog(object):
    def __init__(self, name):
        self.name = name

    def game(self):
        print(f'{self.name} 蹦蹦跳跳的玩耍')


# 子类没有重写__init__，在创建XiaoTianDog('啸天犬')时，Python自动向上寻找父类Dog.__init__执行
# 如果子类自己写了__init__，又不调用super()，那在使用self.name时就会报错
# 子类不写init：自动调用父类__init__，父类实例属性正常拥有；子类重写init：不会自动调用父类构造方法，想要父类实例属性必须手动super().__init__()
class XiaoTianDog(Dog):
    def game(self):print(f'{self.name}飞到天上去玩耍。。。')


class Person:
    def __init__(self, name):
        self.name = name

    # 多态
    def game_with_dog(self, dog: Dog):
        print(f'{self.name}和{dog.name}快乐的玩耍')
        dog.game()  # 多态


if __name__ == '__main__':
    zhangsan = Person('张三')
    wangcai = Dog('旺财')
    zhangsan.game_with_dog(wangcai)
    xiaotianquan = XiaoTianDog('啸天犬')
    zhangsan.game_with_dog(xiaotianquan)
