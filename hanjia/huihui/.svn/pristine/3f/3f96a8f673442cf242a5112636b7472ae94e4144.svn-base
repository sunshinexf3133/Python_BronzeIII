#coding:utf-8
#函数的参数_可变参数

#请计算a^2 + b^2 + c^2 +...
def calc(*numbers) :
    sum = 0
    for n in numbers :
        sum = sum + n * n
    return sum

if __name__ == "__main__" :
    print calc(1,2,3)
    print '---------------------------'
    print calc()

    #已有一个list或者tuple，要调用一个可变参数的情况
    nums = [1,2,3]
    print '---------------------------'
    print calc(nums[0],nums[1],nums[2])
    print '---------------------------'
    print calc(*nums)
