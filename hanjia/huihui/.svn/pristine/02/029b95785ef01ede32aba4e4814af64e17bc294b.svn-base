#coding:utf-8
#正则表达式符号与方法
#findall:匹配所有符合规律的内容，返回包含结果的列表

import re
#from re import findall,S,search,sub
secret_code = 'hadkfalifexxIxxfasdjifja134xxlovexx23345sdxxyouxx8dfse'

'''
#.的使用举例
#.:匹配任意字符，换行符\n除外
a = 'xy123'
b = re.findall('x...',a)
print b
'''

'''
#*的使用举例
#*：匹配前一个字符0次或者无限次
a = 'xyxy123'
b = re.findall('x*',a)
print b
'''

'''
#?的使用举例
#?:匹配前一个字符0次或者1次
a = 'xy123'
b = re.findall('x?',a)
print b
'''

'''
# #.*的使用举例
#.*：贪心算法
b = re.findall('xx.*xx',secret_code)
print b

#.*?的使用举例
#.*?:非贪心算法
c = re.findall('xx.*?xx',secret_code)
print c

#使用括号与不使用括号的差别
#(.*?)的使用举例
#():括号内的数据作为结果返回
d = re.findall('xx(.*?)xx',secret_code)
print d
for each in d :
    print each
'''

#s = '''sdfxxhello
#xxfsdfxxworldxxasdf'''

#d = re.findall('xx(.*?)xx',s,re.S)
#print d

'''
#对比findall与search的区别
s2 = 'asdfxxIxx123xxlovexxdfd'
f = re.search('xx(.*?)xx123xx(.*?)xx',s2).group(1)
print f
f2 = re.findall('xx(.*?)xx123xx(.*?)xx',s2)
print f2[0][1]
'''
'''
#sub的使用举例
s = '123abcssfasdfas123'
output = re.sub('123(.*?)123','123789123',s)
#output = re.sub('123(.*?)123','123%d123'%789,s)
print output
'''

'''
#演示不同的导入方法
info = findall('xx(.*?)xx',secret_code,S)
for each in info :
    print each
'''

'''
#不要使用compile
pattern = 'xx(x*?)xx'
new_pattern = re.compile(pattern,re.S)
output = re.findall(new_pattern,secret_code)
print output
'''

#匹配数字
#使用\d+匹配纯数字
a = 'asdfasf1234567asd555fas'
b = re.findall('(\d+)',a)
print b
