"""
@Author:Hirsi
@Time:2020/6/5 21:50
"""
"""
不设定个数的参数
"""

# 包裹位置传递

# def userInfo(*args):
#     print(args)
#
# userInfo('Hirsi')
# userInfo('Hirsi',20,'男')

# 包裹关键子传递
def userInfo(**kwargs):
    print(kwargs)


userInfo(name='Hirsi', age=30, gender='男')
