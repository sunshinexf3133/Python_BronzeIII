#-*-coding:utf-8-*-
#使用main函数
##使用了main函数的密码检查程序
#password2.py

def main() :
    pwd = raw_input('What is the password?')
    if pwd == 'apple' :
        print('Logging on...')
    else :
        print('Incorret password.')
    print('All done!')
