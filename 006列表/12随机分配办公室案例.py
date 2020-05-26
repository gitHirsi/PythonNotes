"""
@author:Hirsi
@time:2020/5/26 20:04
"""
import random

teachers = ['AA', 'BB', 'CC', 'DD', 'EE', 'FF', 'GG', 'HH']
offices = [[], [], []]

# 随机分配老师
for t in teachers:
    randint = random.randint(0, 2)
    offices[randint].append(t)

print(offices)

i = 1
for office in offices:
    print(f"{i}号办公室的老师有{len(office)}个:", end='')
    # 如果此办公室没老师，立即换行显示下个办公室的
    if len(office) == 0:
        print()
        continue
    for o in office:
        # 判断是最后一个数据，后面不加 ,
        if o == office[-1]:
            print(o)
        else:
            print(o, end=',')
    i += 1
