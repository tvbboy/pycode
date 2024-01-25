######新建“学号+hw_sqrt.py”，以提示语“please input the numer:”接收用户输入正整数。
##通过逐次逼近法，输出该数的平方根。（不能使用没有学过的内容）
number = int(input("please input the number:"))
#print(number//2+1)
k=1
#for i in range(0,number//2+1):
#print("逼近值:", abs(round(number-k*k,2)))
while(abs(round(number-k*k, 2)) > 0.1):
        k=round(k+0.01,2)
        #print("逼近值:", round(number-k*k, 2))
print("the root of sqrt:",k)
        # #print(k)
        # #print("逼近值:",round(number-k*k,2))
        # if 0<=(round(number-k*k,2)) <= 1e-2:
        #     print("the root of sqrt:",k)
# print(number//2+1)
# k=number//2
# #for i in range(0,number//2+1):
# print("逼近值:", abs(round(number-k*k,2)))
# while(abs(round(number-k*k, 2)) > 0.1):
#         k=round(k-0.01,2)
#         print("逼近值:", round(number-k*k, 2))
# print("the root of sqrt:",k)
#         # #print(k)
#         # #print("逼近值:",round(number-k*k,2))
#         # if 0<=(round(number-k*k,2)) <= 1e-2:
#         #     print("the root of sqrt:",k)
