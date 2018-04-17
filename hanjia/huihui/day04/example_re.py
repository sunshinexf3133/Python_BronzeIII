#coding:utf-8
#使用正则表达式匹配字符串
#编写程序，要求用户必须输入done或quit来结束程序
#???不知道执行之后该返回啥，如果直接在IDEL里调用的话，会返回TRUE或者FALSE
#is_done2(s)中，为了匹配正则表达式，使用了函数re.match(regex,s),
#它在regex与s不匹配时返回None,否则返回一个特殊的正则表达式匹配对象。
#在这个示例中，我们不关心匹配对象的细节，因此只检查返回值是否为None。

#####
#小懒懒老师课堂：
#题目要求用户必须输入done或quit来结束程序，那么
#正确的正则表达式应该为： '^done$|^quit$' （^表示文档开始，$表示文档结束、字符串末尾）
#该正则表达式表示匹配为quit或者done的字符串
#错误的正则表达式： 'done|quit'
#该正则表达式表示匹配以quit或者done开始的字符串，即如果输入quitxxx也可以结束程序
#The function of 're.match' is :
#Try to apply the pattern at the start of the string,
#returning a match object, or None if no match was found.
#即检测这个正则所匹配的子字符串是不是这个字符串的开始
#该题目的正则表达式的正解也可以是： 'quit$|done$'
#allover.py

import re   #使用正则表达式
def is_done1(s) :
    return s == 'done' or s == 'quit'

def is_done2(s) :
    return re.match('^done$|quit$',s) != None



if __name__ == "__main__" :
    a = is_done1('donexxx')
    b = is_done2('quitxxx')
    print a,b



