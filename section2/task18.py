path = 'popular-names.txt'
with open(path) as f:
    s = f.read().split('\n')
l = [i.split() for i in s[:-1]]
l = sorted(l,key=lambda t: t[2],reverse=True)
path_w = 'task18.txt'
res = ""
for i in l:
    s = '\t'.join(i)
    res+=s+'\n'
with open(path_w,mode='w') as f:
    f.write(res)