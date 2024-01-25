# >>> import random
# >>> random.randint(0,99)
# 21
# 第一行的意思是使用前必须导入随机数包
# 第二行是产生0到99之间（包含0和99）的随机数的函数。
# 请大家编写程序homeworkRandom.py，当程序运行的时候，自动产生0到99之间的10个不同的随机数。
# 首先输出原数列，再输出排序后的数列，结果如图所示
import random
L = []
while len(L) < 10:
    num = random.randint(0, 99)
    if num not in L:
        L.append(num)
print(L)
L.sort()
print('排序后')
print(L)
