path1 = 'col1.txt'
path2 = 'col2.txt'
s = " "
with open(path1) as f:
    col1 = f.read().split()
with open(path2) as f:
    col2 = f.read().split()
for i in range(len(col1)):
    s+=col1[i]+'\t' + col2[i]+'\n'
path_w = 'task13.txt'
with open(path_w,mode='w') as f:
    f.write(s)