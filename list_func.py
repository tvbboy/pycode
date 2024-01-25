list1 = ['Hello', 'Python', 'World']
list2=list("Hello Python World")
print(list2)
languages = ['Python', 'C sharp', 'C', 'C++']
languages[1] = 'C#' 
languages_cp = languages.copy()
print("languages:",languages)
print("languages_cp:",languages_cp)
print("len of languages:",len(languages))
print(languages==languages_cp)


languages = ['Python', 'C sharp', 'C', 'C++']
languages[1] = 'C#' 
languages_cp = languages.copy()
print("languages:",languages)
print("languages_cp:",languages_cp)
languages.append('Java')
print('After append:' , languages)
languages.insert(2, 'JavaScript')
print('After insert:' , languages)


languages.remove('Java')
print("After removing Java:" , languages)
languages.pop()
print("After pop:" , languages)
languages.pop(2)
print("After pop(2):" , languages)
del languages[1]
print("after deleting languages[1]", languages)
languages.clear()
print("after clearing:" , languages)


x = [1,2,3]
z = [4,5,6]
x.extend(z)

languages = ['Python', 'C sharp', 'C', 'C++']
languages[1] = 'C#' 
print("languages:",languages)
languages.append("Java")
print('After append Java:' , languages)
languages.pop()
languages.extend("Java")
print('After extend Java:' , languages)

