#coding:utf-8
#返回函数_闭包
#?略有一点点懵逼

def count() :
    fs = []
    for i in range(1,4) :
        def f() :
            return i * i
        fs.append(f)
    return fs

if __name__ == "__main__" :
    f1,f2,f3 = count()
    print f1(),f2(),f3()
