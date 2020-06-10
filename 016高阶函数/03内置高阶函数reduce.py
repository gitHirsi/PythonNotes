"""
@Author:Hirsi
@Time:2020/6/9 22:26
"""
import functools

"""
reduce(func,lst),其中func必须有两个参数，每次func计算的结果继续和序列的下一个元素做累计计算
"""

list1 = [1, 2, 3, 4, 5, 6]

def func(a,b):
    return a+b


result = functools.reduce(func,list1)
print(result)