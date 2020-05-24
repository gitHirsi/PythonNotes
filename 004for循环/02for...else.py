"""
@author:Hirsi
@time:2020/5/23 22:14
"""

stri = 'hirsiboom'

for s in stri:
    if s == 'b':
        # print('遇到b不打印')
        # continue
        break
    print(s)
else:
    print('\n完成')
