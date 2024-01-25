# 公司某一地区连锁门店一个月的利润输入到字符串shopInfo中， 
# 利润信息字符串输入格式为:"12号店 48528 23号店 56380 
# 18号店 32854 4号店 68385 53号店 92383 6号店 28387 37号店 40238 8号店 70823"
# 1. 需将各门店以及该门店的利润组成[[店名1,利润1],[店名2,利润2],[店名3,利润3],...]的二维列表并输出。
# 2.同时计算输出利润最高的店名和利润值。
# 运行结果如下：
# 请输入利润信息：
# "12号店 48528 23号店 56380 18号店 32854 4号店 68385 53号店 92383 6号店 28387 37号店 40238 8号店 70823"
# 各店名和利润如下：
# [['12号店', 48528], ['23号店', 56380], ['18号店', 32854], ['4号店', 68385], ['53号店', 92383], ['6号店', 28387], ['37号店', 40238], ['8号店', 70823]]
# 53号店利润最高为：92383
#shopInfo=input("请输入利润信息：")
shopInfo = "12号店 48528 23号店 56380 18号店 32854 4号店 68385 53号店 92383 6号店 28387 37号店 40238 8号店 70823"
temp_list=shopInfo.split()
list_shop=temp_list[0:len(temp_list):2]
list_money=temp_list[1:len(temp_list):2]
print(list_shop)
print(list_money)
list_result=[]
max_index=0
max_money=int(list_money[max_index]) #初始化
for i in range(0,len(list_shop)):
    temp=[list_shop[i],int(list_money[i])]
    list_result.append(temp)
    if int(list_money[i])>max_money:
        max_index=i
        max_money = int(list_money[max_index])
print("各店名和利润如下：")
print(list_result)
print("{0}利润最高为：{1}".format(list_shop[max_index],max_money))
