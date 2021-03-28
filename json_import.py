#!/home/andrei/.pyenv/shims/python3
import json
from pprint import pprint
lis = []
with open('survey_results.json', 'r', encoding='utf-8') as f:
    text = json.load(f)
    for dic in text:
        if dic['sex'] == 'm':
            lis.append(dic['answers'][0]['answer'])
    #pprint(text)
res_dic = {}
for i in lis:
    res_dic[i] = lis.count(i)
print(res_dic)

