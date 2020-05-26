"""
@author:Hirsi
@time:2020/5/25 21:34
"""

nameList = ['Hirsi', 'Tom', 'Bill', 'aa', 'bb', 'cc']

"""
1.del
"""
# del nameList  #删除整个列表
# del nameList[2]  #删除指定下标位置数据

# print(nameList)
# print('-------------------')

"""
2.pop()  按下标删除,不指定下标，删除最后一个
        
"""
# popName1 = nameList.pop()
# print(popName1)
# popName2 = nameList.pop(2)
# print(popName2)

"""
3.remove(数据)   删除指定数据
"""
# nameList.remove('Hirsi')
# print(nameList)

"""
4.clear()  清空列表数据
"""
nameList.clear()
print(nameList)
