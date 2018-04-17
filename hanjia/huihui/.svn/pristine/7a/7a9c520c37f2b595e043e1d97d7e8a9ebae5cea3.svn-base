#coding:utf-8
#函数的参数_参数组合
#*args是可变参数，args接收的是一个tuple
#**kw是关键字参数，kw接收的是一个dict

def func(a,b,c = 0,*args,**kw) :
    print 'a = ',a,'b = ',b,'c = ',c,'args = ',args,'kw = ',kw
    return

if __name__ == "__main__" :
    func(1,2)
    print '---------------------------------'
    func(1,2,c = 3)
    print '---------------------------------'
    func(1,2,3,'a','b')
    print '---------------------------------'
    func(1,2,3,'a','b',x = 99)
    print '---------------------------------'
    args = (1,2,3,4)
    kw = {'x' : 99}
    func(*args,**kw) 
