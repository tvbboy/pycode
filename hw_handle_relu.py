# 程序改错-线性整流函数ReLU
# 提供程序代码有错误，按下列要求进行改错，不得增删行，使其能正确执行。
# 程序功能：深度学习算法中常用线性整流函数ReLU，其定义为 f(x) = max(0,x)。程序从键盘接收若干个以半角空格分隔的整数，对其逐个应用ReLU函数进行转换，转换结果存放于列表并输出。
# 程序代码中有3处错误（语法错误或逻辑错误），请改正，使程序能正常运行并输出要求的结果。
# 程序运行示例：
# 请输入若干个以半角空格分隔的整数：
# 3 0 -5 5 -9 8
# 应用ReLU函数处理后的数据为： [3, 0, 0, 5, 0, 8]
def relu(x):
    if x>0:
        return x
    else:
        return 0
mystr=input("请输入若干个以半角空格分隔的整数：")
mylist=mystr.split(" ")
resultList=[]
for number in mylist:
    number=int(number)
    resultList.append(relu(number))
print("应用ReLU函数处理后的数据为：",resultList)



