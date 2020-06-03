"""
@Author:Hirsi
@Time:2020/6/3 22:24
"""


def addNum(a, b):
    sum1 = a + b
    print(sum1)


splitStr = input('请输入2个数字(空格隔开):').split(' ')

# b = int(input('请输入第2个数字：'))
addNum(int(splitStr[0]), int(splitStr[1]))

# str1='10,20'
# split = str1.split(',')
# print(split)
