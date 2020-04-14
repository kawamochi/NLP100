def cipher(s):
    return ''.join(chr(219 - ord(c)) if 'a' <= c <= 'z' else c for c in s)
s = cipher("cipher")
print(s)
print(cipher(s))