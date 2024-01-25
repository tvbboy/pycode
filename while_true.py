mykey=88
while True:
    guess=int(input("请输入一个100以内的正整数："))
    if(guess>mykey):
        print("太大了")
    elif(guess<mykey):
        print("太小了")
    else:
        print("恭喜你，猜对了")
        break;