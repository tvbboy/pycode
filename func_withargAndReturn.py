def printStar(arg1):
    for i in range(arg1):
        print("*"*arg1)
def getList(arg1,arg2=""):
    if arg2=="odd":
        return list(range(1,arg1,2))
    elif arg2=="even":
        return list(range(0,arg1,2))
    else:
        return list(range(0,arg1))
list1=getList(10,"odd")
print(list1)
list2=getList(10,"")
print(list2)
list3=getList(arg2="odd",arg1=10)
print(list3)
printStar(5)
