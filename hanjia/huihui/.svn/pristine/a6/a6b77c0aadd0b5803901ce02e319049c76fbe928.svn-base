#coding:utf-8
#多重继承

class Animal(object) :
    pass

class Mammal(Animal) :
    pass

class RunnableMixin(object) :
    def run(self) :
        print('Running...')


class FlyableMixin(object) :
    def fly(self) :
        print('Flying...')

class CarnivorousMixin(object) :
    pass

class Bird(Animal) :
    pass

class Dog(Mammal,RunnableMixin,) :
    pass

class Bat(Mammal,FlyableMixin) :
    pass

class Parrot(Bird) :
    pass

class Ostrich(Bird) :
    pass



if __name__ == "__main__" :
    a = Dog()
    a.run()
