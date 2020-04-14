path = './popular-names.txt'
path_w = './task11.txt'
with open(path) as f:
    s = f.read()
    s = s.replace('\t',' ')

with open(path_w, mode='w') as f:
    f.write(s)