"""
@author:Hirsi
@time:2020/6/1 21:48
"""

list1=[]
for i in range(1,3):
    for j in range(3):
        list1.append((i,j))
print(list1)

list2=[(i,j) for i in range(1,3) for j in range(3)]
print(list2)