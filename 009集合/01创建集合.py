"""
@Author:Hirsi
@Time:2020/5/30 0030 7:53
"""

"""
set()集合有去重的特点
"""
s1 = {10, 20, 30, 40, 50}
print(s1)

s2 = {10, 20, 30, 40, 50, 20, 30}
print(s2)

s3 = set('abcdefg')
print(s3)

s4 = set()
print(s4)
print(type(s4))

s5 = {}
print(type(s5))
