#coding:utf-8
#多进程

#下面的例子演示了启动一个子进程并等待其结束

from multiprocessing import Process
import os

def run_proc(name) :
    print 'Run child process %s (%s)...' %(name,os.getpid())

if __name__ == "__main__" :
    print 'Parent process %s.' %os.getpid()
    p = Process(target = run_proc,args = ('test',))
    print 'Process will start.'
    p.start()
    p.join()
    print 'Process end.'

