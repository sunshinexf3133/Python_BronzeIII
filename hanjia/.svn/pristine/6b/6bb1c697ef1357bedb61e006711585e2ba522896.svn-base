#coding:utf-8
#错误处理_记录错误

import logging

def foo(s) :
    return 10 / int(s)

def bar(s) :
    return foo(s) * 2

def main() :
    try :
        bar('0')
    except StandardError ,e:
        logging.exception(e)

main()
print 'End'
