"""
@Author:Hirsi
@Time:2020/6/14
"""

"""自定义的模块"""


"""
用from 模块名 import *  方法调用的模块，在all列表中的函数，才能使用
"""
__all__=['testB']

def testA(a, b):
    print(a + b)


def testB():
    print('testB')

def testC():
    print('testC')

# __name__是系统变量，是模块的标识符，运行自身模块它的值就是__main__,否则是当前模块的名字
if __name__ == '__main__':
    testA(1, 2)
    print(__name__)
