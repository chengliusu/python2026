# 作者: 橙流苏
# 2026年08月05日15时37分08秒
# 强扭的瓜不甜，但解渴
import os


def use_rename():
    """
    理解相对路径，绝对路径
    绝对路径每一级需要使用双斜杠
    :return:
    """
    # 重命名文件（源文件，目标文件）
    # .表示当前路径，默认当前路径时可以省略.号
    # 此处dir1表示与本文件处于同一层级
    os.rename('file4', 'file3')
    os.rename('dir1/file2', 'dir1/file1')                   # 注意Mac电脑路径写法

    # 删除同层级dir1中file1文件；只能删除文件，不能删除文件夹
    os.remove('dir1/file1')


def use_dir_func():
    # 列出当前文件列表（list directory）
    file_list = os.listdir('.')
    print(file_list)

    # 创建目录（make directory）
    os.mkdir('dir2')

    # 删除空文件夹，如果文件夹有文件则不能删除（remove directory）
    os.rmdir('dir1')

    # 获取当前工作目录（get current working directory）
    print(os.getcwd())

    # 改变当前工作目录，跳转至dir2文件夹中（change directory）
    os.chdir('dir2')

    # 打开dir2文件夹中file1文件
    file = open('file1', 'w', encoding='utf-8')
    file.close()


def change_dir():
    """
    改变路径
    :return:
    """
    # 获取当前工作目录（get current working directory）
    print(os.getcwd())                          # /Users/qingjiabu/PycharmProjects/python_code2025/day07

    # 改变当前工作路径（change directory）
    os.chdir('dir2')

    # 获取但前工作目录（get current working directory）
    print(os.getcwd())                          # /Users/qingjiabu/PycharmProjects/python_code2025/day07/dir2


def scan_dir(current_path, width):
    """
    目录深度优先搜索
    :param current_path:
    :param width:
    :return:
    """
    file_list = os.listdir(current_path)            # 得到当前文件夹下所有文件
    for file in file_list:
        print(' ' * width, file)                    # 打印文件名，width代表多少空格
        new_path = current_path + '/' + file        # 把当前路径和文件名拼接到一起
        if os.path.isdir(new_path):
            scan_dir(new_path, width + 4)


def use_stat(file_path):
    """
    文件大小
    :param file_path:
    :return:
    """
    file_info = os.stat(file_path)
    # file_info.st_size：文件大小，单位：字节（bytes）；file_info.st_uid：user-id，文件所有者的用户ID，Windows下恒为0，只有Linux/Mac下才有意义
    # file_info.st_mode：文件模式，整数。里面编码了两种信息：1.文件类型：普通文件/文件夹/符号链接  2.文件权限（rwx读写执行权限）
    # file_info.st_time：modify-time，最后修改时间戳，浮点数，单位秒，从1970-01-01 00:00:00 UTC开始计时
    print(f'size{file_info.st_size}, uid{file_info.st_uid}, mode{file_info.st_mode}, mtime{file_info.st_mtime}')    # size5, uid501, mode33188, mtime1786095094.794327
    from time import strftime
    from time import gmtime
    # 使用localtime()可以转为操作系统本地时区（即北京时间东八区）
    gm_time = gmtime(file_info.st_mtime)                                # 输出UTC零时区的时间元组 time_struct；格林威治时间，不是北京时间；北京时间 = UTC + 8小时

    # 把秒数转为字符串时间
    print(strftime("%Y-%m-%d %H:%M:%S", gm_time))                       # 2026-08-07 09:31:34


if __name__ == '__main__':
    # use_rename()
    # use_dir_func()
    # change_dir()
    # 既可以传绝对路径，也可以传相对路径
    # scan_dir('.', 0)
    use_stat('file4')
