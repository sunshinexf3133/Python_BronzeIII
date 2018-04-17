#coding:utf-8

def move(n,a,b,c):
    if n == 1 :
        print(a, '--->',c) #只有1个盘子，A-->C
    else:
        move(n - 1,a,c,b) #有n个盘子，借助于C，A(n-1)-->B
        move(1,a,b,c) #A上的最后一个盘子--> C
        move(n - 1,b,a,c) #B上的n-1个盘子借助A移到C上
