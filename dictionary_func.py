thisdict = {
 "brand": "Ford",
 "model": "Mustang",
 "year": 1964
}

thisdict.pop("model")
print(thisdict)

thisdict = {
 "brand": "Ford",
 "model": "Mustang",
 "year": 1964
}
thisdict.popitem()
print(thisdict)

del thisdict
#print(thisdict) #this will cause an error because “thisdict” no longer exists.

#thisdict.clear()
#print(thisdict)


# dictionary of a sample portfolio
shares1 = {'APPL': 100, 'GOOG': 50}
shares2 = {}

# print the items of the shares1 and shares2
print("Items of shares1:", shares1.items())
print("Items of shares2:", shares2.items())


# dictionary of a sample portfolio
shares1 = {'APPL': 100, 'GOOG': 50}
shares2 = {}

# print the keys of the shares1 and shares2
print("Keys of shares1:", shares1.keys())
print("Keys of shares2:", shares2.keys())

# print the values of the shares1 and shares2
print("Values of shares1:", shares1.values())
print("Values of shares2:", shares2.values())



# dictionary of a sample portfolio
shares ={1: 'apple', 2: 'ball',3:'ball'}
print("shares length:",len(shares))
shares_cp=shares.copy()
# dictionary keys view object
keys = shares.keys()
# iterate over keys
for k in keys:
    print(k)
for k in shares:
    print(k)
for k in shares:
    print(shares[k])
for k in shares.values():
    print(k)
for k, v in shares.items():
    print(k, v)
print(shares[1])
print(shares.get(1))
print(shares.get(3))
print(shares.get(3,'NOT FOUND!'))

shares ={1: 'apple', 2: 'ball',3:'ball'}
shares_new = { 4:"orange" , 5:"banana" }
shares_new.update(shares)
print(shares_new)
shares ={1: 'apple', 2: 'ball',3:'ball'}
shares_new = { 4:"orange" , 5:"banana" }
shares.update(shares_new)
print(shares)
test1={4: 'orange', 5: 'banana', 1: 'apple', 2: 'ball', 3: 'ball'}
test2={1: 'apple', 2: 'ball', 3: 'ball', 4: 'orange', 5: 'banana'}
print(test1==test2)