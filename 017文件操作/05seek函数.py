"""
@Author:Hirsi
@Time:2020/6/11 11:39
"""
"""
seek(偏移量，起始位置) 0开头  1当前  2结尾，  默认为0
"""
# r+
# f1 = open('test.txt', 'r+')
#
# f1.seek(3, 0)
# # f1.seek(0, 2)
# print(f1.read())
# f1.close()

# a+
f2 = open('test.txt', 'a+')
f2.seek(2,0)
f2.seek(0,0)
print(f2.read())

f2.close()
