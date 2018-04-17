#coding:utf-8
#map/reduce

#资料：
#法一：capitalize()首字母大写，其余字母均为小写
#法二：upper()将字母变为大写，lower()将字母变为小写

#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字
#输入：['adam','LISA','barT'],输出：['Adam','Lisa','Bart']

#法二
def StandardName(x) :
    return x[0].upper()+x[1:].lower()
    

if __name__ == "__main__" :
    #法一
    print map(lambda s:s.capitalize(),['adam','LISA','barT'])
    print '--------------------------------------------------'
    #法二
    print map(StandardName,['adam','LISA','barT'])
    print '--------------------------------------------------'
