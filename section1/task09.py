import random
def change_word(s):
    if len(s)<=4:
        return s
    else:
        l = list(s)
        mid = l[1:-1]
        random.shuffle(mid)
        return l[0] + ''.join(mid)+l[-1]

def Typoglycemia(s):
    l = s.split()
    res = [change_word(i) for i in l]
    return ' '.join(res)

print(Typoglycemia("I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."))