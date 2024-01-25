#循环提示用户输入整数，当输入OK的时候，程序把输入的所有数的最大值，最小值和平均值输出。
l=[]
while True:
    a=input("请输入一个数字（输入OK停止）：\n")   
    if a=="OK":       
        break   
    else:       
         l.append(int(a))
l.sort()
print("最大值为",l[-1],"最小值为",l[0],"平均值为",str((sum(l)/len(l))))