name1="Python"
name2='Python Ecnu'
name3='Python "ecnu"'
name4=str(99999)
print(name1)
print(name2)
print(name3)
print(name4)


string="PROGRAMIZ"
# accessing the third character
print("string[2] is :",string[2]) 
# accessing the last character
print("string[-1] is :",string[-1]) 
# from the 5th character to the 8th character
print("string[4:8] is :",string[4:8])
# from the last 6th character to the last 4th character
print("string[-6:-2] is :",string[-6:-2])


print("string[3:] is :",string[3:]) 
# accessing all the characters from the 4th character
print("string[-2: ] is :",string[-2:]) 
# accessing all characters from the last 2nd character

# accessing characters till the 5th character
print("string[:5 ] is :", string[:5])
print("string[:] is :",string[:])  # printing the entire string
print("string[3:3] is :",string[3:3])  # printing empty string
# printing all the characters till the last 2nd character
print("string[:-2] is :",string[:-2])  


string="PythonECNU"
print(string[::-1])





####################转义字符
print("a") #输出a
print(" ") #输出空格
#print("
#      ")   #输出回车？？
name4_1="my \name is tvbboy" #输出my 换行 ame is tvbboy
name4_2 = "my \\name is tvbboy"  # 输出my \ name is tvbboy
a
name5_2="my name is \"tvbboy\"" #输出 my name is "tvbboy"
print(name4_1)
print(name4_2)
print(name5_2)
fn = input("Enter first name:")
ln = input("Enter last name:")
print(f"your full name is {fn+ln}\n")
print("your full name is {0}{1}\n".format(fn,ln))
print("your full name is %s%s\n" % (fn, ln))

