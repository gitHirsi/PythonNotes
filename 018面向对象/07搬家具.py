"""
@Author:Hirsi
@Time:2020/6/11 22:32
"""


# 定义家具类   两个属性：名字和占地面积
class Furniture():
    def __init__(self, name, area):
        self.name = name
        self.area = area


# 定义房屋类  4个属性：地理位置，房屋面积，剩余面积，家具列表
class House():
    def __init__(self, address, area):
        self.address = address
        self.area = area
        self.free_area = area
        self.furniture = []

    def add_furniture(self, item):
        """添加家具方法"""
        if self.free_area >= item.area:
            self.furniture.append(item.name)
            self.free_area -= item.area
        else:
            print('家具太大，剩余空间无法容纳！')

    def __str__(self):
        return f'房子坐落于{self.address},占地面积是{self.area}㎡，' \
               f'剩余空间{self.free_area}㎡,里面的家具有{self.furniture}'


bed = Furniture('双人床', 6)
sofa = Furniture('沙发', 12)
piano=Furniture('豪华钢琴',115)

house = House('武汉', 120)
house.add_furniture(bed)
house.add_furniture(sofa)
house.add_furniture(piano)
print(house)
