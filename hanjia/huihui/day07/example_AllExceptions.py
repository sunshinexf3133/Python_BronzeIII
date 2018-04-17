#coding:utf-8
#捕获多种异常
###convert_to_int(s,base)的作用是将s（通常是一个字符串）
###按照base进制转换成整数


def convert_to_int1(s,base) :
    try :
        return int(s,base)
    except (ValueError,TypeError) :
        return 'error'

def convert_to_int2(s,base) :
    try :
        return int(s,base)
    except ValueError :
        return 'value error'
    except TypeError :
        return 'type error'

def convert_to_int3(s,base) :
    try :
        return int(s,base)
    except :
        return 'error'
    

if __name__ == "__main__" :
    print convert_to_int1('9',10)
    print convert_to_int2('B',16)
    print convert_to_int3('110',8)
