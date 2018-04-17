#coding:utf-8
#编写类
#编写一个表示人的简单类(进化版)
#1.用str来简化方法display)
#2.通过添加方法__repr__可控制这里打印的字符串
#3.其实添加了方法__repr__后，可进一步简化方法display：
#  def display(self) :
#       print(self)
#4.重写__init__，这样我们在初始化Person对象时会很简单
#我们在方法__init__中使用了self.name和name（以及self.age和age）。
#变量name指向传入__init__的值，而self.name指向存储在对象中的值。
#使用self更清楚地指出了谁是谁
#person.py

class Person:
    """Class to represent a person"""
    def __init__(self,name = '',age = 0) :
        self.name = name
        self.age = age

    def display(self) :
        """将Person对象的内容以适合程序员阅读的
            格式打印到屏幕上"""
        print(str(self))
        return

    def __str__(self) :
        """该方法用于生成对象的字符串表示"""
        return "Person('%s',%d)" %(self.name,self.age)

    def __repr__(self) :
        return str(self)

    


if __name__ == "__main__" :
    p = Person('Hui',21)
    
    p.display()
    print '-------1-------'
    print str(p)
    print '-------2-------'
    print p
