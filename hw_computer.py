# 按照下列要求，设计完成一个程序。
# 程序功能：电脑销售员一次性输入若干电脑配件的销售情况，按毛利降序排序生成商品名、毛利统计报表。
# 输入数据格式："商品名1 进价1 售价1 销售量1,商品名2 进价2 售价2 销售量2……"。
# 商品名、进价、售价、销售量之间用半角空格分隔，各商品之间用半角逗号分隔。
# 例如：主板 1850 2100.5 19,路由器r83 120 149 28,内存16g 380 420 38。
# 毛利计算：毛利 = ( 售价 - 进价 ) × 销售量
# 输出格式：各商品名和毛利，中间用","间隔，毛利保留小数点后2位，并按毛利降序排序。
# pro1.py 文件中前端注释语句可以在调试程序时用复制、粘贴作为输入数据，方便调试。其它现成的代码不可改动。
# 程序运行示例：
# 请输入由半角空格分隔的品名、进价、售价、销售量，各商品间用半角逗号分隔：
# 主板 1850 2100.5 19,路由器r83 120 149 28,内存16g 380 420 38,SSD硬盘1T 590 649 23,U盘1T 799 899 32
# 商品名,毛利主板,4759.50
# U盘1T,3200.00
# 内存16g,1520.00
# SSD硬盘1T,1357.00
# 路由器r83,812.00
def calpay(tmpli):
    a=float(tmpli[0])
    b=float(tmpli[1])
    c=float(tmpli[2])
    return (a-b)*c
mystr=input("请输入由半角空格分隔的品名、进价、售价、销售量，各商品间用半角逗号分隔：")
mylist=mystr.split(",")
sublist=[]
for item in mylist:
    templist=[]
    templist.append(item.split(' ')[0])
    templist.append(calpay(item.split(' ')[1:]))
    sublist.append(templist)

sublist.sort(key=lambda ele: ele[1],reverse=True)
print(sublist)
# for item in sublist:
#     print(item[0],item[1])


