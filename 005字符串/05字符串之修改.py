"""
@author:Hirsi
@time:2020/5/24 14:47
"""

myStr = 'hello world and itcast and itheima and Python'

# 1.replace() 替换  返回修改后的字符串，不改变原字符串

# rStr = myStr.replace('and', 'he')
rStr = myStr.replace('and', 'he', 1)  # 1 是替换次数
print(rStr)
# 说明字符串是不可变类型

# 2.split()  分割，返回一个列表
# listStr = myStr.split('and')
# listStr = myStr.split('and',2)
listStr = myStr.split('and',10)
print(listStr)

#3.join()  合并
myList=['aa','bb','cc']
jStr = '~~'.join(myList)
print(jStr)
