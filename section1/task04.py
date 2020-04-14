l = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.".split()
s = {1, 5, 6, 7, 8, 9, 15, 16, 19}
d = dict()
for i in range(len(l)):
    if i+1 in s:
        d[l[i][:1]]=i+1
    else:
        d[l[i][:2]]=i+1
print(d)
