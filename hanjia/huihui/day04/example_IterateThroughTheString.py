#coding:utf-8
###使用for循环访问字符
#codesum1()使用for循环时，在循环的每次迭代开头，都会将循环变量c设置
#为s中的下一个字符。使用索引访问s中字符的工作由for循环自动处理
#codesum2()使用了常规字符串索引，这种与codesum1()相比更为复杂，可读性更差
#codesum.py

def codesum1(s) :
    """Returns the sums of the character codes of s."""
    total = 0
    for c in s :
        total = total + ord(c)
    print total
    return total

def codesum2(s) :
    """Return the sums of the character codes of s."""
    total = 0
    for i in range(len(s)) :
        total = total + ord(s[i])
    print total
    return total



if __name__ == "__main__":
     codesum1("abc")
     codesum2("abd")
   # print a
