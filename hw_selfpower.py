import math
num = input("pease input the number:")
pow_number=len(num)
sum=0
for char in num:
    sum += math.pow(int(char), pow_number)
if sum == int(num):
    print(f"{num} is self power")
else:
    print(f"{num} is not self power")