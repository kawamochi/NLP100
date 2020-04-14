from collections import Counter
path = './neko.txt.mecab'
with open(path) as f:
    s = f.read()
    sentences = s.split('EOS')
    res = []
    for sentence in sentences:
        t = sentence.split('\n')
        tmp = []
        for i in t:
            l = i.split('\t')
            if(len(l)<2):
                continue
            surface = l[0]
            l = l[1].split(',')
            base = l[-3]
            pos = l[0]
            pos1 = l[1]
            tmp.append((surface,base,pos,pos1))
        res.append(tmp)
l = []
add = l.append
for i in res:
    for j in i:
        add(j[0])
c = Counter(l)
data = []
for p in c.items():
    data.append((p[1],p[0]))
data = sorted(data,reverse=True)
print(data)