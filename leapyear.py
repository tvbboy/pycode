year = 2000;
condition1 = year % 400 == 0;
print("condition1: ", condition1)
condition2 = year % 4 == 0 and year % 100 != 0;
print("condition2:", condition2)
print(year,"is leap year?", condition1 or condition2)
