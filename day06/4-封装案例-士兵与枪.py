# 作者: 橙流苏
# 2026年07月26日20时52分57秒
# 强扭的瓜不甜，但解渴


class Gun:
    # 对象初试化时，会被自动调用
    def __init__(self, model):
        # 定义对象属性并赋值
        self.model = model
        self.bullet_count = 0

    def add_bullet(self, count):
        self.bullet_count += count

    def shoot(self):
        # 判断是否还有子弹
        if self.bullet_count <= 0:
            print('没有子弹了。。。')
            return
        # 发射一颗子弹
        self.bullet_count -= 1

        print(f'{self.model} 发射子弹,剩余子弹数{self.bullet_count}')


class Soldier:
    def __init__(self, name, gun: Gun = None):
        self.name = name
        self.gun = gun

    def fire(self):
        # 1. 判断士兵是否有枪
        # if self.gun == None:
        if self.gun is None:
            print(f'{self.name}还没有枪')
            return
        # 2. 高喊口号
        print(f'冲啊。。。{self.name}')
        # 3. 让枪装填子弹
        self.gun.add_bullet(50)
        # 4. 让枪发射子弹
        self.gun.shoot()


if __name__ == '__main__':
    # 创建枪对象
    ak47 = Gun('ak47')
    # ak47.add_bullet(50)
    # ak47.shoot()
    xuSanDuo = Soldier('许三多')
    xuSanDuo.fire()
    xuSanDuo.gun = ak47
    xuSanDuo.fire()
