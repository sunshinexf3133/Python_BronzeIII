#coding:utf-8
#使用元类_metaclass

class ListMetaclass(type) :
    def __new__(cls,name,bases,attrs) :
        attrs['add'] = lambda self,value:self.append(value)
        return type.__new__(cls,name,bases,attrs)

class MyList(list) :
    __metaclass__ = ListMetaclass

if __name__ == "__main__" :
    L = MyList()
    print L.add(1)
    print L
