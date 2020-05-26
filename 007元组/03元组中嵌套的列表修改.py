"""
@author:Hirsi
@time:2020/5/26 22:13
"""

t1 = ('aa', 'bb', 'cc', 'dd', 'ee')
t2 = ('aa', 'bb', ['cc', 'dd', 'ee'])

print(t1[1])

# 修改元组中嵌套的列表
t2[2][1]='Hirsi'
print(t2)
