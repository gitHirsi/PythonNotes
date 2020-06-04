"""
@author:Hirsi
@time:2020/5/21 20:47
"""

age = 30

# if (age >= 16) and (age <= 60):
if 18 <= age <= 60:  #化简
    print('可以上班！')
elif age >= 60:
    print('已经退休了！')
else:
    print("未成年不能上班!")
