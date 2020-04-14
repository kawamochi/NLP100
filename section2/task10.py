path = './popular-names.txt'
with open(path) as f:
    s = f.read()
    print(s.count('\n'))