#coding:utf-8
#使用元类_type()

def fn(self,name = 'world') :
    print ('Hello,%s.' %name)

if __name__ == "__main__" :
    Hello = type('Hello',(object,),dict(hello = fn))
    h = Hello()
    h.hello()
    print (type(Hello))
    print(type(h))
