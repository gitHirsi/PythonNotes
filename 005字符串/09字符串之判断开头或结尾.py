"""
@author:Hirsi
@time:2020/5/24 15:22
"""

"""
检查字符串是否以某个字串结束或开始
语法:
    字符串序列.startswith(子串,开始位置下标,结束位置下标)
    字符串序列.endswith(子串,开始位置下标,结束位置下标)
"""

myStr = 'hello world and itcast and itheima and Python'

#1.startswith() 检查字符串是否以某个字串开始
print(myStr.startswith('hello'))  #True
print(myStr.startswith('hels'))   #False
print('-----------------')
#2.endswith()  检查字符串是否以某个字串结尾
print(myStr.endswith('Python'))
print(myStr.endswith('python'))

