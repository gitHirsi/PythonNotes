"""
@Author:Hirsi
@Time:2020/5/30 0030 8:21
"""

s1 = {10, 20, 30, 60, 50}

# remove()删除制定数据，没有则报错
# s1.remove(20)
# s1.remove(80)
# print(s1)

# discard()  输出指定数据，没有也不报错
# s1.discard(50)
# s1.discard(90)
# print(s1)

# pop()随机删除数据，并返回删除的数据，集合随机排列的第一个数据
pop = s1.pop()
print(s1)
print(pop)
