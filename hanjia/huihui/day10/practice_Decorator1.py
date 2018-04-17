#coding:utf-8
#装饰器

#再思考一下能否写出一个@log的decorator，使它既支持：
#@log
#def f() :
#    pass
#又支持：
#@log('execute')
#def f() :
#    pass

import functools

def log(text) :
    def decorator(func) :
        @functools.wraps(func)
        def wrapper(*args,**kw) :
            print 'begin call'
            print ('%s:%s'%(text,func.__name__))
            execute = func(*args,**kw)
            print 'end call'
            return execute
        return wrapper

    if isinstance(text,str) :
        return decorator

    func = text
    text = 'execute'
    return decorator(func)

@log('execute')
def now1() :
    print '2016-5-30'

@log
def now2() :
    print '2016-5-30'
if __name__ == "__main__" :
    now1()
    print '----------------'
    now2()

    
