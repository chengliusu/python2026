# 作者: 橙流苏
# 2026年07月27日11时56分50秒
# 强扭的瓜不甜，但解渴


class Parent:
    def __init__(self, height):
        self.height = height


class Son1(Parent):
    def __init__(self, age, *args):
        self.age = age
        super().__init__(*args)


class Son2(Parent):
    def __init__(self, score, *args):
        self.score = score
        super().__init__(*args)


class Grandson(Son1, Son2):
    def __init__(self, name, *args):
        self.name = name
        # 依次调用Son1、Son2
        super().__init__(*args)


if __name__ == '__main__':
    xiaoming = Grandson('小明', 18, 98.5, 175)  # 姓名、年龄、分数、身高
    print(xiaoming.name)
    print(xiaoming.age)
    print(xiaoming.score)
    print(xiaoming.height)
    # (<class '__main__.Grandson'>, <class '__main__.Son1'>, <class '__main__.Son2'>, <class '__main__.Parent'>, <class 'object'>)
    print(Grandson.__mro__)
