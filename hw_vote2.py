vote1 = ['柴进', '卢俊义', '柴进', '柴进', '柴进', '柴进', '卢俊义', '柴进', '弃权',
         '卢俊义', '柴进', '柴进', '卢俊义', '柴进', '卢俊义', '卢俊义', '弃权']
vote2 = ['卢俊义', '柴进', '柴进', '董平', '卢俊义', '卢俊义', '柴进', '弃权',
         '武松', '史进', '柴进', '卢俊义', '柴进', '林冲', '卢俊义', '弃权', '弃权']
vote3 = ['卢俊义', '柴进', '柴进', '柴进', '卢俊义', '吴用', '林冲', '卢俊义', '柴进', '柴进','弃权', '史进', '吴用', '卢俊义', '柴进', '林冲', '宋江', '宋江', '卢俊义', '弃权', '弃权']
vote4=['鲁智深','弃权','花荣','弃权','林冲','弃权','弃权','史进','吴用','弃权','柴进','弃权','宋江','宋江','卢俊义','弃权','弃权']
vote_all=[vote1,vote2,vote3,vote4]
promotion_list=[]
vote_set=[]
valid_total=0
for vote_temp in vote_all:
    #print(vote_temp.count('弃权'),"---",len(vote_temp)*2/3)
    #统计有效票数
    valid_total+=(len(vote_temp)-vote_temp.count('弃权'))
    ##正常组
    if vote_temp.count('弃权')<=(len(vote_temp)*1/3):
        vote_set.append(set(vote_temp))
#print(vote_set)
vote_and=vote_set[0]
for vote_temp in vote_set:
    vote_and=vote_and & vote_temp
#print(vote_and)

for general in vote_and:
    general_count=0
    for vote_temp in vote_all:
        general_count+=vote_temp.count(general)
    if general_count>valid_total*0.35:
        promotion_list.append([general,str(general_count)+"票","得票率:",str(round(general_count/valid_total,2))])
print("晋级名单:",promotion_list)