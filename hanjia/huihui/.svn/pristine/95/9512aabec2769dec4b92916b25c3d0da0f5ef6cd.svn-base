#coding:utf-8
#清理操作
#在try/except块中，可包含执行清理操作的finally代码块
#example_finally.py

def invert(x) :
    try :
        return 1/x
    except  ZeroDivisionError :
        return 'error'
    finally :
        print('invert %s done' %x)

if __name__ == "__main__" :
    print invert(1)
