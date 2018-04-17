#coding:utf-8
#sorted_排序算法

#排序忽略大小写，按照字母序排序
def cmp_ignore_case(s1,s2) :
    u1 = s1.upper()
    u2 = s2.upper()
    if u1 < u2 :
        return -1
    elif u1 > u2 :
        return 1
    else :
        return 0

if __name__ == "__main__" :
    #默认情况下对字符串排序
    print sorted(['bob','about','Zoo','Credit'])
    print '-------------------------------------'

    #排序忽略大小写，按照字母序排序
    print sorted(['bob','about','Zoo','Credit'],cmp_ignore_case)
