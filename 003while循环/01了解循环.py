"""
@author:Hirsi
@time:2020/5/21 21:48
"""
a = 1
# while a < 10:
#     print(f'我错了,第{a+1}次')
#     a += 1

while a <= 5:

    if a == 3:
        print('吃到虫子')
        a += 1
        continue  #continue之前要写计时器

    print(f'吃了{a}个')
    a += 1