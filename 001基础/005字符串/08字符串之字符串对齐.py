"""
@author:Hirsi
@time:2020/5/24 15:15
"""
"""
语法:
    字符串序列.ljust(长度,填充字符)
    字符串序列.rjust(长度,填充字符)
    字符串序列.center(长度,填充字符)
"""

str1='hirsi'

print(str1.ljust(11, '~'))  #左对齐

print(str1.rjust(11,'~'))   #右对齐

print(str1.center(11,'~'))  #居中对齐
