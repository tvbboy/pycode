def getMax(a,b):
    if a>b:
        return a
    else:
        return b
num1=int(input("please input a number:"))
num2=int(input("please input a number:"))
#num3=int(input("please input a number:"))
print("最大值：",getMax(num1,num2))