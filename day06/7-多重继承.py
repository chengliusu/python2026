# 作者: 橙流苏
# 2026年07月27日10时54分20秒
# 强扭的瓜不甜，但解渴


class A:
    def test(self):
        print('A test')

    def demo(self):
        print('A demo')


class B:
    def test(self):
        print('B test')

    def demo(self):
        print('B demo')


class C(A, B):
    def test(self):
        print('C test')


if __name__ == '__main__':
    c = C()
    c.test()        # C test
    c.demo()        # A demo
    # MRO(method resolution order) 是一个元组，查看方法解析顺序，在多继承时判断方法、属性的调用路径
    # super() 不是直接去找父类，而是严格按照__mro__序列，找到当前类的下一个类
    print(C.__mro__)    # (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
