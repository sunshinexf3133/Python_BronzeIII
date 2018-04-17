#coding:utf-8
#本代码将所有收集好的数据写出到一个HTML页面中，打开这个页面就能看到
#所有已经爬取好的数据
'''
Created on 2017年3月3日

@author: xufei
'''
class HtmlOutputer(object):
    
    def __init__(self):
        self.datas = []
    
    def collect_data(self,data):
        if data is None:
            return 
        self.datas.append(data)
    
    def output_html(self):
        fout = open('output.html','w')
        
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")
        
        #ascii
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" %data['url'])
            fout.write("<td>%s</td>" %data['title'].encode('utf-8'))
            fout.write("<td>%s</td>" %data['summary'].encode('utf-8'))
            fout.write("</tr>")
        
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        
        fout.close()
        
        
        
        