"""
@Author:Hirsi
@Time:2020/6/5 16:14
"""


def testB():
    print('-----B Function start-----')
    print('-----B Function end-----')


def testA():
    print('-----A Function start-----\n')
    testB()
    print('\n-----A Function end-----')

testA()
