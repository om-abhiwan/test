from gamechatbot.nltk import Chat ,reflections ,A2Chat
from gamechatbot.A2 import A2
import pandas as pd
df = pd.read_excel('gamechatbot/data.xlsx')
df = df.fillna("0")
questionList = df['A1'].tolist()
answerList = df['A2'].tolist()
questionlist2 = df['A3'].tolist()
annswerlist2 = df['A4'].tolist()
totalQuestion = len(questionList)

pair = []
for i in range(totalQuestion):
    if questionList[i] != "0":
        pair.insert(i, [questionList[i],[answerList[i]]])
totalQuestion = len(questionList)
for j in range(totalQuestion):
    if questionlist2[j] != "0":
        pair.insert(i, [questionlist2[j],[annswerlist2[j]]])
        i +=1
    else:
        index = len(A2)
        A2.insert(i,[questionlist2[j],[annswerlist2[j],annswerlist2[j-1]]])
# print(pair)
def chatty(queery):
    chat = Chat(pair, reflections)
    value = chat.converse(queery)
    return value

def A2chatty(queery):
    chat = A2Chat(A2, reflections)
    value = chat.converse(queery)
    return value