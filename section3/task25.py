import json
import re
path = './jawiki-country.json'
with open(path) as f:
    for i in f:
        data = json.loads(i)
        if data['title']=='イギリス':
            json_data = data
text = json_data['text']
#print(text)
pattern = re.compile(r'^\{\{基礎情報.*?$(.*?)^\}\}$', re.MULTILINE + re.VERBOSE + re.DOTALL)
# 基礎情報テンプレートの抽出
res = pattern.findall(text)
pattern2 = re.compile('^\|(.+?) = (.+?$)',re.MULTILINE)
res2 = pattern2.findall(res[0])
d = dict()
for i in res2:
    print(i)
    d[i[0]]=i[1]
