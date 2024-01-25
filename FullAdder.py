#实现2位全加器
#作者：葛佳誉
#时间：10/7
#test1
a=0b10
b=0b11
a0=a&1
a1=(a>>1)&1
b0=b&1
b1=(b>>1)&1
print(a0,a1,b0,b1)
#第0位
sum0 = a0^b0
carry0 =a0&b0
#第1位 全加
sum1_0 = a1^b1
carry1_0 =a1&b1
sum1_1 =sum1_0^carry0
carry1_1 =sum1_0&carry0



carry1_2 = carry1_0|carry1_1
result=(carry1_2<<2)+(sum1_1<<1)+sum0
#result=carry1_2<<2+sum1_1<<1+sum0
print("carry1_2<<2",carry1_2<<2)
print("sum1_1<<1",sum1_1<<1)
print ("carry1_2=",carry1_2,"sum1_1=",sum1_1,"sum0=",sum0,"result=",bin(result))
