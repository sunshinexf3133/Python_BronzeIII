#coding:utf-8
#编写类
#编写一个表示人的简单类
#person.py

class Person:
    """Class to represent a person"""
    def __init__(self) :
        self.name = ''
        self.age = 0

    def display(self) :
        """将Person对象的内容以适合程序员阅读的
            格式打印到屏幕上"""
        print("Person('%s',%d)" %(self.name,self.age))
        return

    def __str__(self) :
        """该方法用于生成对象的字符串表示"""
        return "Person('%s',%d)" %(self.name,self.age)

    


if __name__ == "__main__" :
    p = Person()
    p.name,p.age = 'Bob',32
    print str(p)
    print '-------'
    p.display()
