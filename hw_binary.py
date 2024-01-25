# 请输出给定的一个二进制数字，按位取反后的形式（不考虑符号位）
# 目的：掌握二进制 + - × / ^ % 
# 日期时间：2023-9-28 
# 作者:蒲鹏
# 参考:https://pythonspot.com/binary-numbers-and-logical-operators/
num1=0b10010011
num2=0b11111111
result=num1^num2 #异或
print(bin(num1),"Inverse code:",bin(result))