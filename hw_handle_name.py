# 程序填空-姓名脱敏处理
# 按下列要求对提供程序代码中的下划线进行填空（用填空内容代替下划线，除此之外，不能改动其它任何地方，也不得增删行），调试并运行之。
# a. 程序功能：对多个输入的姓名进行脱敏处理，输出脱敏后的姓名。
# b. 数据脱敏是指对敏感信息进行变形处理，姓名脱敏是指姓正常显示，名用星号“*”代替，不考虑复姓。例如：古丽苏如合 脱敏为 古**** 。
# c. 输入一组空格分隔的姓名，输出脱敏后的姓名，以空格分隔。
# 程序运行示例：
# 请输入多个用空格分隔的姓名：
# 徐晃 夏侯惇 诸葛孔明 孙权
# 输出：
# 徐* 夏** 诸*** 孙*
mystr=input("请输入多个用空格分隔的姓名：")
mylist=mystr.split(" ")
for name in mylist:
    #方法1
    print(name[0]+"*"*(len(name)-1)+" ",end="")
    ##方法2
    # newname=name.replace(name[1:],"*"*len(name[1:]))
    # print(newname+" ",end="")