#coding:utf-8
#map/reduce

#python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，
#可以接受一个list并利用reduce()求积。

def prod(s) :
    return reduce(lambda x,y:x*y,s)

if __name__ == "__main__" :
    print prod([1,2,3,4,5])
