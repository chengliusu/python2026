# 作者: 橙流苏
# 2026年07月24日07时25分35秒
# 强扭的瓜不甜，但解渴


# 代码导入模块中时直接被执行的语句会被直接执行
import my_first_module

my_first_module.print_line('-', 50)

print(my_first_module.__name__)     # my_first_module
print(__name__)     # __main__
