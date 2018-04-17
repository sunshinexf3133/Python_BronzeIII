#coding:utf-8
#使用@property

class Student(object) :

    @property
    def birth(self) :
        return self._birth

    @birth.setter
    def birth(self,value) :
        self._birth = value

    @property
    def age(self) :
        return 2014 - self._birth

if __name__ == "__main__" :
    s = Student()
    s.birth = 2010
    print s.birth
    print s.age
    
