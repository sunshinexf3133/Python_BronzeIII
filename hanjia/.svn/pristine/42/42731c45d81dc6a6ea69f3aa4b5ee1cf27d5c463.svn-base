#coding:utf-8
#装饰器

#如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数。
#比如，要自定义log的文本：

import functools

def log(text) :
    def decorator(func) :
        @functools.wraps(func)
        def wrapper(*args,**kw) :
            print '%s %s():'  %(text,func.__name__)
            return func(*args,**kw)
        return wrapper
    return decorator

@log('execute')
def now() :
    print '2016-5-30'

if __name__ == "__main__" :
    print now()
    print '--------------------------------------'
    print now.__name__
