#coding:utf-8
#with语句：为了确保即使发生异常，也将尽早执行清理操作（如关闭文件），
#还可使用Python语句with
###下面代码在屏幕上打印文件内容，并给每一行都加上行号。
#example_with.py

def print_nowith(fname):
    num = 1
    f = open(fname)
    for line in f :
        print '%04d %s'%(num,line),
        num = num + 1
    return
def print_with(fname) :
    num = 1
    with open(fname,'r') as f :
        for line in f :
            print '%04d %s'%(num,line),
            num = num + 1
    return

if __name__ == "__main__" :
    print_nowith('test_With.txt')
    print'\n-------------------------'
    print_with('test_With.txt')
