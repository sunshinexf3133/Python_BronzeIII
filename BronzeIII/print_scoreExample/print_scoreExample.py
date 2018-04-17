#coding:utf-8

__author__ = 'Sunshine'

def print_score(std):
    print('%s:%s' % (std['name'],std['score']))

def main():
    std1 = {'name':'Michael','score':98}
    std2 = {'name':'Bob','score':81}
    print_score(std1)
    print_score(std2)


if __name__ == '__main__':
    main()
