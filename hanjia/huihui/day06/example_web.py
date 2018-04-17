# coding:utf-8

import urllib2 as u





page = u.urlopen("http://115.159.202.75:8080/")
html = page.read()
print html
