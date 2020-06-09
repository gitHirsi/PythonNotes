"""
@author:Hirsi
@time:2020/5/25 21:26
"""

"""
extend()如果追加的数据是一个序列，则将这个序列的数据拆开逐一添加到列表
"""

nameList = ['Hirsi', 'Tom', 'Bill']

# nameList.extend('Boom')   #['Hirsi', 'Tom', 'Bill', 'B', 'o', 'o', 'm']
nameList.extend(['aa','bb'])

print(nameList)