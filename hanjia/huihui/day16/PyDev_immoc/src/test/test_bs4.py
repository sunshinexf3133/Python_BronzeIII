#coding:utf-8
#使用beautifulsoup来解析网页文档字符串，然后进行各种搜索和节点访问的各种方法
'''
Created on 2017年3月2日

@author: xufei
'''
import re
from bs4 import BeautifulSoup
#用html_doc作为我们本次测试代码的测试素材
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

#创建bs对象，第一个参数指定为文档字符串，第二个参数指定html.parser作为它的解析器，第三个参数指定编码
soup = BeautifulSoup(html_doc,'html.parser',from_encoding = 'utf-8')

print '获取所有的链接'
#传入链接的字符串为a
links = soup.find_all('a')
#打印节点的名称，节点的href属性，节点的文字
for link in links :
    print link.name,link['href'],link.get_text()
    
print '获取lacie的链接'
#此时只想获取一个链接，故将find_all改为find
link_node = soup.find('a',href = 'http://example.com/lacie')
print link_node.name,link_node['href'],link_node.get_text()

#输入一个正则表达式来匹配出我们模糊匹配需要的内容
print '正则匹配'
#加上r的作用：如果正则表达式中出现了反斜杠只需要写一个就OK了，否则得写两个
link_node = soup.find('a',href = re.compile(r"ill"))
print link_node.name,link_node['href'],link_node.get_text()

#该例子是为了查看能否获取到p这个段落文字，指定他的class来获取他的内容
print '获取p段落文字'
#标签名称为p,class是python的一个关键字，于是我们加一个下划线，此处为p_node
p_node = soup.find('p',class_ = "title")
#输出p_node的名称，以及它的文字，他没有href了，于是删掉href部分，
print p_node.name,p_node.get_text()