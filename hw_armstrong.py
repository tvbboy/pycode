num = input("请输入一个三位数整数:")
if len(num) != 3:
    print("数据格式错误！")
else:
    num = int(num)
    if num == pow(num // 100, 3) + pow(num % 10, 3) + pow(num // 10 % 10, 3):
        print(f"{num}是水仙花数")
    else:
        print(f"{num}不是水仙花数")
