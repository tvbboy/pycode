from math import sqrt

def getMean(li):
    return sum(li)/len(li)
def getstd(li, mean):
    sum = 0
    for i in range(len(li)):
        sum += (li[i]-mean)**2
    return sqrt(sum/len(li))
def getCov(list1,list2):
    sum=0
    mean_list1=getMean(list1)
    mean_list2=getMean(list2)
    for i in range(0,len(list1)):
        sum+=(list1[i]-mean_list1)*(list2[i]-mean_list2)
    return sum/len(list1)
liYu=[86,97,98,77,92,94,99,97]
liMa=[92,91,93,88,96,91,91,88]
liEn=[100,96,94,60,97,92,93,86]
print("语文课的平均成绩{0},最高分：{1}".format(sum(liYu)/len(liYu),max(liYu)))
print("数学课的平均成绩{0},最高分：{1}".format(sum(liMa)/len(liMa),max(liMa)))
print("英语课的平均成绩{0},最高分：{1}".format(sum(liEn)/len(liEn),max(liEn)))
print("语文与数学的协方差：",getCov(liYu,liMa))
print("英语与数学的协方差：",getCov(liEn,liMa))
print("语文与英语的协方差：",getCov(liYu,liEn))
