class Morph():
    def __init__(self,surface,base,pos,pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

path = './neko.txt.cabocha'
with open(path) as f:
    s = f.read()
    sentences = s.split('EOS')
    res = []
    for sentence in sentences:
        t = sentence.split('\n')
        tmp = []
        for i in t:
            if len(i)<1:
                continue
            if i[0]=='*':
                continue
            l = i.split('\t')
            if(len(l)<2):
                continue
            surface = l[0]
            l = l[1].split(',')
            base = l[-3]
            pos = l[0]
            pos1 = l[1]
            tmp.append(Morph(surface,base,pos,pos1))
        res.append(tmp)

for j in res[2]:
    print(j.surface,j.base,j.pos,j.pos1)