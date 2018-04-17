#coding:utf-8
'''
Created on 2017年2月18日

@author: xufei
'''
import urllib2,cookielib

url = "http://www.baidu.com"

print '第一种方法'
response1 = urllib2.urlopen(url)
print response1.getcode()
print len(response1.read())

print '第二种方法'
request = urllib2.Request(url)
#添加头部，将爬虫伪装成Mozilla浏览器
request.add_header("user-agent","Mozilla/5.0")
response2 = urllib2.urlopen(request)
print response2.getcode()
print len(response2.read())

print '第三种方法'
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
response3 = urllib2.urlopen(url)
print response3.getcode()
#打印cookie内容
print cj
#打印爬虫获得的内容
#print response3.read()