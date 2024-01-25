#输入一个人的数据，str,输出考勤分
def cal_score(p_list):
    score=0
    #p_list=['10225102494', '陈稷豪', '已打卡', '已打卡', '已打卡', '已打卡', '已打卡', '已打卡', '已打卡', '已打卡', '已打卡', '已打卡', '已打卡', '已打卡', '已打卡', '已打卡', '已打卡', '已打卡', '已打卡', '已打卡', '已打卡']
    total_num=len(p_list)-2
    present_num=p_list.count('已打卡')
    absent_num=p_list.count("未打卡")
    
    score=(100/total_num) *present_num
    #-------扣分
    score_a=(100/(total_num/3))*absent_num
    score=score-score_a
    if(score<0):
        score=0
    if(absent_num>total_num/3):
        score=-1
    return str(int(score))  #转为整数是为了去除小数，转为字符串，是方便后续将结果写入到新的考勤文件
file=r"../absent.csv"
target_file=r"../absent_handled.csv"
fi=open(file,'r')
csv_list=fi.readlines() #每行一个元素
csv_list_title=csv_list[0] # 标题拿出来
data=csv_list[1:len(csv_list)-3] # 去头，去尾巴
print("total stu:",len(data))
print(data)
csv_list_data=[]
for item in data:
    subli=item.replace(',\n','').split(',')
    subli.append(cal_score(subli))
    csv_list_data.append(subli)
print(csv_list_data)
fi.close()
## 写回文件
f=open(target_file,"w")
f.write(str(csv_list_title).replace('\n','百分制,\n'))
for i in range(0, len(csv_list_data)):
    f.write(','.join(csv_list_data[i])+'\n')
#tmp = '\n'
#print('\n'.join(csv_list_data))
#f.write(tmp.join(csv_list_data))
#f.writelines(csv_list_data)
f.close()
