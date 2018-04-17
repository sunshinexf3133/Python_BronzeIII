#coding:utf-8

def createCounter():
    def f():
        x = 0
        while True:
            x += 1
            yield x
    it = f()
    def number():
        return next(it)
    return number

       
def main():
    counterA = createCounter()
    print(counterA(),counterA(),counterA(),counterA(),counterA())
    counterB = createCounter()
    if [counterB(),counterB(),counterB(),counterB()] == [1,2,3,4]:
        print('测试通过！')
    else:
        print('测试失败！')

if __name__ == '__main__':
    main()
