"""
@author:Hirsi
@time:2020/5/21 21:05
"""
import random

# 玩家出拳
player = int(input('请出拳: 0=石头，1=剪刀，2=布'))

# 电脑随机出拳
computer = random.randint(0, 2)
print(f'电脑出拳是{computer}')
# computer = 2
if player ==computer:
    print('平手')
elif (player==0 and computer==1) or (player==1 and computer==2) or (player==2 and computer==0):
    print('玩家获胜')
else:
    print('电脑获胜')



