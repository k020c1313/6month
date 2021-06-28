import random
import csv

scoreList = [["japanese","math","english","grade"]]

for i in range(10000):
    
    score = [random.randint(0,100), random.randint(0,100), random.randint(0,100)]
    average = sum(score) / 3
    
    if average >= 90:
        score.append("A")
    elif average >= 70:
        score.append("B")
    elif average >= 50:
        score.append("C")
    elif average >= 30:
        score.append("D")
    else:
        score.append("E")
      
    scoreList.append(score)

print(scoreList)

with open("score.csv", "w", encoding="Shift_jis") as f:
    writer = csv.writer(f, lineterminator="\n")
    writer.writerows(scoreList)