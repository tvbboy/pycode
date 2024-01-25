#请编写homeworkPrintChar.py程序.要求输入行数1～26之间，然后程序输出字母，如图所示
n=int(input('请输入行数：'))
label='A'
for i in range(n):
    s=''
    for j in range(n-i-1):
        s+=' '
    for j in range(2*i+1):
        s+=label
    print(s)
    label=chr(ord(label)+1)