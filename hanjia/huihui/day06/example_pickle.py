#coding:utf-8
#python模块pickle执行的操作通常被称为对象串行化（简称串行化）
#其基本思想是，将复杂的数据结构转换为字节流，即创建数据结构串行化表示
#
#使用pickle.dump将数据结构存储到磁盘，以后再使用pickle.load从
#磁盘获取数据结构
#？没太熟悉
#picklefile.py

import pickle

def make_pickled_file() :
    grades = {'alan' :[4,8,10,10],
              'tom' :[7,7,7,8],
              'dan' :[5,None,7,7],
              'may' :[10,8,10,10]}
    outfile = open('grades.dat','wb')
    pickle.dump(grades,outfile)
    return

def get_pickled_data() :
    infile = open('grades.dat','rb')
    grades = pickle.load(infile)
    return grades

if __name__ == "__main__" :
    make_pickled_file()
    get_pickled_data()
