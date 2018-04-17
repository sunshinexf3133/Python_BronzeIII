#coding:utf-8
#函数的参数_关键字参数

def person(name,age,**kw) :
    print 'name:',name,'age:',age,'other:',kw
    return

if __name__ == "__main__" :
    person('XLL1',20)
    person('XLL2',21,city = 'Beijing')
    person('XLL3',22,gender = 'M',job = 'Student')
    print '----------------------------------------------'
    kw = {'city':'Beijing','job':'Student'}
    person('XLL4',23,city = kw['city'],job = kw['job'])
    print '----------------------------------------------'
    person('XLL5',24,**kw)
