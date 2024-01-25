# inpu a list  with some duplicate and unique elements
li=[]
while True:
    temp=input("please input an element(break for exit):")
    if(temp=="break"):
        break
    li.append(temp)
print("the list is",li)
li_unique=[]
remove_count=0
for item in li:
    if item not in li_unique:
        li_unique.append(item)
    else:
        remove_count+=1
print("after remove duplicat:",li_unique)
print("remove",remove_count," elements")

