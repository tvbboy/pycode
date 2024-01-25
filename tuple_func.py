tuple1 = (10, 20, 60, 30, 60, 40, 60)
# Count all occurrences of item 60
count = tuple1.count(60)
print(count)
# Output 3

count = tuple1.count(600)
print(count)
# Output 0


tuple1 = (0, 1, 2, 3, 4, 5)

# converting tuple into a list
sample_list = list(tuple1)
# reomve 2nd item
sample_list.remove(2)

# converting list back into a tuple
tuple1 = tuple(sample_list)
print(tuple1)
# Output (0, 1, 3, 4, 5)


tuple1 = (10, 20, 60, 30, 60, 40, 60)
# Count all occurrences of item 60
count = tuple1.count(60)
print(count)
# Output 3

count = tuple1.count(600)
print(count)
# Output 0




sampletup1 =(0,1,2,3,4,5,6,7,8,9,10)
sampletup1=tuple()
#print(sampletup1)
print("check empty tuple:",sampletup1==())
del sampletup1
tuple1 = (0, 1, 2, 3, 4, 5)
# copy tuple
tuple2 = tuple1
print(tuple2)
# Output (0, 1, 2, 3, 4, 5)
# changing tuple2
# converting it into a list
sample_list = list(tuple2)
sample_list.append(6)
# converting list back into a tuple2
tuple2 = tuple(sample_list)
# printing the two tuples
print(tuple1)
# Output (0, 1, 2, 3, 4, 5)
print(tuple2)
# Output (0, 1, 2, 3, 4, 5, 6)


tuple1 = (1, 2, 3, 4, 5)
tuple2 = (3, 4, 5, 6, 7)
# concatenate tuples using + operator
tuple3 = tuple1 + tuple2
print(tuple3)
# Output (1, 2, 3, 4, 5, 3, 4, 5, 6, 7)
# using sum function
tuple3 = sum((tuple1, tuple2), ())
print(tuple3)
# Output (1, 2, 3, 4, 5, 3, 4, 5, 6, 7)
tuple1 = ('xyz', 'zara', 'abc')
# The Maximum value in a string tuple
print(max(tuple1))  
# Output zara
# The minimum value in a string tuple
print(min(tuple1))
# Output abc

tuple2 = (11, 22, 10, 4)
# The Maximum value in a integer tuple
print(max(tuple2))
# Output 22
# The minimum value in a integer tuple
print(min(tuple2))
# Output 4
print(sum(tuple2))
# Output 47
tuple1 = (1, 2, 3, 4, 5)
tuple2 = ('a', 'b', 'c', 'd')
zip_tuple = zip(tuple1, tuple2)
print(zip_tuple)
print(*zip_tuple)
print(type(zip_tuple))
