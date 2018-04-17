#coding:utf-8
#继承和多态

class Animal(object) :
    def run(self) :
        print 'Animal is running...'

class Dog(Animal) :
    def run(self) :
        print 'Dog is running...'
    def eat(self) :
        print 'Eating meat...'

class Cat(Animal) :
    def run(self) :
        print 'Cat is running...'

        
def run_twice(animal) :
    animal.run()
    animal.run()

class Tortoise(Animal) :
    def run(self) :
        print 'Tortoise is running slowly...'
    

if __name__ == "__main__" :
    dog = Dog()
    cat = Cat()
    dog.run()
    cat.run()
    print '--------------'
    run_twice(Animal())
    print '--------------'
    run_twice(Dog())
    print '--------------'
    run_twice(Tortoise())
    
