#在密码学中，恺撒密码是一种最简单且最广为人知的加密技术。
#它是一种替换加密的技术，明文中的所有字母都在字母表上向后（或向前）按照一个固定数目进行偏移后被替换成密文。
#例，当偏移量是3的时候，所有的字母A将被替换成D，B变成E，以此类推。这个加密方法是以恺撒的名字命名的，
#当年恺撒曾用此方法与其将军们进行联系。请实现下述功能：输入字符串和偏移量，如果是大小写字母加密后依然是大字母，数字不加密。输出加密处理后的字符串。
string=input("please input a string:")
offset=int(input("please input a offset:"))
pattern_upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
pattern_lower=pattern_upper.lower()
string_en=""
for cha in string:
    if cha.isupper():
        cha_index=pattern_upper.find(cha)
        cha_index+=offset
        cha_index=cha_index%26
        cha=pattern_upper[cha_index]
    elif cha.islower():
        cha_index=pattern_lower.find(cha)
        cha_index+=offset
        cha_index=cha_index%26
        cha=pattern_lower[cha_index]
    string_en+=cha
print("after encoder,string is:",string_en)