#coding:utf-8

def product(*kw):
    s = 1
    for i in kw:
        s = s * i

    return  s
