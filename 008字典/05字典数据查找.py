"""
@author:Hirsi
@time:2020/5/28 22:13
"""
dict1 = {'name': 'Hirsi', 'age': 20, 'gander': '男'}

# get()
print(dict1['name'])
print(dict1.get('id',100))
print(dict1)

# keys()
keys = dict1.keys()
print(keys)
# values()
print(dict1.values())
# items
items = dict1.items()
print(type(items))
print(items)