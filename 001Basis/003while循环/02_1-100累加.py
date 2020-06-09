"""
@author:Hirsi
@time:2020/5/21 21:56
"""

"""
1+2+3+4+5......+99+100=?
准备变量保存和
循环做加法运算
"""
# i = 0
# sum = 0
#
# while i <= 100:
#     sum += i
#     i += 2

i = 1
sum = 0
while i <= 100:
    if i % 2 == 0:
        sum += i
    i += 1

print(sum)
