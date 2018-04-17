#coding:utf-8
#返回函数_闭包

#返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量
#如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，
#无论该循环变量后续如何更改，已绑定到函数参数的值不变：
def count() :
    fs = []
    for i in range(1,4) :
        def f(j) :
            def g() :
                return j * j
            return g
        fs.append(f(i))
    return fs

if __name__ == "__main__" :
    f1,f2,f3 = count()
    print f1(),f2(),f3()
