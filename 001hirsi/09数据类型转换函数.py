"""
@author:Hirsi
@time:2020/5/20 20:53
"""

# eval()  --计算在字符串中的有效python表达式，并返回一个对象
str1='1'
str2='1.1'
str3='(10,20,30)'
str4='[100,200,300]'
print(type(eval(str1)))
print(type(eval(str2)))
print(type(eval(str3)))
print(type(eval(str4)))