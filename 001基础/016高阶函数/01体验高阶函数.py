"""
@Author:Hirsi
@Time:2020/6/9 22:00
"""
"""
把函数当作参数传递
"""


# abs()绝对值
# print(abs(-12))
#
# # round() 四舍五入
# print(round(1.5))
# print(round(2.4))

def sunNum(a, b, f):
    return f(a) + f(b)


print(sunNum(-2.8, 6, abs))

print(sunNum(-2.8, 6, round))

print(round(-2.5))   # -2
