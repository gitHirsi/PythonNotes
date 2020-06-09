"""
@Author:Hirsi
@Time:2020/6/4 22:23
"""


# def buy():
#     return '❤'*5
#
# goods = buy()
# print(goods)

def sumNum(a, b):
    return a + b


numStr = input("""两个数字求和
请输入(空格隔开): """)
splitNum = numStr.split(' ')
a = int(splitNum[0])
b = int(splitNum[1])

result = sumNum(a, b)
print(result)
