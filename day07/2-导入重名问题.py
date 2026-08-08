# 作者: 橙流苏
# 2026年07月27日15时49分18秒
# 强扭的瓜不甜，但解渴


# 从module1中导入函数test1
from module1 import test1

# 模块module2中函数test1与module1中函数test1重名，因此可以取别名为 module2_test1
# 同名函数，后导入的模块函数会覆盖先导入的函数
from module2 import test1 as module2_test1

import random

test1()
module2_test1()

# 查看模块所在路径
print(random.__file__)  # 查看模块所在路径
# 取值范围两边都包含
num = random.randint(1, 3)
print(num)