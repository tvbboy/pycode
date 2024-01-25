# 成绩列表
stu_score = {"zhangsan": "98.123", "lisi": "58.456", "wangwu": "67.986", "laowang": 99.22,
                 "xiaoxia": "57.333", "liming": 'Null', "zhangjin": "154.213", 
                 "jingsong": "-24.345", "liusong": '',"niuniu":'Null',"lili":-13.123}
stu1=filter(lambda k:not str(stu_score[k]).isdigit() and str(stu_score[k]).count("-")==0 and str(stu_score[k]).count(".")==0,stu_score)
temp=list(stu1).copy()
print("filter:",temp)
for tmp in temp:
  stu_score.pop(tmp)
#map(lambda (k,v):stu_score[k]=float(v),stu_score.items())
for k,v in stu_score.items():
  stu_score[k]=round(float(v),2)
#stu1=map(lambda (k,v):p[k]=v,stu_score.items())
#map(lambda (k,v): p(k+'1',v+'1'), stu_score.items())
# student1=filter(lambda k:student_score[k]>100 or student_score[k]<0,student_score)
# for tmp in list(student1):
#   student_score.pop(tmp)
print(stu_score)

