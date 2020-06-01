"""
@author:Hirsi
@time:2020/6/1 21:31
"""
list1 = []

# ----while()循环实现----
# i = 0
# while i < 10:
#     list1.append(i)
#     i += 1
# print(list1)
# print('-' * 30)

# for循环实现
# for i in range(10):
#     list1.append(i)
# print(list1)

# 列表推导式实现

list2 = [i for i in range(10)]
print(list2)

list3 = [i for i in range(0, 10, 2)]
print(list3)

list4 = [i for i in range(10) if i % 2 == 0]
print(list4)
