import json
path = './jawiki-country.json'
with open(path) as f:
    for i in f:
        data = json.loads(i)
        if data['title']=='イギリス':
            json_data = data
print(json_data['text'])