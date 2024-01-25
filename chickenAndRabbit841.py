counter=0
findAnswer=False
for chicken in range(0,36):
    for rabbit in range(0,36):
        counter+=1
        if (chicken+rabbit==35)and(2*chicken+4*rabbit==94):
          print("鸡有{}只，兔子有{}只".format(chicken,rabbit))
          findAnswer=True;
          break 
    if findAnswer:
      break
print("execute times:",counter)