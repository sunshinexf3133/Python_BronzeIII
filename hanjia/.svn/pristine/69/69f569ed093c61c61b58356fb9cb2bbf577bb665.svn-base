#coding:utf-8
###只想获悉当前工作目录中的.py文件
#####小懒懒课堂
##逻辑bug：
#在本次代码中遇到的问题是调用list_py()时如果直接给该函数传参数输出为[ ]
#代码示例：
#print list_py('F:\PythonWorkSpace\hanjia\huihui\day05')
#
##分析：
#os.path.isfile(name):name如果不是绝对路径，就是相对于当前路径的
#基于此，如果按照错误的思路来：
#首先传进去的绝对路径被path接受，现在path = 'F:\PythonWorkSpace\hanjia\huihui\day05'
#os.listdir(path)就是os.listdir('F:\PythonWorkSpace\hanjia\huihui\day05')
#开始执行return语句中的os.listdir(path)即os.listdir('F:\PythonWorkSpace\hanjia\huihui\day05')
#它返回F:\PythonWorkSpace\hanjia\huihui\day05下的所有文件和文件夹的名字类似于1.py等等
#for fname in os.listdir(path)假设开始第一次迭代
#此时os.listdir(path)返回的列表为['1.py',...]
#接下来应该执行return语句中的if条件筛选，即if os.path.isfile("1.py")，然而当前路径下并没有1.py
#返回False，进行下一次迭代，下一次如果没有了的话，就return []。解析完毕
#
##正解：
#如果想要直接传参数调用list_py(),即：
#print list_py('F:\PythonWorkSpace\hanjia\huihui\day05')
#只需对return中的语句进行修改：
#return [fname for fname in os.listdir(path)
#        if os.path.isfile(os.path.join(path,fname))
#        if fname.endswith('.py')]
#即给每个fname拼接上path就行了
#os.path.join()是拼接路径的
#####
#list.py

import os
def list_py(path = None) :
    """该函数巧妙地利用了其输入参数：如果你调用list_py()时
       未提供参数，它将把当前工作目录视为目标文件夹，否则将指
       定的目录视为目录文件夹"""
    if path == None :
        path = os.getcwd()
    return [fname for fname in os.listdir(path)
            if os.path.isfile(fname)
            if fname.endswith('.py')]

if __name__ == "__main__" :
    os.chdir('F:\PythonWorkSpace\hanjia\huihui\day05') 
    print list_py()
