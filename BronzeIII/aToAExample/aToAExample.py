#coding:utf-8

def aToA(*L):
    return [s.lower() for s in L if(isinstance(s,str))]

def main():
    L1 = ['Hello','World',18,'Apple',None]
    L2 = aToA(*L1)
    print(L2)
    if L2 == ['hello','world','apple']:
        print('测试通过！')
    else:
        print('测试失败！')


if __name__ == '__main__':
    main()
