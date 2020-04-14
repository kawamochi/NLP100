from collections import Counter
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Hiragino Maru Gothic Pro', 'Yu Gothic', 'Meirio', 'Takao', 'IPAexGothic', 'IPAPGothic', 'VL PGothic', 'Noto Sans CJK JP']
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
    flag = False
    for j in i:
        if j[0]=='猫':
            flag = True
    if flag:
        for j in i:
            if j[0]!='猫':
                add(j[0])
c = Counter(l)
data = []
for p in c.items():
    data.append((p[1],p[0]))
data = sorted(data,reverse=True)
cnt = [data[i][0] for i in range(10)]
label = [data[i][1] for i in range(10)]
left = [i+1 for i in range(10)]
plt.bar(left,cnt,tick_label=label,align="center")
plt.show()