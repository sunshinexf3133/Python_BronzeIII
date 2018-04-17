#coding:utf-8
###下面的函数返回当前工作目录中所有文件的大小总和
#list.py

import os

def list_cwd() :
    """获悉当前工作目录中的文件和文件夹"""
    return os.listdir(os.getcwd())

def files_cwd() :
    """使用列表解析返回当前工作目录中的文件"""
    return [p for p in list_cwd() if os.path.isfile(p)]


def size_in_bytes(fname) :
    """返回文件的大小，以位为单位"""
    return os.stat(fname).st_size

def cwd_size_in_bytes() :
    """返回当前工作目录中所有文件的大小总和"""
    total = 0
    for name in files_cwd() :
        total = total + size_in_bytes(name)
    return total

if __name__ == "__main__" :
    a = cwd_size_in_bytes()
    print a
