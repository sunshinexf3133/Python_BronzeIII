#coding:utf-8
#reduce函数
#map(f,list[....])
#reduce(f(),list[....])

#对序列求和，用reduce实现
def add(x,y) :
    return x + y

#把序列[1,3,5,7,9]变换成整数13579
def fn(x,y) :
    return x * 10 + y

#把str转换为int的函数
def char2num(s) :
    return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]

if __name__ == "__main__" :
    print reduce(add,[1,3,5,7,9])
    print '---------------------------------'
    print reduce(fn,[1,3,5,7,9])
    print '---------------------------------'
    #把str转换为int的函数
    print reduce(fn,map(char2num,'13579'))
