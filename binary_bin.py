# 这是用来熟悉二进制以及基本运算的一个程序
# 目的：
# 掌握bin函数关于负数的处理方法
# 日期时间：2023-9-28 
# 作者:蒲鹏
# 参考:https://pythonspot.com/binary-numbers-and-logical-operators/
##########################################
# 对一个数按位取反
##########################################
# Output: 107
print("2#:0", bin(0))
# Output: 253 (251 + 2)
print("2#:1", bin(1))
print("对1按位取反",~1)
print("2#对1按位取反",bin(~1))
print("2#对1按位取反",bin(~1 & 0xffffffff))
print("*"*28)
