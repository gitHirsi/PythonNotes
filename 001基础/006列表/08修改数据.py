"""
@author:Hirsi
@time:2020/5/26 19:36
"""

nameList = ['Hirsi', 'Tom', 'Bill', 'aa', 'bb', 'cc']
numList = [2, 6, 3, 4, 9, 8, 7, 5, 1]
# 1.修改指定下标数据
# nameList[1]='Tony'
# print(nameList)

# 2.逆序reverse()
# nameList.reverse()
# print(nameList)

# sort() 排序：升序reverse=False 和 降序reverse=True
# numList.sort()
numList.sort(reverse=True)
print(numList)
