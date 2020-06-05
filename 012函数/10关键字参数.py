"""
@Author:Hirsi
@Time:2020/6/5 21:37
"""

"""
通过“键=值”的形式加以指定，不用考虑参数的位置顺序
"""

def userInfo(name, age, gender):
    print(f'你的名字是:{name},年龄是:{age},性别是:{gender}')


# userInfo('Hirsi', 20, '男')


userInfo('Hirsi',gender='男',age=25) #'Hirsi'是位置参数，必须在关键字参数前面
