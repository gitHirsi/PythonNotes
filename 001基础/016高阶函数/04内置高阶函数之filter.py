"""
@Author:Hirsi
@Time:2020/6/10 22:00
"""

"""
filter(func.lst)函数用于过滤序列，过滤不符合条件的元素，返回一个filter对象，可以用list()来转换为列表
"""

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


# 定义功能函数，过滤序列中的偶数
def func(a):
    return a % 2 == 0


result = filter(func, list1)
print(result)
print(list(result))