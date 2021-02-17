import json
from pprint import pprint
lis = []
with open('survey_results.json','r', encoding='utf-8') as f:
    text = json.load(f)
    for dic in text:
        if dic['sex'] == 'm':
            lis.append(dic['answers'][0]['answer'])
    #pprint(text)
ff = {}
for i in lis:
    ff[i] = lis.count(i)
print(lis)
print(ff)
