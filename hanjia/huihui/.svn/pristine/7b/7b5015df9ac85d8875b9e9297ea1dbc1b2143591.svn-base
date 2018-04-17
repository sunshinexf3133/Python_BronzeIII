#coding:utf-8
#捕获异常
###假设你要从用户那里获取一个整数，为此你反复提示用户
###直到用户输入有效的整数
#get_age.py

def get_age() :
    while True :
        try :
            n = int(raw_input('How  old  are  you?'))
            return n
        except ValueError :
            print('Please enter an integer value.')

    return

if __name__ == "__main__" :
    print ('You are '+str(get_age())+ ' years old.')
