"""
@author:Hirsi
@time:2020/5/24 14:28
"""



myStr = 'hello world and itcast and itheima and Python'

#1.find()
# print(myStr.find('and'))          #12
# print(myStr.find('and',15,30))    #23
# print(myStr.find('ands'))         #-1

#2.index()
# print(myStr.index('and'))         #12
# print(myStr.index('and',15,30))   #23
# print(myStr.index('ands'))        #如果index查找，不存在会报错

# 3.count
# print(myStr.count('and'))           #3
# print(myStr.count('and',15,30))     #1
# print(myStr.count('ands'))          #0

#4.rfind()  --从右边开始查找
# print(myStr.rfind('and'))          #12
# print(myStr.rfind('ands'))         #-1

#5.rindex() --从右边开始查找
print(myStr.rindex('and'))         #12
print(myStr.rindex('and',15,45))   #23
print(myStr.rindex('ands'))        #如果rindex查找，不存在会报错




