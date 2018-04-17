#coding:utf-8
#?下面示例打印了拥有两个字符串的“hello world”信息，用连字符(-)分隔，
#?以‘END’作为结束标记，并把它输出到文件中：

if __name__ == '__main__':
    with open("tmp.txt","w") as tmp:
        print("Hello", "World", end = "END", sep = "-", file = tmp)
