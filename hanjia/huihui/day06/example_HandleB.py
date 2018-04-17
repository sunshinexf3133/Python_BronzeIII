#coding:utf-8
#处理二进制文件
#如果文件不是文本文件，它就被视为二进制文件
###该函数检查fname是不是GIF图像文件，方法是
###检查其前四个字节是不是（0x47,0x49，0x46,0x38）
###（所有GIF图像文件都是以这4个字节打头）
#?这个返回结果是不是True或False
#handleb.py

def is_gif(fname) :
    f = open(fname,'rb')
    first4 = tuple(f.read(4))
    return first4 == (0x47,0x49,0x46,0x38)

if __name__ == "__main__" :
    print is_gif('todo06.md')
