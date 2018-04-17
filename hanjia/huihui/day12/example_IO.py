#coding:utf-8
#文件读写

try :
    f = open('f:/PythonWorkSpace/hanjia/huihui/day12/mydict.py','r')
    print f.read()
finally :
    if f :
        f.close()

print '================================================================'

with open('f:/PythonWorkSpace/hanjia/huihui/day12/mydict.py','r') as f :
    print f.read()

print '================================================================='

with open('f:/PythonWorkSpace/hanjia/huihui/day12/mydict.py','r') as f :
    
    for line in f.readlines() :
        print(line.strip())
