# 作者: 橙流苏
# 2026年07月27日14时02分43秒
# 强扭的瓜不甜，但解渴


def input_password():
    # 1. 提示用户输入密码
    pwd = input('请输入密码')
    # 2. 判断密码长度 >= 8,返回用户输入的密码
    if len(pwd) >= 8:
        return pwd
    raise Exception('密码长度必须大于等于8位！')


if __name__ == '__main__':
    # try:
    #     print(input_password())
    # except Exception as result:
    #     print(result)
    try:
        assert 1 == 0, '你的程序在这里发生了XXX异常'
    except Exception as e:
        print(e)
    while True:
        pass
