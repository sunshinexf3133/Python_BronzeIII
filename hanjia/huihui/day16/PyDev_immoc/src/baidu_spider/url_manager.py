#coding:utf-8
#URL管理器：需要对外提供四个方法
'''
Created on 2017年3月3日

@author: xufei
'''
class UrlManager(object):
    #URL管理器需要维护两个列表，即待爬取的URL列表和爬取过的URL列表
    #在构造函数中进行初始化
    
    #构造函数
    def __init__(self):
        self.new_urls = set() 
        self.old_urls = set() 
    #向管理器中添加一个新的URL，添加单个URL
    def add_new_url(self,url):
        #进行参数判断
        if url is None:
            return
        #该URL既不在待爬取的URL列表里面，也不在爬取过的URL列表里面
        #说明它是一个全新的URL，它可以用来待爬取
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)
        
    #向管理器中添加批量的URL
    def add_new_urls(self,urls):
        #参数判断urls是None或urls列表为空，则不进行添加
        if urls is None or len(urls) == 0:
            return
        #否则循环调用add_new_url进行单个添加
        for url in urls:
            self.add_new_url(url)   
   
    #判断管理器中是否有新的待爬取的URL
    def has_new_url(self):
        #new_urls列表长度不为零，即说明有待爬取的URL
        return len(self.new_urls) != 0
    
    #从URL管理器中获取一个新的待爬取的URL
    def get_new_url(self):
        #获取一个URL，pop方法会在待爬取的URL列表中获取一个URL，并将该URL移除
        new_url = self.new_urls.pop()
        #此时需要将该URL添加进self.odd_urls
        self.old_urls.add(new_url)
        #并将获取得的URL返回
        return new_url
    
