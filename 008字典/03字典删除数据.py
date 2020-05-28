"""
@author:Hirsi
@time:2020/5/28 22:03
"""

dict1 = {'name': 'Hirsi', 'age': 20, 'gander': '男'}

# del 删除字典或指定的键值对
# del (dict1)
# print(dict1)

del dict1['name']
print(dict1)

# clear() 清空字典
dict1.clear()
print(dict1)