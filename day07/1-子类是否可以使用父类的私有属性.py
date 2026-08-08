# 作者: 橙流苏
# 2026年07月27日15时41分07秒
# 强扭的瓜不甜，但解渴


class A:
    def __init__(self):
        # 私有对象属性、实例属性
        # 私有属性、私有方法只能在类内使用
        self.__age = 18

    # 通过共有方法调用私有属性
    def base_age(self):
        print(self.__age)


class B(A):
    # 子类一旦初始化默认覆盖父类初始化方法，此时父类的init方法将不会执行。为保留父类初始化逻辑，须手动调用 super().__init__(参数)
    def __init__(self):
        super().__init__()

    def get_age(self):
        self.base_age()


if __name__ == '__main__':
    zhangsan = B()
    zhangsan.get_age()
