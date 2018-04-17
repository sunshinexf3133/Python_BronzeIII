#coding:utf-8
#错误处理_try

#example1
try :
    print 'try...'
    r = 10 / 0
    print 'result :',r
except ZeroDivisionError,e :
    print 'except :',e
finally :
    print 'finally...'
print 'END'

#example2
try :
    print 'try...'
    r = 10 / int('a')
    print 'result :' ,r
except ValueError ,e :
    print 'ValueError :',e
except ZeroDivisionError ,e :
    print 'ZeroDivisionError :' ,e
finally :
    print 'finally...'
print 'END'

#example3
try :
    print 'try...'
    r = 10 / int('a')
    print 'result :',r
except ValueError ,e :
    print 'ValueError :' ,e
else :
    print 'no error !'
finally :
    print 'finally...'
print 'END'

#example4
try :
    foo()
except StandardError ,e :
    print 'StandardError'
except ValueError ,e :
    print 'ValueError'
