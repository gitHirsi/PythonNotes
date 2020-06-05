"""
@Author:Hirsi
@Time:2020/6/5 20:47
"""


# 三个数求和的函数
def sunNum(a, b, c):
    return a + b + c


# 三个数求平均值的函数
def averageNum(a, b, c):
    # 调用求和函数
    num = sunNum(a, b, c)
    return num / 3


# result1 = sunNum(1, 2, 3)
# print(result)

# 求平均值
result2 = averageNum(30, 20, 40)
print(result2)
