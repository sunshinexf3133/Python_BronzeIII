#coding:utf-8
#处理文本文件
###逐行读取文本文件
#####小知识
#python文件打开模式
#'r' 为读取而打开文件（默认模式）
#'w' 为写入而打开文件
#'a' 为在文件末尾附件而打开文件
#'b' 二进制模式
#'t' 文本模式（默认模式）
#'+' 为读写打开文件
#printfile.py

def print_file1(fname) :
    f = open(fname,'r')
    for line in f :
        print line,
    f.close() #这行代码是可选的
    return

if __name__ == "__main__" :
    print_file1('test_HandleFile.txt')
