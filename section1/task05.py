def n_gram(it, n):
  return [ it[i:i + n] for i in range(len(it) - n + 1)]
print(n_gram("I am an NLPer",2))
print(n_gram("I am an NLPer".split(),2))