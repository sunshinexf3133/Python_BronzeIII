#coding:utf-8

__author__ = 'Sunshine'


class Animal(object):
    def run(self):
        print('Animal is running..')


class Dog(Animal):

    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eating meat...')


class Cat(Animal):
    def run(self):
        print('Cat is running...')

def run_twice(animal):
    animal.run()
    animal.run()
