"""
@Author:Hirsi
@Time:2020/6/5 20:32
"""


# 打印横线的函数
def printLine():
    print('-' * 20)


# 打印一一条横线
# printLine()

# 打印多条横线
def printLines(num):
    i = 0
    while i < num:
        print('-' * 20)
        i+=1

printLines(6)