# 作者: 橙流苏
# 2026年07月27日12时52分12秒
# 强扭的瓜不甜，但解渴


class MusicPlayer(object):
    instance = None     # 用来保存对象的

    # 分配内存空间；返回对象引用
    def __new__(cls, *args, **kwargs):
        # 1. 创建对象，分配空间
        if cls.instance is None:
            # 调用父类object的__new__开辟内存，创建对象
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self, name):
        # 创建对象属性并赋值
        self.name = name


if __name__ == '__main__':
    player1 = MusicPlayer('七里香')
    print(MusicPlayer.instance)
    player2 = MusicPlayer('东风破')
    print(MusicPlayer.instance)
    # 为什么ID地址一样
    print(id(player1))
    print(id(player2))
    print(player1.name)
    print(player2.name)
