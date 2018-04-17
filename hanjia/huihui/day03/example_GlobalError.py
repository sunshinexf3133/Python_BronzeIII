#-*-coding:utf-8-*-
##全局变量
##修改全局变量的方法不对的代码，以下为错误示范
#global_error.py

name = 'Jack'
def say_hello() :
    print('Hello ' + name + '!')
def change_name(new_name):
    name = new_name
