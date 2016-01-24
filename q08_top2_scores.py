#q08_top2_scores.py
#displays top 2 scorers and scores based on input

#input
r = int(input("Number of students: "))
names = [r]
scores = [r]

print() #insert blank line

for i in range(0,r):
    names.insert(i,str(input("Name of student {}:".format(i+1)))) #update list names
    scores.insert(i,int(input("Score for {}: ".format(names[i])))) #update list scores
    print()#insert blank line


#get max scorer
max_score = max(scores)
max_index = scores.index(max_score)

#show max scorer and score
print(names[max_index])
print(max_score)

scores[max_index] = 0 #set max score in scores list to min score

if r >1:
    #get second max scorer
    second_max_score = max(scores)
    second_max_index = scores.index(second_max_score)

    #show second max scorer and score
    print(names[second_max_index])
    print(second_max_score)
