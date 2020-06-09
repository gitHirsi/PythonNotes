"""
@Author:Hirsi
@Time:2020/6/5 21:10
"""

a=100

def testA():
    print(a)

def testB():
    global a #声明a为全局变量
    a=200
    print(a)

testA()
testB()
print(a)

"""
在函数体内修改全局变量，先用global声明该变量为全局的，在进行修改
"""