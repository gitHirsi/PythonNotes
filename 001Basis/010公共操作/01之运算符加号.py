"""
@Author:Hirsi
@Time:2020/5/30 0030 8:40
"""

"""
+ :合并  支持  字符串，列表，元组
"""
str1 = 'hirsi'
str2 = 'boom'

list1=[10,20,30]
list2=[60,80]

t1=('aa','bb')
t2=('cc','FF','MM')

dict1={'name':'Tom','age':26}
dict2={'id':300,"teacher":'haha'}

print(str1+str2)
print(list1+list2)
print(t1+t2)

# + 不支持合并字典
# print(dict1+dict2)
