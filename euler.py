"""# problème 29
stoppeur = 101
resultat = []
for a in range(2, stoppeur):
    for b in range(2, stoppeur):
        n = a**b
        if not n in resultat:
            resultat.append(n)
"""
"""
"""
# problème 30

resultat = []
for i in range(10):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                for o in range(10):

                    somme = i**5 + j**5 + k**5 + l**5 + o**5
                    # print(somme)
                    nombreetudier = i*10**4+j*10**3+k*10**2+l*10**1+o*10**0
                    if somme == nombreetudier:
                        resultat.append(somme)

print("ON EST PASSER LOL ")
print(resultat[4:])
print(sum(resultat))
"""
for a, b, c, d, e in zip(1, 11):
    print(a, b, c)
"""

print(1**4+6**4+3**4+4**4)
