"""
@Author:Hirsi
@Time:2020/6/9 17:27
"""


# def fn1():
#     return 100
#
# print(fn1(),end='\n----------\n')
#
#
# # lambda  匿名函数
#
# fn2=lambda :100
# print(fn2)
# print(fn2())


def add(a, b):
    return a + b


addNum = add(10, 20)
print(addNum)

# lambda
fn1 = lambda a, b: a + b
print(fn1(5, 23))
