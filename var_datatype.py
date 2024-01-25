####################### 数据变量和常量#######################
## 实验目的：体验变量和常量
## 知识点：变量的内存实质
##        欢迎大家破坏性测试：）       
## email:ppu@cc.ecnu.edu.cn
## update:2022-10-8
###########################################################
##########################################
# 1.赋值
# 体验不同数据类型的赋值写法
##########################################
#num  #未赋值的变量，在引用的时候并会报错
#print(num)  
# num==1 # 这不是赋值语句是比较 
print("*"*10,"step 1","*"*10)
counter = 100        # An integer assignment
temp = -134          # An integer assignment
biggest = 1e10       # a float 10000000000.0
smallest = 1e-4      # a float 0.0001
rating = 12.88       # A floating point
name1 = "John"       # A string
name2 = 'John'       # A string 目前单引号和双引号两种写法都嗲表字符串赋值
name1 = "john"       # 发生了什么？
#体验布尔类型,真假李逵
ligui = "True"
likui = True
print("typeof ligui", type(ligui), "typeof likui", type(likui))
print("*"*28)
##########################################
# 2.赋值的内存实质---数据不可变
# 体会宏观世界的赋值和微观世界内存的变化
##########################################
print("*"*10,"step 2","*"*10)
a=1
b1=a
b2=a
print("b1:",b1,"b2:",b2,"\n")
a=2
print("b1:",b1,"b2:",b2,"\n")
print("*"*28)
##########################################
# 3.其他赋值小技巧
# 
##########################################
print("*"*10,"step 3","*"*10)
num="hello world!" #变量可以跨类型修改
#多变量赋值
ming,xing='zhang','fei'
print("xingming:",xing,ming)
#Python优雅 swap
ming,xing=xing,ming
print("after swap:")
print("xingming:",xing,ming)
print("*"*28)

##########################################
# 3.小整数对象池-5到256
# 
##########################################
print("255 address:",id(255))
print("256 address:",id(256))
print("257 address:",id(257))
a=255
b=255
print(a,"addrss:",id(a))
print(b,"addrss:",id(b))
a=258
b=258
print(a,"addrss:",id(a))
print(b,"addrss:",id(b))