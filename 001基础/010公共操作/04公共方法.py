"""
@Author:Hirsi
@Time:2020/5/30 0030 8:57
"""

str1 = 'hirsi'
list1 = [10, 20, 30]
t1 = ('cc', 'FF', 'MM')
s1 = {10, 30, 60, 20, 80, 70}
dict1 = {'name': 'Tom', 'age': 26}

""" 1.len() 同级元素个数 """
# print(len(str1))
# print(len(list1))
# print(len(t1))
# print(len(dict1))

""" 2.del/del()  删除 """
# del  str1
# print(str1)

# del list1
# del (list1[1])
# print(list1)

# del  s1
# print(s1)

# del dict1
# del dict1['name']
# print(dict1)

"""3.max()/min()"""
# print(max(str1))
# print(min(s1))

"""4.ranger(start,end,step)返回一个可迭代对象   step:步长默认为1，start：默认为0"""
# 1 2 3...7 8 9
# rNum = range(1, 10, 1)
# for i in rNum:
#     print(i,end=' ')
# print()
#
# for i in range(1,20,2):
#     print(i,end=' ')
# print()
#
# for i in range(10):
#     print(i,end=' ')

"""5.enumerate()返回可迭代对象"""
# for i in enumerate(list1):
#     print(i)

for i in enumerate(list1,1): #1：起始值
    print(i)

for i in enumerate(dict1):
    print(i)
