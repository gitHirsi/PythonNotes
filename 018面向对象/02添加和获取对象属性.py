"""
@Author:Hirsi
@Time:2020/6/11 16:34
"""

# 类里面获取对象名 self.属性名
class Washer():
    def wash(self):
        print('洗衣服了！')


    def printInfo(self):
        print(f'宽：{self.width}')
        print(f'高：{self.height}')


haier=Washer()


# 在类外面添加对象属性
haier.width=600
haier.height=700

# 在类外面获取对象属性
# print(f'宽:{haier.width}')
# print(f'高:{haier.height}')


haier.printInfo()