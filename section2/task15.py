path = 'popular-names.txt'
with open(path) as f:
    s = f.read().split('\n')
n = int(input())
for i in range(n):
    print(s[len(s)-n+i-1])
