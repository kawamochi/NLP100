path = 'popular-names.txt'
with open(path) as f:
    s = f.read()
l = s.split('\n')
path_w1 = 'col1.txt'
path_w2 = 'col2.txt'
col1 = ""
col2 = ""
for i in l[:-1]:
    tmp = i.split('\t')
    col1+=tmp[0]
    col1+='\n'
    col2+=tmp[1]
    col2+='\n'
with open(path_w1,mode='w') as f:
    f.write(col1)
with open(path_w2,mode='w') as f:
    f.write(col2)
