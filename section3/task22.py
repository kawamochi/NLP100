import json
import re
path = './jawiki-country.json'
with open(path) as f:
    for i in f:
        data = json.loads(i)
        if data['title']=='イギリス':
            json_data = data
text = json_data['text']
pattern = re.compile('\[\[Category:.*\]\]')
res = pattern.findall(text)
for i in res:
    t = i.split(':')
    print(t[1][:-2].replace('|*',''))