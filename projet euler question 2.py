# probleme 23
#Conclusion: Pour l'instant, TOUJOURS TRIER QUAND ON INSERE et utiliser des tableaux si on connait la taille de nos fichiers.
# PLUS ATTENTION QUAND ON MODIFIE UN ENTIER DANS UNE FONCTION, CELA NE MODIFIE PAS SA VALEUR EN DEHORS
# Attend, le problème viendrait du fait qu'on les liste et on doit les garders alors en mémoire?
# le .append est bien en complexité linéaire, c'est le test de verification qui posse problème?!!
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


from math import *
def sommediviseurs(n): # Renvoie la somme de tous les diviseurs de n, IL NE COMPTE PAS n
    somme=1
    for k in range(2,int(sqrt(n))+1):
        #♠print(k)
        if n%k==0:
            #print(k,n//k)
            if k!= sqrt(n):
                somme=k+somme+n//k # On ajoute k , n/k et la somme initial
            else:
                somme+=k


    return somme


def estabundant(n):
    return sommediviseurs(n)>n



def listeabundantnumber(p):
    # Renvoie la liste des nombres abondants k <p

    resultat=[0 for k in range(p)]
    marqueur= 0
    for k in range(1,p):

        if estabundant(k):
            resultat[marqueur]=k
            marqueur+=1

    return resultat[:marqueur]


print("sommediviseur",sommediviseurs(12))

def gererinsertion(somme,resultat,marqueur):
    # On suppose
    if marqueur==0:
        resultat[0]=somme
        return 1
    else:
        # On vérifie que la somme n'est pas déjà dedans

        qualite= True
        for k in range(marqueur):
            if resultat[k]==somme:
                qualite=False

        # La somme n'est pas dedans
        if qualite:

            resultat[marqueur]=somme
            test=True
            k=marqueur-1
            while k>=0 and test:
                if resultat[k+1]<resultat[k]:
                    resultat[k+1],resultat[k]= resultat[k],resultat[k+1]
                    k=k-1

                else:
                    test=False
        marqueur+=1
        return marqueur

def listesommeabundantnumber(p):
    resultat=[0 for k in range(p**2)]
    finliste=0
    labnumber=listeabundantnumber(p)
    print("on a calculer la liste des nombres abondant ")
    for indpremier in range(len(labnumber)):
        for indsecond in range(indpremier,len(labnumber) ):
            premierabnumber= labnumber[indpremier]
            secabnumber=labnumber[indsecond]
            somme=secabnumber+premierabnumber
            #print("somme quon va inserer",somme,"finliste",finliste,"resultat",resultat[:finliste])

            finliste=gererinsertion(somme,resultat,finliste)
            #print("finliste apres algo",finliste)
    #print("finliste",finliste)
    return resultat[:finliste]


# Ici, on pourrait améliorer la complexité en triant in place le résultat obtenu, la recherche alors de if not serait plus simple
#TOUJOURS TRIER LE RESULTAT ENFAITE
def listesnonabundantnumber(p):
    listesomme=listesommeabundantnumber(p)
    return listesomme
    print("on a passé le tri rapide")
    nombremaximum=listesomme[-1]

    resultat=[True for k in range(nombremaximum+1)] # Il contient que des True, si c'est bien une somme, non sinon

    for element in listesomme:
        resultat[element]=False
    return resultat


def sommenonabundantnumber(p):
    liste=listesnonabundantnumber(p)
    print(len(liste))
    somme=0
    for k in range(len(liste)):
        if liste[k]:
            somme+=k
    return somme


"""
resultat=[1,2,3,0]
finliste=0
somme=10
finliste=gererinsertion(somme,resultat,marqueur)
print(finliste)
"""

#a=listesommeabundantnumber(2000)
#print(a)


## Nouvel angle d'attaque
from math import *
def sommediviseurs(n): # Renvoie la somme de tous les diviseurs de n, IL NE COMPTE PAS n
    somme=1
    for k in range(2,int(sqrt(n))+1):
        #♠print(k)
        if n%k==0:
            #print(k,n//k)
            if k!= sqrt(n):
                somme=k+somme+n//k # On ajoute k , n/k et la somme initial
            else:
                somme+=k


    return somme


def estabundant(n):
    return sommediviseurs(n)>n



def listeabundantnumber(p):
    # Renvoie la liste des nombres abondants k <p

    resultat=[]
    for k in range(1,p):
        if estabundant(k):
            resultat.append(k)
    return resultat

def sommeapartirdelisteabudantnumber(p):
    l=listeabundantnumber(p)
    tableauverificateur=[0 for k in range (4*p)]
    print(" on est a la deuxieme phasse relou ")
    sommetotal=0
    for i1 in range(len(l)):
        for i2 in range(i1,len(l)):
            abnum1=l[i1]
            abnum2=l[i2]
            somme=abnum1+abnum2
            #print(somme,4*p)
            if tableauverificateur[somme]==0 and somme<=28123:
                sommetotal+=somme
                tableauverificateur[somme]=1

    return sommetotal




#Question 24

