#coding:utf-8
#写入文本文件
###make_story()函数创建一个名为story.txt的文本文件，
###如果该文本文件已经存在则提示已经存在，否则继续创建
###add_to_story()是将文本文件附加到文件末
###insert_title()是将字符串插入到文件开头
#write.py

import os
def make_story1() :
    if os.path.isfile('story.txt') :
        print('story.txt already exists')
    else :
        f = open('story.txt','w')
        f.write('huihuijiejie loves xiaolanlan ,\n')
        f.write('and lanyangyanggege loves xiaohuihui.\n')
 
    return

def add_to_story(line,fname = 'story.txt') :
    f = open(fname,'a')
    f.write(line)
    return

def insert_title(title,fname = 'story.txt') :
    f = open(fname,'r+')
    temp = f.read()
    temp = title + '\n\n' + temp
    f.seek(0) #让文件指针指向文件开头
    f.write(temp)
    return

    
if __name__ == "__main__" :
    make_story1()
    add_to_story('xiaolanlan  and  xiaohuihui',fname = 'story.txt')
    insert_title('qingqingcaoyuan',fname = 'story.txt')
