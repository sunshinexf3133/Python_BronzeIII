#coding:utf-8
#装饰器

#请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。


import functools

def log(func) :
    @functools.wraps(func)
    def wrapper(*args,**kw) :
        print 'begin call %s():' %func.__name__
        res = func(*args,**kw)
        print 'end call %s():' %func.__name__
        return res
    return wrapper

@log
def now() :
    print '2016-5-30'

if __name__ == "__main__" :
    now()


