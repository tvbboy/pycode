def doubler(x):
    return x*2
print(doubler(2))
print(doubler(5))


doubler = lambda x: x*2
print(doubler(2))
print(doubler(5))

# A lambda function that multiplies two values
mul = lambda x, y: x*y
print(mul(2, 5))

# Python code to illustrate 
# filter() with lambda() 
list1 = [5, 7, 97, 77, 23, 73, 61] 
filter_list = list(filter(lambda x: (x>50) , list1)) 
print(filter_list) 

cube = [1, 2, 3, 4, 5, 6, 7]
cubed_list = list(map(lambda x: x*x*x, cube))
print(cubed_list)


# Python code to illustrate 
# reduce() with lambda() 
from functools import reduce
list2 = [1, 2, 3, 4, 5, 6, 7] 
multiply = reduce((lambda x, y: x * y), list2) 
print (multiply) 

n=int(input("please input a number:"))
list3 = [i for i in range(0,n+1)]
#print(list3)
fib = reduce((lambda x, y: x + y), list3) 
print (fib) 
