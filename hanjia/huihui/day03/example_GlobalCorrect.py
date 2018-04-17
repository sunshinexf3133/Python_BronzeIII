#-*-coding:utf-8-*-
##全局变量
##修改全局变量正确示范如下
#global_correct.py

name = 'Jack'
def say_hello() :
    print('Hello ' + name + '!')
def change_name(new_name) :
    global name
    name = new_name
