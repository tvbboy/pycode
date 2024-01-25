#班长选举的投票情况已存放在两组vote列表中，请计算每位有效提名者（两组均提名）的得票次数、并按得票数从大到小输出结果。
vote1=['鲁智深','柴进','宋江','吴用','林冲','卢俊义','柴进','柴进','孙二娘','史进','吴用','卢俊义','柴进','林冲','宋江','宋江','卢俊义','吴用','吴用']
vote2=['林冲','卢俊义','宋江','吴用','林冲','卢俊义','柴进','柴进','张青','史进','燕青','卢俊义','柴进','林冲','宋江','宋江','卢俊义','吴用','吴用']
set1=set(vote1)
set2=set(vote2)
valid_user=set1&set2
print(valid_user)
valid_list=list(valid_user)
mydict=dict()
vote_num=[]
# print(vote1.count('柴进'))
# print(vote2.count('柴进'))
for user in valid_list:
    mydict[user]=(vote1.count(user)+vote2.count(user))
    vote_num.append(vote1.count(user)+vote2.count(user))
#vote_num=vote_num[::-1]
vote_num.sort(reverse=True)
print(vote_num)
print(mydict)
for item in vote_num:
    for k,v in mydict.items():
        if item==v:
            print(k)
            mydict.pop(k)
            break