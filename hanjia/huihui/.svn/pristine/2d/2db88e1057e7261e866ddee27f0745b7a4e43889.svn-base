#coding:utf-8
#检查文件和文件夹
#？其实这个代码想让我干嘛我也搞不太清楚，感觉无从下爪
#！主要问题在于文件和文件夹函数的作用没搞清楚，加上自己耐心不足使得工作无法正常进行
#！学习任何一门知识都少不了自己的细心探索，烦躁暴躁并不能解决问题，反而会使问题变得
#！复杂化。
###下列函数使用列表解析分别返回当前工作目录中的文件和文件夹
#####实用的文件和文件夹函数
#import os
#导入os函数
#os.getcwd()
#返回当前工作目录的名称
#os.listdir(p)
#返回一个字符串列表，其中包含路径p指定的文件夹中所有的文件和文件夹的名称
#os.chdir(p)
#将当前工作目录设置为路径p
#os.path.isfile(p)
#判断p是否为文件，如果是返回True，否则返回False。当文件不存在时也返回False
#os.path.isdir(p)
#判断p是否为文件夹，如果是返回True，否则返回False。当文件夹不存在时也返回False
#os.stat(fname)
#返回有关fname的信息，如大小（单位为字节）和最后一次修改时间
#####
#list.py

import os
def list_cwd() :
    """获悉当前工作目录中的文件和文件夹"""
    return os.listdir(os.getcwd())

def files_cwd() :
    return [p for p in list_cwd() if os.path.isfile(p)]

def folders_cwd() :
    return [p for p in list_cwd() if os.path.isdir(p)]

if __name__ == "__main__" :
    os.chdir("f:\PythonWorkSpace")
    a = list_cwd()
    b = files_cwd()
    c = folders_cwd()

    print a
    print b
    print c
    
