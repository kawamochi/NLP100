path = 'popular-names.txt'
with open(path) as f:
    s = f.read().split('\n')
l = [i.split()[0] for i in s[:-1]]
se = set(l)
print(len(se))