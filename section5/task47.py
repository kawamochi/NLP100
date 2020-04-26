class Morph():
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1


class Chunk():
    def __init__(self, info, morphs):
        self.morphs = morphs
        l = info.split()
        self.to = int(l[2][:-1])

    def print_info(self):
        for i in self.morphs:
            print(i.surface, end='')
        print()

    def get_info(self):
        s = ""
        for i in self.morphs:
            s += i.surface
        return s

    def check_pos(self, pos):
        for i in self.morphs:
            if i.pos == pos:
                return i.surface
        return False

    def check_pos1(self, pos1):
        for i in self.morphs:
            if i.pos1 == pos1:
                return i.surface
        return False

    def get_base(self, pos):
        for i in self.morphs:
            if i.pos == pos:
                return i.base
        return False


path = './neko.txt.cabocha'
with open(path) as f:
    s = f.read()
    sentences = s.split('EOS')
    res = []
    for sentence in sentences:
        if len(sentence) < 1:
            continue
        morphs = []
        info = ""
        tmp = []
        for j in sentence.split('\n'):
            if len(j) < 1:
                continue
            if j[0] == '*':
                if info == "":
                    info = j
                else:
                    tmp.append(Chunk(info, morphs))
                    info = j
                    morphs = []
            else:
                l = j.split('\t')
                if(len(l) < 2):
                    continue
                surface = l[0]
                l = l[1].split(',')
                base = l[-3]
                pos = l[0]
                pos1 = l[1]
                morphs.append(Morph(surface, base, pos, pos1))
        if info != "":
            tmp.append(Chunk(info, morphs))
        res.append(tmp)

for i in res:
    for j in range(len(i)):
        meisi = i[j].check_pos1('サ変接続')
        josi = i[j].check_pos('助詞')
        if not (josi and josi == 'を'):
            josi = False
        verb = False
        if i[j].check_pos('動詞'):
            verb = i[j].get_base('動詞')
        if meisi and josi and verb:
            verb = meisi+josi+verb
            particles = []
            surfaces = []
            for k in i:
                if k.to == j:
                    item = k.get_base('助詞')
                    if item:
                        particles.append(item)
                    surfaces.append(k.get_info())
            print(verb, end='\t')
            print(' '.join(particles), end='\t')
            print(' '.join(surfaces))
