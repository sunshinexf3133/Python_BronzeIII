#coding:utf-8

def findMinAndMax(L):
    if L == []:
        return (None,None)
    else:

        min = L[0]
        max = L[0]

        for i in L:
            if i > max:
                max = i
            if i < min:
                min = i
           

        return (min,max)

def main():
    if findMinAndMax([]) != (None,None):
        print('测试失败！')
    elif findMinAndMax([7]) != (7,7):
        print('测试失败！')
    elif findMinAndMax([7,1]) != (1,7):
        print('测试失败！')
    elif findMinAndMax([7,1,3,9,5]) != (1,9):
        print('测试失败!')
    else:
        print('测试成功！')


if __name__ == '__main__':
    main()
                
            
