"""
@Author:Hirsi
@Time:2020/6/14
"""
"""
1.import 模块名
2.from 模块名 import 功能名1，功能2，功能3... 
3.from 模块名 import * 
4.定义别名：只能通过别名调用了
     模块定义别名： import 模块名 as 别名
     功能定义别名： from 模块名 import 功能名 as 别名
"""

# # 方法1
# import math
#
# # math模块的sqrt()：开平方
# result = math.sqrt(36)
# print(result)

# #方法2 ,直接调用功能，不需要书写  模块名.功能
# from math import sqrt
#
# print(sqrt(25))


# # 方法3
# from math import *
#
# print(sqrt(49))

# 4
# import math as mm

# print(mm.sqrt(9))

from math import sqrt as ss

print(ss(81))

