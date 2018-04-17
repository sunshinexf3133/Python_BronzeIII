#coding:utf-8
#切片示例，这个函数返回文件名中的扩展名
#函数get_txt的工作原理如下：确定最右边的'.'的索引（因此使用rfind从右往左查找）；
#如果fname不包含'.',则返回一个空字符串，否则返回'.'后面的所有字符
#extension.py

def get_ext(fname) :
    """Returns the extension of file fname."""
    dot = fname.rfind('.')
    if dot == -1:
        return ' '
    else :
        return fname[dot + 1 :]

if __name__ == "__main__":
    a = get_ext('hello.txt')
    b = get_ext('pizza.py')
    c = get_ext('pizza.od.c')
    d = get_ext('pizza')
    print a,b,c
    print d
    #print a
