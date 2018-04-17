#coding:utf-8
#匿名函数

def build(x,y) :
    return lambda : x * x + y * y

if __name__ == "__main__" :
    print map(lambda x : x * x,[1,2,3,4,5,6,7,8,9])
    f = build(1,2)
    print f
