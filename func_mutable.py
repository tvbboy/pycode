def changeX(arg):
  if(type(arg) == type([])):
    arg[0]="--"
  print("arg:",arg,"id:",id(arg))
list1=[10,5,0]
print("before list1:",list1,"id:",id(list1))
changeX(list1)
print("after list1:",list1,"id:",id(list1))
tuple1=(10,5,0)
print("tuple1:", tuple1, "id:", id(tuple1))
changeX(tuple1)

