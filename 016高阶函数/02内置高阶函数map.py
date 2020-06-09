"""
@Author:Hirsi
@Time:2020/6/9 22:16
"""
"""
map(funx,lst),将传入的函数变量funx作用到lst变量的每个元素中，并将结果做成新的迭代器返回
"""
list1 = [2, 3, 4, 5, 6, 7, 8, 9]


def funx(a):
    return a ** 2


result = map(funx, list1)
print(result)
print(list(result))
