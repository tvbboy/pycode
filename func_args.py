def add(*args, **kwargs):
  result = 0
  for arg in args:
    result += arg
  print(result)
  for key, value in kwargs.items():
    print(key, value)
add(2, 4, 6, a=8, b=10)
#add(2,4,6,a=8,7,b=10)
