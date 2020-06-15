"""
@Author:Hirsi
@Time:2020/6/15
"""

"""
方法一
    import 包名.模块名
"""
# import mypackage.my_module1
#
# mypackage.my_module1.info_print1()

"""
方法二
    from 包名 import * 
    模块名.目标
    必须要__init__.py文件中添加__all__=[],控制允许导入的模块列表
"""
from mypackage import *

my_module1.info_print1()