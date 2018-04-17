#coding:utf-8
#高阶函数（Higher-order function）_传入参数

def add(x,y,f) :
    return f(x) + f(y)

if __name__ == "__main__" :
    print add(-5,6,abs)
