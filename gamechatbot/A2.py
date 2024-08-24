import pandas as pd
df = pd.read_excel('gamechatbot/data.xlsx')
df = df.fillna("0")
questionList = df['A1'].tolist()
answerList = df['A2'].tolist()
questionlist2 = df['A3'].tolist()
annswerlist2 = df['A4'].tolist()
annswerlist3 = df['A5'].tolist()
totalQuestion = len(questionlist2)

pair = []
answer = ""
count = 0
for i in range(totalQuestion):  
    if answerList[i] != "0":
        pair.insert(i, [answerList[i],[questionlist2[i]]])
        answer = answerList[i]
    else:
        pair.insert(i, [answer,[questionlist2[i]]])
combined_data = {}

for prompt, response in pair:
    if prompt in combined_data:
        combined_data[prompt].extend(response)
    else:
        combined_data[prompt] = response

A2 = [[prompt, responses] for prompt, responses in combined_data.items()]

