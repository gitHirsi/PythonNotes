"""
@author:Hirsi
@time:2020/5/21 20:56
"""

money = 1
seat = 0
if money == 1:
    print('可以上车')
    if seat == 1:
        print('有座位可以坐')
    else:
        print('没有钱只能站着')
else:
    print('没有钱无法上车')
