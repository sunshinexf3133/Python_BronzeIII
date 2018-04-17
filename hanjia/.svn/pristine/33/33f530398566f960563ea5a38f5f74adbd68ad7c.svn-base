#coding:utf-8
#尾递归优化

#计算阶乘n! = 1 x 2 x 3 x ... x n
def fact(n) :
    return fact_iter(n,1)

def fact_iter(num,product) :
    if num == 1 :
        return product
    return fact_iter(num - 1,num * product)

if __name__ == "__main__" :
    print fact(4)
