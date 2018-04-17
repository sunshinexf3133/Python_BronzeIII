#coding:utf-8
#装饰器（Decorator）

import functools

def log(func) :
    @functools.wraps(func)
    def wrapper(*args,**kw) :
        print 'call %s() :'%func.__name__
        return func(*args,**kw)
    return wrapper

@log
def now() :
    print '2016-5-30'

if __name__ == "__main__" :
    now()
