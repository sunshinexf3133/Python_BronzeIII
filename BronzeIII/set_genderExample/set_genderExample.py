#coding:utf-8

class Student(object):

    def __init__(self,name,gender):
        self.__name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def get_name(self):
        return self.__name

    def set_gender(self,gender):
        self.__gender = gender


def main():
    bart = Student('Bart','male')
    if bart.get_gender() != 'male':
        print('测试失败！')
    else:
        bart.set_gender('female')
        if bart.get_gender() != 'female':
            print('测试失败！')
        else:
            print('测试成功！')

if __name__ == '__main__':
    main()
