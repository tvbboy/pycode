

print('abc123'.upper())
print("123Python".lower())
print("*"*10)

# String methods--> Part 2
string=" Python "
print("string:",string,"have two spaces",sep='')
print("On using  strip():",string.strip(),".",sep='')
print("On using lstrip():",string.lstrip(),".",sep='')
print("On using rstrip():", string.rstrip(), ".", sep='')
print("*"*10)


####################33333
print('abc'.isalpha())
print('aei4'.isalpha())
print('234'.isdigit())
print('aei4'.isdigit())
print('3.1415'.isdigit())
print('234'.isnumeric())
print('IV'.isnumeric())
print('四'.isnumeric())
print('IV'.isdigit())
print(" ".isspace())
##########################33333
print("*"*10)
print('abc'.islower())
print('aei4'.islower())
print('abAB'.islower())
print('ABC'.isupper())
print("ABC123".isupper())
print("ABCerr".isupper())

##########################33333
print("*"*10)
string = "object oriented programming"
print("Given string :", string)
print('index()')
print("index of 'r' in:'", string, "':", string.index('r'))
#print("index of 'z' in:'", string, "':", string.index('z'))
print('count()')
print("number of 'o' in '", string, "':", string.count('o'))
print('find()')
print("index of 'z' in '", string, "':", string.find('z'))
print("index of 'o' in '", string, "':", string.find('o'))
print('replace()')
print("replacing 'e' with '3' :", string.replace('e', '3'))
print("*"*10)
months="JanFebMarAprMayJunJulAugSepOctNovDec"
print(months[0::3])