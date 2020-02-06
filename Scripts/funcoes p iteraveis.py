import functools

# --------- ALL ---------- # --> verifica se todos os elementos são verdadeiros

r1 = all([1,1,1,0])
r2 = all([1,1,1,1])

# --------- ANY ---------- # --> verifica se pelos um elemento é verdadeiro

r3 = any([0,0,0,0])
r4 = any([0,0,1,0])

# --------- SUM ---------- # --> soma elementos de uma lista

r5 = sum([1,3,4,6])
r6 = sum([1,3,4,6],5)

print(r5,r6)

# --------- REDUCE ---------- # --> caiu em desuso...
