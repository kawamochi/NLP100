path = 'popular-names.txt'
n = int(input())
with open(path) as f:
    l = f.read().split('\n')
cnt = (len(l)+n-1)//n
for i in range(n):
    with open('child_{}.txt'.format(i),mode='w') as f:
        for j in l[cnt*i:min(cnt*(n+1),len(l))]:
            f.write(j)
            f.write('\n')
