# 作者: 橙流苏
# 2026年07月27日11时10分48秒
# 强扭的瓜不甜，但解渴


class Son1:
    # *args 是python函数定义中处理可变数量位置参数的常用语法，核心作用是让函数能接受任意个数的位置参数
    # *是关键：它会把传入的多个位置参数打包成一个元组（tuple），赋值给后面的变量（如 args）
    def __init__(self, age, *args):
        self.age = age
        super().__init__(*args)


class Son2:
    def __init__(self, score):
        self.score = score


class Grandson(Son1, Son2):
    def __init__(self, name, *args):
        self.name = name
        # 匿名父类对象只是叫法，实际进去之后还是xiaoming的ID地址
        super().__init__(*args)


if __name__ == '__main__':
    xiaoming = Grandson('小明', 18, 98.5)     # 姓名，年龄，分数
    print(xiaoming.name)
    print(xiaoming.age)
    print(xiaoming.score)
