#coding:utf-8
#下面示例要求用户输入一个数字，如果数字太高或者太低，它会打印一个警告

if __name__ == '__main__':

    target = 66

    while True:
        value = raw_input("Enter an integer between 1 and 100")
        try:
            value = int(value)
            break
        except ValueError:
            print("Please enter an integer!")

    if int(value) > target:
        print(value,"is too high")
    elif int(value) < target:
        print(value,"is too low")
    else:
        print("Perfect")
        
