"""
@Author:Hirsi
@Time:2020/6/11 23:22
"""

"""
单继承:一个父类继承给一个子类，这种单一的继承关系
"""

class Master(object):
    def __init__(self):
        self.kongfu='《煎饼果子大法》'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

class Prentice(Master):
    pass


pre=Prentice()
pre.make_cake()