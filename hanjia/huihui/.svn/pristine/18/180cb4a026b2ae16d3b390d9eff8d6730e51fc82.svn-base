#coding:utf-8
#使用了列表解析创建一个由1-10的平方组成的列表
#未使用列表解析创建一个由1-10的平方组成的列表

def unused() :
    result = []
    for n in range(1,11) :
        result.append(n * n)
    return result


def used() :
    return [n * n for n in range(1,11)]

if __name__ == "__main__":
    a = unused()
    b = used()

    print a
    print b
