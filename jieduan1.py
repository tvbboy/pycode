
# 程序功能：编程判断输入的数是否为对称数，(对称数是左右两边对称的位上的数都相等的数)
# #运行结果如下：
# 请输入一个非负整数：
# 12321
# 12321是对称数
# 请输入一个非负整数：
# 12351
# 12351不是对称数
# 请输入一个非负整数：
# abba
# 你输入的不是非负整数
number=input("请输入一个非负整数：\n")
success=True
for ch in number:
    if(not ch.isdigit()):
        print("你输入的不是非负整数")
        success=False
        break
if success:
    if(number==number[::-1]):
        result="是对称数";
    else:
        result="不是对称数";
    print(number+result);
#------------------------------------------------------------------
#方法2：

# 程序功能：编程判断输入的数是否为对称数，(对称数是左右两边对称的位上的数都相等的数)
# #运行结果如下：
# 请输入一个非负整数：
# 12321
# 12321是对称数
# 请输入一个非负整数：
# 12351
# 12351不是对称数
# 请输入一个非负整数：
# abba
# 你输入的不是非负整数
number=input("请输入一个非负整数：\n")
if number.isdigit():
    if int(number)>0:
        if(number==number[::-1]):
            result="是对称数";
        else:
            result="不是对称数";
        print(number+result);
    else:
        print("你输入的不是非负整数")
else:
    print("你输入的不是非负整数")
