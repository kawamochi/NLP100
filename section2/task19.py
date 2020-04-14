from collections import Counter
path = 'popular-names.txt'
with open(path) as f:
    s = f.read().split('\n')
l = [i.split() for i in s[:-1]]
col1 = [i[0] for i in l]
c = Counter(col1)
l = sorted(l,key=lambda t: c[t[0]],reverse=True)
path_w = 'task19.txt'
res = ""
for i in l:
    s = '\t'.join(i)
    res+=s+'\n'
with open(path_w,mode='w') as f:
    f.write(res)