from nltk import Chat, reflections
import pandas as pd

df = pd.read_excel('qna.xlsx')
questionList = df['Question'].tolist()
answerList = df['Answer'].tolist()
totalQuestion = len(questionList)

temp = []
tempList = []
for i in range(totalQuestion):
    tempList.append((f"{questionList[i]}",[f"{answerList[i]}"]))
    #tempList.append([temp.append(f"{questionList[i]}"),temp.append([answerList[i]])])
    tempList = [*tempList[0]]
    print(tempList)
    tempList.clear()
#print(temp)

