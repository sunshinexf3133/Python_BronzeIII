#coding:utf-8
#filter()函数：把传入的函数依次作用于每个元素，
#然后根据返回值是True还是False决定保留还是丢弃该元素

#在一个list中，删掉偶数，只保留奇数
def is_odd(n) :
    return n%2 == 1

def not_empty(s) :
    return s and s.strip()

if __name__ == "__main__" :
    print filter(is_odd,[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
    print '---------------------------------'
    print filter(not_empty,['A','','B',None,'C',''])
