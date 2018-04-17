#coding:utf-8
#高级特性_生成器

#斐波拉契数列（Fiboncci）函数
#def fib(max) :
#    n,a,b = 0,0,1
#    while n < max :
#        print b
#        a,b = b,a + b
#        n = n + 1
#    return

#把上面的函数变成generator
def fib(max) :
    n,a,b = 0,0,1
    while n < max :
        yield b
        a,b = b, a + b
        n = n + 1
    return

def odd() :
    print 'step 1'
    yield 1
    print 'step 2'
    yield 3
    print 'step 3'
    yield 5

def invoke_fib(max) :
    for n in fib(max) :
        print n
    return 

if __name__ == "__main__" :
    print fib(6)
    print '---------------------------'
    print '---------------------------'
    o = odd()
    print o.next()
    print '---------------------------'
    print o.next()
    print '---------------------------'
    print o.next()
    print '---------------------------'
    #print o.next()
    print '---------------------------'
    print '---------------------------'
    invoke_fib(6)
   # fib(8)
