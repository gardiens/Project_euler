# problème 24
from math import *
def enumererpermutation(l): # La liste correspond à l'ensemble ou on va énumérer les partitions
    n=len(l)
    choisi=[False for k in range(n)]
    touspermutation=[]
    permetudier=[0]*n
    def auxiliaire(permetudier,k):# C'est la fonction récursive qui va lister toutes les permutations
        if k==n:
            touspermutation.append(permetudier[:])
        else:

            for i in range(n):
                if choisi[i]==False: #On a pas encore étudier la permutation
                    permetudier[k]=l[i]
                    choisi[i]=True
                    auxiliaire( permetudier,k+1) # On étudie les permutations   avec la permutation qui possède l'element i
                    choisi[i]=False # On rénitialise choisi



    auxiliaire(permetudier,0)
    return touspermutation




l=[0,1,2,3,4,5,6,7,8,9]

a=enumererpermutation(l)
##Tri rapide

def partition(t, p, r):
    """pivot = t[p] inséré à la bonne place t[i], la fonction renvoie i"""
    i = p # au départ, t[p]<=pivot (car il lui est égal)
    for j in range(p+1, r): # on explore à partir de p+1
        # si t[j]>t[p], on ne fait rien car t[j] est à la fin de la
        # zone explorée, là où sont les termes supérieurs au pivot
        if t[j]<=t[p]: # par contre si t[j]<=t[p]...
            i += 1 # il faut décaler la frontière (un terme de plus dans
            # la partie gauche)
            t[j], t[i] = t[i], t[j] # on échange t[i] (qui est maintentant
        # le premier des plus grands que le pivot)
        # avec t[j] qui va dans la partie gauche
    t[p], t[i] = t[i], t[p] # à la fin, un échange suffit à mettre le pivot
            # à sa place
    return i # on renvoie la position où le pivot a été placé
def tri_rapide_rec(t, p, r):
    """trie t[p:r]"""
    if r<=p+1:
        return None
    q = partition(t, p, r)
    tri_rapide_rec(t, p, q)
    tri_rapide_rec(t, q+1, r)

def tri_rapide(t):
    tri_rapide_rec(t, 0, len(t))
        ## fin traitement de donnée

def concatener(l):
    n=len(l)
    somme= 0
    for k in range(n):
        element=l[k]
        somme+= element *(10)**((n-1)-k)
    return somme
""""
print("on est la ")
tri_rapide(a)
print("on a fini ")
print(a[1e6-1 ])"""

def trierliste(l):
    resultat=[]
    for liste in l:
        s= concatener(liste)
        resultat.append(s)
    return resultat