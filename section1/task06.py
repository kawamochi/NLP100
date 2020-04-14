def n_gram(it, n):
  return [ it[i:i + n] for i in range(len(it) - n + 1)]
s1 = set(n_gram("paraparaparadise",2))
s2 = set(n_gram("paragraph",2))
print("和集合：",s1.union(s2))
print("積集合：",s1.intersection(s2))
print("差集合：",s1.difference(s2))
if 'se' in s1:
    print('se in X')
else:
    print('not se in X')
if 'se' in s2:
    print('se in Y')
else:
    print('not se in Y')