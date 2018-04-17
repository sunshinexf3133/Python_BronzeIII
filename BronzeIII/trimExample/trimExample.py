#coding:utf-8

def trim(s):
    if s == '':
        return s
    elif(s[0] != ' ')and (s[-1] != ' '):
            return s
    elif s[0] == ' ':
            return trim(s[1:])
    else:
        return trim(s[0:-1])

def main():
    if trim('hello ') != 'hello':
        print('测试失败！')
    elif trim(' hello') != 'hello':
        print('测试失败！')
    elif trim(' hello ') != 'hello':
        print('测试失败！')
    elif trim(' hello world ') != 'hello world':
        print('测试失败！')
    elif trim('') != '':
        print('测试失败！')
    elif trim('   ') != '':
        print('测试失败！')
    else:
        print('测试成功！')

if __name__ == '__main__':
    main()
