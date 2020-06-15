"""
@Author:Hirsi
@Time:2020/6/11 12:52
"""

import os


# 构造条件的函数
flag = 2

# 选择到E盘的ZZZ文件夹
os.chdir('E:\\ZZZ')
# 返回目录下所有文件的名字组成的列表
fileList = os.listdir()

for i in fileList:
    if flag == 1:
        newName = 'Python_' + i
    if flag == 2:
        index = len('Python_')
        newName = i[index:]

    os.rename(i, newName)
