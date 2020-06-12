"""
@Author:Hirsi
@Time:2020/6/12 22:10
"""
"""
1.定义私有属性和方法
2.获取和修改私有属性值
"""

# 师傅类
class Master(object):
    def __init__(self):
        self.kongfu = '《师傅煎饼果子大法》'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


# 学校类
class School(object):
    def __init__(self):
        self.kongfu = '《学校煎饼果子大法》'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


# 徒弟类
class Prentice(School, Master):
    def __init__(self):
        self.kongfu = '《独创煎饼果子大法》'
        # 定义私有属性
        self.__money = 2000000

    # 定义函数：获取私有属性值
    def get_money(self):
        return self.__money

    # 定义函数:修改私有属性值
    def set_money(self,money):
        self.__money=money
        # self.__money=600    #也可不穿参数money，直接赋值

    # 定义私有方法
    def __info_print(self):
        print('这是私有方法')

    def make_cake(self):
        self.__init__()
        print(f'运用{self.kongfu}制作煎饼果子')

    def make_Master_cake(self):
        Master.__init__(self)
        Master.make_cake(self)

    def make_School_cake(self):
        School.__init__(self)
        School.make_cake(self)

# 徒孙类
class TuSun(Prentice):
    pass


QQ = TuSun()
# print(QQ.money)    # money定义私有后，无法访问
# QQ.info_print()    # info_money定义私有后，无法访问
print(QQ.get_money())

QQ.set_money(12138)

print(f'修改后：{QQ.get_money()}')