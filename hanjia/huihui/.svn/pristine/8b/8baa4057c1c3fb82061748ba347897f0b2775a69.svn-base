#coding:utf-8
#定制类__iter__

class Fib(object) :
    def __init__(self) :
        self.a,self.b = 0,1

    def __iter__(self) :
        return self

    def next(self) :
        self.a,self.b = self.b,self.a + self.b
        if self.a > 100000 :
            raise StopIteration() 
        return self.a

    def __getitem__(self,n) :
        if isinstance(n,int) :
            a,b = 1,1
            for x in range(n) :
                a,b = b,a + b
            return a
        if isinstance(n,slice) :
            start = n.start
            stop = n.stop
            a,b = 1,1
            L = []
            for x in range(stop) :
                if x >= start :
                    L.append(a)
                a,b = b,a + b
            return L

#    def __getitem__(self,n):
#        a,b = 1,1
#        for x in range(n) :
#            a,b = b,a + b
#        return a
    


if __name__ == "__main__" :
    for n in Fib() :
        print n

    print '-----------'
    f = Fib()
    print f[0],f[1],f[2],f[3],f[10]
    print range(100)[5:10]
    print f[0:5],f[:10]
    print f[:10:2]
    
