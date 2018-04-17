#coding:utf-8

import math

def quadratic(a,b,c):
   # float p,x1,x2
    
    p = b * b - 4 * a * c
    
    if(p < 0):
        print('Unsolvable')
        return 0
    elif(p == 0):
        x1 = - b / (2 * a)
        x2 = x1
        print('x1 = x2 =',x1)
        return x1,x2
    else:
        x1 = (- b + math.sqrt(p)) / (2 * a)
        x2 = (- b - math.sqrt(p)) / (2 * a)
        print('x1 = ',x1)
        print('x2 = ',x2)
        return x1,x2


