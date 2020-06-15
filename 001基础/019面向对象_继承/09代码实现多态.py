"""
@Author:Hirsi
@Time:2020/6/12
"""

class Dog(object):
    def work(self):
        print('指哪咬哪...')

class ArmyDog(Dog):
    def work(self):
        print('追缉敌人~')

class DrugDog(Dog):
    def work(self):
        print('追缉毒品~')

class Person(object):
    def work_with_dog(self,dog):
        dog.work()

ad=ArmyDog()
dd=DrugDog()

p=Person()

p.work_with_dog(ad)
p.work_with_dog(dd)




