"""
@Author:Hirsi
@Time:2020/6/11 23:16
"""

class A(object):
    def __init__(self):
        self.num=1

    def print_num(self):
        print(self.num)

# B类继承A类
class B(A):
    pass


b=B()
b.print_num()

