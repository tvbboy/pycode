tuple1 = (10, 20, 25.75)
tuple2 = ('Jessa', 'Emma', 'Kelly')
tuple3 = ('Jessa', 30, 45.75, [25, 78])
tuple4 = tuple([23, 78])
tuple5=()
print(type(tuple5))
print(tuple1[0])
print(tuple1[-1])
#print(tuple1[3])

string="1234567890"
tuple5=tuple(string)
print(tuple5[:3])
print(tuple5[4:])
print(tuple5[0:9:2])
print(tuple5[::-1])


# packing variables into tuple
tuple1 = 1, 2, "Hello"
print(tuple1)  
# Output (1, 2, 'Hello')
# unpacking tuple into variable
i, j, k = tuple1
# printing the variables
print(i, j, k)   #1 2 Hello


tuple1 = (0, 1, 2, 3, 4, 5)
#tuple1[1] = 10
# Output TypeError: 'tuple' object does not support item assignment
tuple1 = (10, 20, [25, 75, 85])
# before update
print(tuple1)
# Output (10, 20, [25, 75, 85])
# modify last item's first value
tuple1[2][0] = 250
# after update
print(tuple1)
# Output (10, 20, [250, 75, 85])

tuple1 = (0, 1, 2, 3, 4, 5)

# converting tuple into a list
sample_list = list(tuple1)
# modify 2nd item
sample_list[1] = 10

# converting list back into a tuple
tuple1 = tuple(sample_list)
print(tuple1)  
# Output (0, 10, 2, 3, 4, 5)


# create a tuple
sample_tuple = tuple((1, 2, 3, "Hello", [4, 8, 16]))
# iterate a tuple
for item in sample_tuple:
    print(item)