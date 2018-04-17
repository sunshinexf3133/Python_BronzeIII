#coding:utf-8
#列表函数
###下面的函数根据传入的数字列表创建一个消息列表
# s.append(x):在列表s末尾添加元素x 
#numnote.py

def numnote(lst) :
    """The function of numnote(lst) is to creat a list of
       messages based on the list of numbers passed in.
    """
    msg = []
    for num in lst :
        if num < 0 :
            s = str(num) + ' is negative'
        elif 0 <= num <= 9 :
            s = str(num) + ' is a digit'
        msg.append(s)
    return msg

if __name__ == "__main__" :
    a = numnote([1,2,3,-4,0,22])
    print a

    for msg in a:
        print msg

    print('__________')

    print('\n'.join(a))
