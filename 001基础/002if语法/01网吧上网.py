"""
@author:Hirsi
@time:2020/5/21 20:21
"""
"""
if False:
    print("条件成立执行001")
else:
    print("else执行的代码")

# 不带缩进的代码不属于if
print("不成立执行的代码")
"""

"""
年龄大于18，就可以上网，不然就不能上网
"""
age = int(input("请输入你的年龄:"))

if age>=18:
    print(f'{age}岁成年了，可以上网了')
else:
    print('%d岁，未成年，不可以上网' %age)

print('系统关闭~')
