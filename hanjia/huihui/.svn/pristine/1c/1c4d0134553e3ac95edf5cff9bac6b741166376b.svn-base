#coding:utf-8
#使用列表解析进行筛选

def filter_used() :
    """列表解析返回一个列表，该列表只包含列表nums中的正数"""
    nums = [-1,0,8,6,-3,6,4,-9,-2]
    result = [n for n in nums if n > 0]
    return result


def filter_unused() :
    """未使用列表解析，返回一个列表，该列表只包含列表nums中的正数"""
    result = []
    nums = [-1,0,8,6,-3,6,4,-9,-2]
    for n in nums :
        if n > 0 :
            result.append(n)
    return result

if __name__ == "__main__" :
    a = filter_used()
    b = filter_unused()

    print('filter_used():{}\nfilter_unused():{}\n'.format(a,b))
