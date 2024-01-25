vote1 = ['柴进', '卢俊义', '柴进', '柴进', '柴进', '柴进', '卢俊义', '柴进', '弃权',
         '卢俊义', '柴进', '柴进', '卢俊义', '柴进', '卢俊义', '卢俊义', '弃权']
vote2 = ['卢俊义', '柴进', '柴进', '董平', '卢俊义', '卢俊义', '柴进', '弃权',
         '武松', '史进', '柴进', '卢俊义', '柴进', '林冲', '卢俊义', '弃权', '弃权']
vote3 = ['卢俊义', '柴进', '柴进', '柴进', '卢俊义', '吴用', '林冲', '卢俊义', '柴进', '柴进','弃权', '史进', '吴用', '卢俊义', '柴进', '林冲', '宋江', '宋江', '卢俊义', '弃权', '弃权']
vote4=['鲁智深','弃权','花荣','弃权','林冲','弃权','弃权','史进','吴用','弃权','柴进','弃权','宋江','宋江','卢俊义','弃权','弃权']
vote_all=[vote1,vote2,vote3,vote4]
vote_valid=[]
promotion_dict=dict() #空字典
valid_total=0
for vote_temp in vote_all:
    valid_total+=(len(vote_temp)-vote_temp.count('弃权'))
    ##正常组
    if vote_temp.count('弃权')<=(len(vote_temp)*1/3):
        vote_valid.append(vote_temp)  #统计总选票
for vote_temp in vote_all:
    for person in set(vote_temp): #在集合中遍历，确保一个人不要重复计票
        if(person!="弃权"):
            if person in promotion_dict:
                dict_temp=promotion_dict[person]
            else:
                dict_temp={"votes":0,"support_groups":0,"vote_rate":0.0} #定义结构
            if vote_temp in vote_valid: #这个组是有效组，支持组数+1
                dict_temp["support_groups"]+=1
            dict_temp["votes"]+=vote_temp.count(person)
            dict_temp["vote_rate"]=round(dict_temp["votes"]/valid_total,2)
            promotion_dict[person]=dict_temp
for k,v in promotion_dict.items():
  print(k,v)