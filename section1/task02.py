s1 = "パトカー"
s2 = "タクシー"
s = [s2[i//2] if i%2 else s1[i//2] for i in range(8)]
print("".join(s))