#����δ֪�����ֵ��ܺ�
#donesum.py

###����Ҫ���û��������֣�ֱ���û����롮done������ѭ��

total = 0
s = raw_input('Enter a number(or done):')
while s != 'done' :
    num = int(s)
    total = total + num
    s = raw_input('Enter a number(or done):')
print('The sum is:' + str(total))

