#coding:utf-8
#map函数

#把函数f(x) = x ^ 2作用在一个list[1,2,3,4,5,6,7,8,9]上
def f(x) :
    return x * x

if __name__ == "__main__" :
    #用map()函数实现
    #print map(f,[1,2,3,4,5,6,7,8,9])
    print '------------------------------------'
    
    #用for循环实现
    L = []
    for n in [1,2,3,4,5,6,7,8,9] :
        L.append(f(n))
    print L
    print '------------------------------------'

    #把list[1,2,3,4,5,6,7,8,9]所有数字转为字符串
    print map(str,[1,2,3,4,5,6,7,8,9])
    print '------------------------------------'
