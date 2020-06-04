"""
@Author:Hirsi
@Time:2020/6/1 21:57
"""

dict1 = {i: i ** 2 for i in range(1, 5)}
print(dict1)

list1 = ['name', 'age', 'gander','id']
list2 = ['Hirsi', 20, 'man']

# 两个列表数据不同,len统计数据少的个数
dict2 = {list1[i]: list2[i] for i in range(len(list2))}
print(dict2)
