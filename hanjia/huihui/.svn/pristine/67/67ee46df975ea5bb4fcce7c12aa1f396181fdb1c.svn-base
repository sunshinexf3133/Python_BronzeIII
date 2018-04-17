#coding:utf-8
#返回函数_函数作为返回值

#实现一个可变参数的求和
def calc_sum(*args) :
    ax = 0
    for n in args :
        ax = ax + n
    return ax

#如果不需要立刻求和，而是在后面的代码中，根据需要再计算怎么办？
#可以不返回求和的结果，而是返回求和的函数！
def lazy_sum(*args) :
    def sum() :
        ax = 0
        for n in args :
            ax = ax + n
        return ax
    return sum

if __name__ == "__main__" :
    print calc_sum(1,2,3,4,5)
    print '-----------------------'
    f = lazy_sum(1,3,5,7,9)
    print f
    print '-----------------------'
    print f()
    print '-----------------------'
    f1 = lazy_sum(1,3,5,7,9)
    f2 = lazy_sum(1,3,5,7,9)
    print f1 == f2
