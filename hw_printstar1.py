######作业一：新建“学号+hw_printstar.py”，以提示语“please input the line:”接收用户输入的行数，要求行号不能超过26。
#通过行数按照一定逻辑输出如下的菱形。（不能使用没有学过的内容）
lines=int(input("please input the line:"))
if lines<=26:
    for i in range(lines+1):
        print(" "*(lines-i)+"*"*(2*i-1))
    for i in range(lines,0,-1):
        print(" "*(lines-i)+"*"*(2*i-1))
else:
    print("number of lines must <=26")