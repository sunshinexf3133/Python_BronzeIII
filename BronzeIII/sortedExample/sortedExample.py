#coding:utf-8

def by_name(t):
    return t[0].lower()

def by_score(t):
    return t[1]

def main():
    L = [('Bob',75),('Adam',92),('Bart',66),('Lisa',88)]
    L1 = sorted(L,key = by_name)
    print(L1)

    L2 = sorted(L,key = by_score)
    print(L2)

if __name__ == '__main__':
    main()
    
