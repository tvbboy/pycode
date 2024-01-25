def changeX(fx):
  print("befor modify fx:",fx,"id:",id(fx))
  fx=10
  print("fx:",fx,"id:",id(fx))
x=5
changeX(x)
print("x:",x,"id:",id(x))