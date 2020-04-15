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
    for j in i:
        add(j[0])
c = Counter(l)
val = c.values()
val = sorted(val,reverse=True)
x = [i+1 for i in range(len(c))]
plt.scatter(x,val,s=2)
ax = plt.gca()
ax.set_yscale('log')
ax.set_xscale('log')
plt.show()