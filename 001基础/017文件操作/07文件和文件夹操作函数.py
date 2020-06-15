"""
@Author:Hirsi
@Time:2020/6/11 12:27
"""

import os

"""文件操作"""
# 文件重命名
# os.rename('test.txt', '10.txt')

# 删除文件
# os.remove('11.txt')

"""文件夹操作"""
# 创建文件夹
# os.mkdir('aa')

# 删除文件夹
# os.rmdir('aa')

# 获取当前文件目录
# print(os.getcwd())

# 改变目录路径
# os.chdir('aa')  #切换到aa文件夹
# os.mkdir('WW')

# 获取目录下所有文件，并返回一个列表
# listdir = os.listdir()
# print(listdir)
# print(os.listdir('aa'))

# 重命名文件夹
os.chdir('AA')
os.rename('WW','AA')