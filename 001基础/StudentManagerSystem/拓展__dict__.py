"""
@Author:Hirsi
@Time:2020/6/15
"""

class A(object):
    a=0

    def __init__(self):
        self.b='hirsi'
        self.c='男'
        self.d=3356


aa=A()

print(A.__dict__)
print(aa.__dict__)