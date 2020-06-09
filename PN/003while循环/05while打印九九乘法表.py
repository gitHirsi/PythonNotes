"""
@author:Hirsi
@time:2020/5/22 22:22
"""

x = 1
while x <= 9:
    y = 1
    while y <= x:
        # print(f'{y}*{x}={x * y}', end='\t')
        print('%d*%d=%d' % (y, x, x * y), end='\t')
        y += 1

    print()

    x += 1
