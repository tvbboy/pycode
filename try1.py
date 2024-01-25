import math
try:
    num1=float(input("请输入除数："))
    num2=float(input("请输入被除数:"))
    shang=num1/num2
    print("商是:",shang)
    #print("math.exp(1000)",math.exp(1000))
except ZeroDivisionError:
        print("除数不能为0")
except OverflowError:  
        print ("发生溢出！")
except:
    print("出现了异常！")
else:
    print("没有异常发生！")
finally:
    print("finally部分")
