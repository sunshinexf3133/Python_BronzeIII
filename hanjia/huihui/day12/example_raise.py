#coding :utf-8
#´íÎó´¦Àí_Å×³ö´íÎó

class FooError(StandardError) :
    pass

def foo(s) :
    n = int(s)
    if n == 0 :
        raise FooError('invalid value : %s' %s)
    return 10 / n
