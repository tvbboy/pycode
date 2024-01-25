######作业二：新建“学号+hw_printstar2.py”，以提示语“please input the line:”接收用户输入的行数，要求行号不能超过26。
#通过行数按照一定逻辑输出如下的图形。（不能使用没有学过的内容）
lines=int(input("please input the line:"))
if lines<=26:
    rows = 5
    for i in range(0, lines):
        for j in range(0, i + 1):
            print("*", end=' ')
        print("\r")

    for i in range(lines, 0, -1):
        for j in range(0, i - 1):
            print("*", end=' ')
        print("\r")
else:
    print("number of lines must <=26")