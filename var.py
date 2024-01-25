# 本实验目的：
## 知识点：变量的四要素
##        欢迎大家破坏性测试：）

# 1.掌握变量四要素
# 2.掌握赋值的内存变化
# 参考https://blog.csdn.net/weixin_44088790/article/details/117982467
## email:ppu@cc.ecnu.edu.cn
## update:2022-10-8
##########################################
# 1.变量四要素
# 体验变量的赋值四要素
##########################################
print("###############start############"); 
print("1's memory location",id(1))
num=1  #赋值语句，注意=和数学中=的差异
print("My favorite number is %s because it is first.\n",num)
print("num's memory location",id(num),"num's type",type(num),"\n")
##########################################
# 2.变量四要素
# # 体验变量的赋值四要素
##########################################
# 
x=354
print(type(x)) #输出<class 'int'>
print(id(x))   #输出34539888,这个值会随时间以及不同计算机发生变化
y="word"
print(type(y))   #输出<class 'str'>
print(id(xy))    #33407296
##########################################
# 3.掌握赋值的内存变化
# Memory diagram of variables in Python
##########################################
#
a = 2
print('id(a) =', id(a))
a = a+1
print('id(a) =', id(a))
print('id(3) =', id(3))
b = 2
print('id(b) =', id(b))
print('id(2) =', id(2))