#coding:utf-8

def triangles():
    L,index = [1],0
    while index < n:
        yield L
        L = [1] + [L[i] + L[i + 1] for i in range(len(L) - 1)] +[1]
        index += 1
