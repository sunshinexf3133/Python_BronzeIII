#coding:utf-8
#下载器，本代码用来下载HTML
'''
Created on 2017年3月3日

@author: xufei
'''
import urllib2

class HtmlDownloader(object):
    #参数url，即要下载的URL
    def download(self,url):
        #参数判断
        if url is None:
            return  None
        
        #请求URL的内容
        response = urllib2.urlopen(url)
        
        #如果请求失败，返回None
        if response.getcode() != 200:
            return None
        
        #否则返回下载好的内容
        return response.read()
            
        