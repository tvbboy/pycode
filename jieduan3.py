# 统计某字符串中所含的英语字母的频度。程序接受键盘输入的字符串，
# 利用字典统计该字符串中的英语字母和其对应的出现次数，并输出结果。
# 运行结果如下：
# 请输入一字符串：hello world
# h       出现     1次
# e       出现     1次
# l       出现     3次
# o       出现     2次
# w       出现     1次
# r       出现     1次
# d       出现     1次
string = input("请输入一字符串：")
string="hello world"
mydict={}
for chr in string:
    if(chr.isalpha()):
        mydict[chr]=string.count(chr)
#print(mydict)
for k,v in mydict.items():
    print("{0}       出现     {1}次".format(k,v))

