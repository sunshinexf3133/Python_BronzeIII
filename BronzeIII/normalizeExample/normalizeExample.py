#coding:utf-8



def normalize(name):
    return name[0].upper() + (name[1:]).lower()

def main():
    L1 = ['adam','LISA','barT']
    L2 = list(map(normalize,L1))
    print(L2)

if __name__ == '__main__':
    main()
    
