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
meisi = set()
for i in res:
    if len(i)==0:
        continue
    tmp = ""
    for j in i:
        if j[2]=="名詞":
            tmp+=j[0]
        else:
            if len(tmp)>0:
                meisi.add(tmp)
            tmp = ""
print(meisi)