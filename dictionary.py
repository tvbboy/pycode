# empty dictionary
my_dict = {}
# dictionary with integer keys
my_dict = {1: 'apple', 2: 'ball',3: 'ball'}
# dictionary with mixed keys
my_dict = {'name': 'John', 1: [2, 4, 3]}
# using dict()
# from sequence having each item as a pair
my_dict = dict([(1,'apple'), (2,'ball')])
users = {"İsmail Baydan": {"username": "ismail", "password": "123"},
         "Ahmet Baydan": {"username": "ahmet", "password": "456"}}

dic_key = ['m','u','t','z','x']
dic_val = [19,67,28,17,15]  
new_dic = { a:b for (a,b) in zip(dic_key, dic_val)} 
print (new_dic)

thisdict = {
 "brand": "Ford",
 "model": "Mustang",
 "year": 1964
}
thisdict["year"] = 2019

thisdict = {
 "brand": "Ford",
 "model": "Mustang",
 "year": 1964
}
thisdict["color"] = "red"
print(thisdict)


thisdict = {
 "brand": "Ford",
 "model": "Mustang",
 "year": 1964
}
datedict = {
  "date": 13,
  "month": "January",
  "year": 1970
}
date = datedict["date"]
year = datedict.get("year")

print(date, year)


# dictionary with integer keys
my_dict = {1: 'apple', 2: 'ball',3: 'ball'}
print(1 in my_dict)
print('apple' in my_dict)
print('apple' in my_dict.values())


tuple1 = (1,2,3)
tuple2 = (1,2,4)
print (tuple1 == tuple2)  # False
print (tuple1 < tuple2)    # True
print (tuple1 > tuple2)    # False
