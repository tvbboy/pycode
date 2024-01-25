# Sedgewick增量序列
# D=9*4^i-9*2^i+1 或 4^(i+2)-3*2^(i+2)+1 , i>=0
# 稍微变一下形：D=9*(2^(2i)-2^i)+1 或 2^(2i+4)-3*2^(i+2)+1 , i>=0
# n代表排序的数组的元素数量
def getSedgewickStepArr(n):
    i = 0
    arr = []
    while True:
        #tmp = 9 * ((1 << 2 * i) - (1 << i)) + 1
        tmp1 = 9 * (4**i) - 9*(2**i) + 1
        print("i=",i,":",tmp1,end='')
        if tmp1 <= n:
            arr.append(tmp1)
        
        tmp2 = (1 << 2 * i + 4) - 3 * (1 << i + 2) + 1
        print("---",tmp2)
        if tmp2 <= n:
            arr.append(tmp2)
        else:
            break
        print()
        i += 1
    return arr
n=int(input("input the shell sort array num:"))
print(getSedgewickStepArr(n))