"""
@Author:Hirsi
@Time:2020/6/11 16:49
"""

"""
定义init魔法方法，设置初始化属性，并访问调用
"""
# class Washer():
#     def __init__(self):
#         self.width = 600
#         self.height = 700
#
#     def printInfo(self):
#         print(f'宽:{self.width}')
#         print(f'高:{self.height}')
#
# haier=Washer()
# haier.printInfo()

# __init__（）不需要手动调用，里面的self参数也不需要开发者传递，python解释器会自动把当前对象引用传递过去

"""带参数的__init__（）"""
# 一个类创建多个对象，设置不同的初始化属性
class Washer():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def printInfo(self):
        print(f'宽:{self.width}')
        print(f'高:{self.height}')

# 创建对象的时候，传递参数
haier2=Washer(400,650)
haier2.printInfo()

haier3=Washer(555,666)
haier3.printInfo()

