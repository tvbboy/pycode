#https://blog.csdn.net/qq_45978890/article/details/115059675
mylist = ['Apple', 'Grape', 'Orange', 'Pear', 'Cheery', 'Bluebrrey', 'Dew']
print('排序前：')
mylist.sort()
print('排序后：')
print(mylist)


mylist = ['Apple', 'Grape', 'Orange', 'Pear', 'Cheery', 'Bluebrrey', 'Dew']
print('排序前：')
print(mylist)
print('按照长度升序排序：')
mylist.sort(key=lambda ele: len(ele))
print(mylist)

print('按照长度逆序排序：')
mylist.sort(key=lambda ele: len(ele), reverse=True)
print(mylist)



mylist = [['zhangsan', 30, 32000], 
       	['lisi', 25, 15000],
       	['wangwu', 28, 20000],
       	['zhaoliu', 21, 7000]]
print('排序前：')
print(mylist)
print('按照姓名长度排序后：')
mylist.sort(key=lambda ele: len(ele[0]))
print(mylist)


mylist = [['zhangsan', 30, 32000],
       	['lisi', 25, 15000],
       	['wangwu', 28, 20000],
       	['zhaoliu', 21, 7000]]
print('排序前：')
print(mylist)
print('按照年龄大小排序后：')
# 选择年龄属性
mylist.sort(key=lambda ele: ele[1])
print(mylist)
mylist = [['zhangsan', 30, 32000], 
       	['lisi', 25, 15000],
       	['wangwu', 28, 20000],
       	['zhaoliu', 21, 7000]]
print('排序前：')
print(mylist)
print('按照薪水大小排序后：')
# 选择年龄属性
mylist.sort(key=lambda ele: ele[2],reverse=True)
print(mylist)

#字典(dict)的键(key)排序
mydict = {'c': 1, 'b': 9, 'a': 3}
print(sorted(mydict))
# ['a', 'b', 'c']
print(sorted(mydict, reverse=True))
# ['c', 'b', 'a']
#字典(dict)的值(value)排序
print(sorted(mydict,key=lambda a:mydict[a]))