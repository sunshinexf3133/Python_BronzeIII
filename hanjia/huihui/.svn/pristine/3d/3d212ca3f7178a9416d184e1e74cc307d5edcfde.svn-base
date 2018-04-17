#coding:utf-8
#定制类__getattr__

class Student(object) :
    def __init__(self) :
        self.name = 'XLL'

    def __getattr__(self,attr) :
        if attr == 'score' :
            return 99
        elif attr == 'age' :
            return lambda : 25
        raise AttributeError('\'Student\' object has no attribute \' %s \'' %attr)

if __name__ == "__main__" :
    s = Student()
    print s.name
    print s.score
    print s.age()
    print s.grade
