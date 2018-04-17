#coding:utf-8
#filter函数
#素数的判断有待好好研究

#请尝试用filter()删除1-100的素数

import math

def PrimeNumber(n) :
    flag = 0
    for i in range(2,int(math.sqrt(n) + 1)) :
        if n % i == 0 :
            flag = 1
            break
    if flag == 1 :
        return n

        
    

if __name__ == "__main__" :
    print filter(PrimeNumber,range(1,101))
