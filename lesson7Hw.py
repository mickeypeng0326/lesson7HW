scores_list=[]
students=int(input('全班人數:'))
for x in range(students):
    score=int(input('分數:'))
    scores_list.append(score)

max=max(scores_list)
min=min(scores_list)
sum=sum(scores_list)

print('最高分:',max)
print('最低分:',min)
print('平均:',sum/students)


