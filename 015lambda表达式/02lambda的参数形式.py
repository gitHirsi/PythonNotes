"""
@Author:Hirsi
@Time:2020/6/9 20:13
"""

# 无参数
fn1 = lambda: 10
print(fn1())

# 一个参数
fn2 = lambda a: a
print(fn2('HirsiBoom'))

# 默认参数
fn3 = lambda a, b, c=30: a + b + c
print(fn3(10, 20))
print(fn3(10, 20, 50))

# 可变参数 *args    返回的为元组
fn4 = lambda *args: args
print(fn4(5, 6, 8, 10))

# 不设定个数的参数(关键字参数) **kwargs   返回的为字典
fn5 = lambda **kwargs: kwargs
print(fn5(name='Hirsi'))
print(fn5(name='Hirsi', age=20, gander='男'))
