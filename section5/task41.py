class Morph():
    def __init__(self,surface,base,pos,pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1


class Chunk():
    def __init__(self,info,morphs):
        self.morphs = morphs
        l = info.split()
        self.to = int(l[2][:-1])
    def print_info(self):
        for i in self.morphs:
            print(i.surface,end='')
        print()


path = './neko.txt.cabocha'
with open(path) as f:
    s = f.read()
    sentences = s.split('EOS')
    res = []
    for sentence in sentences:
        if len(sentence)<1:
            continue
        morphs = []
        info = ""
        tmp = []
        for j in sentence.split('\n'):
            if len(j)<1:
                continue
            if j[0]=='*':
                if info=="":
                    info = j
                else:
                    tmp.append(Chunk(info,morphs))
                    info = j
                    morphs = []
            else:
                l = j.split('\t')
                if(len(l)<2):
                    continue
                surface = l[0]
                l = l[1].split(',')
                base = l[-3]
                pos = l[0]
                pos1 = l[1]
                morphs.append(Morph(surface,base,pos,pos1))
        if info!="":
            tmp.append(Chunk(info,morphs))
        res.append(tmp)

for j in range(len(res[7])):
    print(j,res[7][j].to,end=' ')
    res[7][j].print_info()