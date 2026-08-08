# 作者: 橙流苏
# 2026年07月26日22时27分29秒
# 强扭的瓜不甜，但解渴


class Women:
    """
    私有属性和私有方法只能在类内部访问
    """

    # 对象初始化时，会被自动调用
    def __init__(self, name, age):
        self.name = name
        # 私有属性
        self.__age = age

    # 在定义属性或方法时，在属性名或者方法名前增加两个下划线，定义的就是私有属性或方法
    def __secret(self):
        print(f'{self.name}年龄{self.__age}')

    def boy_friend(self):
        self.__secret()


if __name__ == '__main__':
    xiaoHong = Women('小红', 18)
    # 定义：class Women：def __init__(self): self.__age = 18
    # 改写后：属性名会变成 _类名__属性名，也就是_Women_age
    # 外部无法直接用 xiaohong.__age 访问，但可以通过改写后的名称 xiaohong._Women__age 绕过限制（这是 Python 的'伪私有' 特性）
    # print(xiaohong._Women__age)   一般不这么写
    xiaoHong.boy_friend()
