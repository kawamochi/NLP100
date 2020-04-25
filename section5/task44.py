import pydot

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
    def get_info(self):
        s = ""
        for i in self.morphs:
            s+=i.surface
        return s
    def check_pos(self,pos):
        for i in self.morphs:
            if i.pos==pos:
                return True
        return False


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

# example https://pythonhaven.wordpress.com/2009/12/09/generating_graphs_with_pydot/

graph = pydot.Dot(graph_type='digraph')

for i in res[:10]:
    for j in i:
        if j.to == -1:
            continue
        edge = pydot.Edge(j.get_info(),i[j.to].get_info())
        graph.add_edge(edge)
graph.write_png('task44.png')