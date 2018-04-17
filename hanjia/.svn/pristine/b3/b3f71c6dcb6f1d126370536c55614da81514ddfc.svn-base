#coding:utf-8
#使用列表解析进行筛选
###下面函数使用列表解析删除字符串中的所有元音
#[c for c in s if c.lower() not in 'aeiou']，这是一个筛选型列表解析，
#它以每次一个字符的方式扫描s，将每个字符转换为小写，再检查它是不是元音。
#如果是元音，则不将其加入最终的列表，否则将其加入最终列表
#
#该列表解析的结果是一个字符串列表，因此我们使用join将所有字符串拼接成一个，
#再返回这个字符串。
#eatvowels.py

def eat_vowels(s) :
    """Removes the vowels from s."""
    return ''.join([c for c in s if c.lower() not in 'aeiou'])

if __name__ == "__main__" :
    s = raw_input("Please input a string :")
    print('After eat_vowels:{}'.format(eat_vowels(s)))
