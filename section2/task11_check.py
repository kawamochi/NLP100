path = './popular-names.txt'
path2 = './test.txt'
with open(path) as f:
    s = f.read()

with open(path2) as f:
    s2 = f.read()

if s==s2:
    print('Yes')
else:
    print('No')