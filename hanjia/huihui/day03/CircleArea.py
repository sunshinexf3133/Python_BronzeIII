#-*-coding:utf-8-*-
#定义函数
#python文档字符串通常遵循一种标准格式约定：
#用三引号标识文档字符串的开始和结束位置；
#第1行是函数的简要描述，对程序员很有帮助，接下来是详情和示例。
#文档字符串的好处：与内置函数一样，你也可以轻松地查看自己编写的函数的文档字符串
#如在IDEL中输入
#>>>print area.__doc__

###求圆面积
#area.py

import math
def area(radius) :
    """Returns the area of a circle with the given radius.
    For example :
    >>>area(5.5)
    95.033177771091246
    """

    return math.pi * radius ** 2
