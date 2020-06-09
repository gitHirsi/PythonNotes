"""
@author:Hirsi
@time:2020/5/20 19:56
@Software: PyCharm
"""

age = 18
name = 'Hirsi'
weigth = 75.5
stuId = 1
stuId2 = 1000

# 我的名字是x，今年X岁了,体重是X    %s的拓展
print('我的名字是%s，今年%s岁了,体重是%s' %(name,age,weigth))

# 今年我几岁   -- 整数   %d
print('今年我%d岁了' % age)

# 我的名字是   --字符串  %s
print('我的名字是：%s' % name)

# 我的体重是多少公斤   --浮点型   %f  加小数点表示留几位
print('我的体重是%.2f公斤' % weigth)

# 我的学号是    d前面加02，表示输出的整数显示位数，不足以0补全，超出当前位数以原样输出
print('我的学号是%d' % stuId)
print('我的学号是%02d' % stuId)
print('我的学号是%02d' % stuId2)

# 我的名字是x，今年X岁了
print('我的名字是%s，今年%d岁了' % (name, age))
print('我的名字是%s，明年%d岁了' % (name, age+1))

# 我的名字是x，今年X岁了,体重是X，学号是X
print('我的名字是%s，今年%d岁了，体重是%.2f，学号是%04d' %(name,age,weigth,stuId))
