# 这是用来熟悉二进制以及基本运算的一个程序
# 目的：
# 掌握Number数据类型的不同进制使用方法
# 掌握进制的转换
# 掌握二进制 + - × / ^ %
# 2.掌握二进制的移位操作
# 掌握几个进制之间的转换函数  bin() hex()分别输出二进制和16进制
# 日期时间：2023-9-28 
# 作者:蒲鹏
# 参考:https://pythonspot.com/binary-numbers-and-logical-operators/
##########################################
# 1.掌握Number数据类型的不同进制使用方法
##########################################
# Output: 107
print("2#:", 0b1101011)
# Output: 253 (251 + 2)
print("16#:", 0xFB + 0b10)
# Output: 13
print("8#:", 0o15)
##########################################
# 2.进制转换
#
##########################################
print("*"*10, "step 2", "*"*10)
Numbase10 = 1024  # python默认的数都是10#
Numbase2 = bin(Numbase10)
print(Numbase10, "转换为2#之后是", Numbase2)
Numbase16 = hex(Numbase10)
print(Numbase10, "转换为16#之后是", Numbase2)
print("*"*28)
##########################################
# 3 .1位二进制操作 bitwise operator
#
##########################################
print("*"*10, "step 2", "*"*10)
num1=0b1
num2=0b0
result=num1^num2 #异或
print("^result:",result)

num1=0b1
num2=0b0
result=num1>>1  #右移1位
print(">>result:",result)

num1=0b1
num2=0b0
result=num1<<2 #左移2位
print("<<result:",result)


num=8
num_right=num>>2
num_left=num<<3
print(num,"右移动2位结果是",num_right)
print(num,"作移动3位结果是",num_left)
##########################################
print("通过二进制的视角观察数的变化")
print(bin(num),"右移动2位结果是",bin(num_right))
print(bin(num),"作移动3位结果是",bin(num_left))

print("*"*28)
