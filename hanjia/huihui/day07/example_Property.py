#coding:utf-8
#特性装饰器
#?p.age = -4
#?print p.age   为啥输出是-4
#####小懒懒课堂（依旧不太理解，日后多做练习）
#!python2.7里面类Person需要继承object，这样的话，该类才是个新式类
#才会有setter，getter
#新类型实例除了拥有传统类实例的全部特例之外，还拥有一种称为property
#的新属性及一个叫做__slots__的特殊属性，该属性会对实例其他属性的访问
#产生重要影响，新的对象模型同样添加了一个新的方法__getattribute__
#比原有的__getattr__方法更通用。不同的实例可以拥有这些特殊方法的不同实现
#####
#这个版本的函数，将底层变量self.age重命名为self._age。
#这里使用这种方法将这个变量与方法age区分开来。
#example_property.py

class Person(object):
    def __init__(self,name = '',age = 0) :
        self._name = name
        self._age = age

    #获取函数返回变量的值，我们将使用@property装饰器来指出这一点
    #这个age方法除必不可少的self外不接受任何参数。我们在它前面加
    #上@property，指出这是一个获取函数。这个方法的名称将被用于设
    #置变量

    @property
    def age(self) :
        """Returns this person's age."""
        return self._age

#    def set_age(self,age) :
 #       if 0 < age <= 150 :
  #          self._age = age
        

    def display(self) :
        print(self)

    def __str__(self) :
        return "Person('%s',%s)" %(self._name,self._age)

    def __repr__(self) :
        return str(self)

    #为给age创建设置函数，我们将方法set_age重命名为age，并使用
    #@age.setter进行装饰
    @age.setter
    def age(self,age) :
        if 0 < age <= 150 :
            self._age = age

if __name__ == "__main__" :
    p = Person('LaLa',23)
    print str(p)
    print '-----------'
    print p.age
    p.age = -4
    
    print p.age
    p._age = -4
    print p._age
    print '-----------'
    print str(p)
    
    
