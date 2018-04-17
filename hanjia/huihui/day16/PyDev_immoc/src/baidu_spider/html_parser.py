#coding:utf-8
#HTML的解析器
'''
Created on 2017年3月3日

@author: xufei
'''
from bs4 import BeautifulSoup
import re
import urlparse

class HtmlParser(object):
    
    
    def _get_new_urls(self,page_url,soup):
        new_urls = set()
        #获取所有的a标签
        # /view/123.htm
        links = soup.find_all('a',href=re.compile(r"/view/\d+\.htm"))
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url,new_url)
            new_urls.add(new_full_url)
        return new_urls
    
    #解析数据
    def _get_new_data(self,page_url,soup):
        res_data = {}
        
        #url
        res_data['url'] = page_url
        
        #<dd class="lemmaWgt-lemmaTitle-title"> <h1>Python</h1>
        title_node = soup.find('dd',class_ = "lemmaWgt-lemmaTitle-title").find("h1")
        res_data['title'] = title_node.get_text()
        
        #<div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('div',class_ = "lemma-summary")
        res_data['summary'] = summary_node.get_text()
        
        return res_data


    #该方法要求我们从cont中解析出两个数据，新的URL列表和数据
    def parse(self,page_url,html_cont):
        #参数判断
        if page_url is None or html_cont is None:
            return 
        #将content加载进soup
        soup = BeautifulSoup(html_cont,'html.parser',from_encoding = 'utf-8')
        #两个本地方法
        new_urls = self._get_new_urls(page_url,soup)
        new_data = self._get_new_data(page_url,soup)
        return new_urls,new_data
    
    