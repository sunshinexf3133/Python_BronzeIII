#coding:utf-8
#列表解析示例

def fun1() :
    """将列表中的每个数字翻倍并加上7"""
    return [2 * n + 7 for n in range(1,11)]

def fun2() :
    """创建一个列表，它包含前10个自然数的立方"""
    return [n ** 3 for n in range(1,11)]

def fun3() :
    """在列表解析中使用字符串"""
    return [c for c in 'pizza']

def fun4() :
    """将所给字符串的每个字母都大写"""
    return [c.upper() for c in 'pizza']

def fun5() :
    """列表解析的一种常见用途是，以某种方式修改现有列表"""
    names = ['al','xiao','lan','lan']
    cap_names = [n.capitalize() for n in names]
    #print (' names:{}\n cap_names:{}\n'.format(names,cap_names)
    return cap_names
    

if __name__ == "__main__" :
    a = fun1()
    b = fun2()
    c = fun3()
    d = fun4()
    e = fun5()

    print (' fun1():{}\n fun2():{}\n fun3():{}\n fun4():{}\n fun5():{}'.
           format(a,b,c,d,e))
