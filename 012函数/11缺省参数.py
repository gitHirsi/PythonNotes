"""
@Author:Hirsi
@Time:2020/6/5 21:46
"""

"""
就是默认参数
    所有位置参数，必须在默认参数前面，包括定义和调用
"""
def userInfo(name, age, gender='男'):
    print(f'你的名字是:{name},年龄是:{age},性别是:{gender}')

# userInfo('Tony',30)
userInfo('Tony',30,'女')