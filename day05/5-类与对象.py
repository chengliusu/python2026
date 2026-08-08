# 作者: 橙流苏
# 2026年07月26日00时46分53秒
# 强扭的瓜不甜，但解渴


# 类名采用大驼峰命名法
class Person:
    def __init__(self, new_name, new_age, new_height):
        # 实例属性
        self.name = new_name
        self.age = new_age
        self.height = new_height

    def run(self):
        print(self.name + '正在奔跑')

    def eat(self):
        print(self.name + '正在吃东西')


# 实例化
elephant = Person('大象', 18, 1.75)

# 输出多个变量
print(elephant.name, elephant.age, elephant.height)

elephant.run()
tiger = Person('老虎', 17, 1.65)
print(tiger.name, tiger.age, tiger.height)
tiger.run()

print('-' * 59)

# directory：目录；清单
# dir(x)返回一个列表，包含对象所有可用属性、方法名称字符串
# dir(Person)：查看类Person拥有的成员（类属性、方法、继承来的魔法方法）
# dir(Person)看不到name、age、height，因为是实例属性，保存在实例对象里，不是类上面
print(dir(Person))

print('-' * 50)

# 类继承来的一切 + 实例属性
print(dir(elephant))

print('-' * 50)
elephant.name = '大黄蜂'
