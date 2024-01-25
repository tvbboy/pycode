set_1 = {1,2,"hello","world"}
print(set_1)
set_2 = {True , False, (1,2,3,4) }
print(set_2)
list1=[1,2,2,3]
set_3=set(list1)
print(set_3)
set_4=set()
print(type(set_4))
set_5={}
print(type(set_5))


set_1 = {1, 2, 3, 4, 5}
set_1.add(6)  # adding an item in a set
set_1.update({7, 8, 9})  # addind multiple items
set_1.update({2, 2, 2, 2, 3, 3,10})  # adding duplicate items
print(set_1)


set_1= {1,2,3,4,5}
set_1.remove(2)
set_1.discard(4)
print(set_1)
#set_1.remove(6)
print(set_1)


set_1 = {1, 2, 3, 4, 5, 6}
set_1.pop()
print(set_1)
set_1.clear()  # Clear all items of set
print(set_1)


a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
c = a | b  # union
d = a.union(b)
print(c)
print(d)


a = {1,2,3,4}
b = {3,4,5,6}
c = a & b
d = a.intersection(b)
print(c)
print(d)


a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
c = a - b
d = b - a
print("a-b is:", c)
print("b-a is:", d)


a = {1,2,3,4}
b = {3,4,5,6}
c = a ^ b
d = b ^ a
print("a ^ b is:", c)
print("b ^ a is:",d)