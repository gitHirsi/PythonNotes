"""
@Author:Hirsi
@Time:2020/6/5 22:12
"""

a = 100
b = 300
"""
方法一
"""
# 定义中间变量
c = 0

c = a
a = b
b = c
# print(a) #300
# print(b) #100

"""
方法二
"""
a,b=20,50
print(a,b)
a,b=b,a
print('交换后👇')
print(a,b)
