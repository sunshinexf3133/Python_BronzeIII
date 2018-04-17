#计算用户输入的数字的总和
#forsum.py

n = int (raw_input('How  many  numbers to sum?'))
total = 0
for i in range(n):
    s = input('Enter number' + str(i) + ':')
    total = total + int(s)
print('The sum is ' + str(total))
