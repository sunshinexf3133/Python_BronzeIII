#coding:utf-8

def readImage(fp):
    if hasattr(fp,'read'):
        return readData(fp)
    return None
