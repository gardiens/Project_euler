def quest1(n):
    somme=0
    for k in range(n):
        if k%3==0 or k%5==0:
            somme+=k

    return somme



def quest2(n):
    somme=0
    fib1=0
    fib2=1
    while fib2<n:
        nvfib=fib2+fib1
        if fib2%2==0:
            somme+=fib2

        fib1,fib2=fib2,nvfib
    return somme



def largestprimefactor(n):
    diviseuretudier = 1
    decomposition=n
    while decomposition!=1: # On va découper n pour avoir des facteurs premieres de plus en plus petit
        diviseuretudier+=1
        #print(decomposition,diviseuretudier)
        while decomposition%diviseuretudier ==0:# le diviseur étudié divise n ( il est nécessairement premier
            decomposition= decomposition/diviseuretudier


    return diviseuretudier


#print(largestprimefactor(600851475143))

# Question 3 Projet EUler
def listechiffre(n): # Renvoie la liste des chiffres en base 10 d'un nombre
    #puissance10inf= ent(log(n,10))
    chiffre=[]
    def recupererchiffre(n):
        if n<10:
            chiffre.append(n)
        else:
            chiffrepuissanceassocie=n%10
            chiffre.append(chiffrepuissanceassocie)
            recupererchiffre(n//10)

    recupererchiffre(n)
    return chiffre

def inverserliste(l): # Inverse une liste
    resultat=[0 for k in range(len(l))]
    n=len(l)
    for k in range(len(l)):
        resultat[k]=l[(n-1)-k]
    return resultat



def verifiepalindrome(n):
    chiffre= listechiffre(n)
    #print(chiffre)
    chiffreinv=inverserliste(chiffre)
    return chiffre==chiffreinv



def troisdigit(n):
    max=0
    for k1 in range(100,1000):
        for k2 in range(100,1000):
            n=k1*k2
            if verifiepalindrome(n):
                if max==0 or n>max:
                    max=n
    return max

#print(troisdigit(3))


# Question 4 : trouver plus petit nombre divisible par tous les nombres entre 1 et 20

def decompofacteurpremier(n): # Renvoie la liste des facteurs premier avec leur exposant
    diviseuretudier = 1
    decomposition=n
    decompositionl=[]
    while decomposition!=1: # On va découper n pour avoir des facteurs premieres de plus en plus petit
        diviseuretudier+=1
        #print(decomposition,diviseuretudier)
        if decomposition%diviseuretudier ==0:
            exposant=0
            while decomposition%diviseuretudier ==0:# le diviseur étudié divise n ( il est nécessairement premier)
                decomposition= decomposition/diviseuretudier
                exposant+=1
            decompositionl.append([diviseuretudier,exposant])
    return decompositionl


    return diviseuretudier

def ppcm(n): # Ppcm de tous les nombre entre 1 et n

    ppcm=1
    decppcm=[[1,1]] # liste de la forme ( nombre premier, exposant associé)
    for k in range(2,n+1):
        if k%ppcm!=0 or ppcm==1: # Ils ont un facteur commun
            #print("il se passe quoi ")
            deck=decompofacteurpremier(k)
            indiceassocie=0
            for indice in range (len(deck)):
                premierk=deck[indice][0]
                exposantk=deck[indice][1]
                print("exposant etudier",premierk,exposantk)
                premiern=decppcm[indiceassocie][0]

                while premierk != premiern  and indiceassocie<len(decppcm):
                    #print(indiceassocie,"dans boucle",len(decppcm))
                    #print("premiern",premiern,decppcm,indiceassocie)
                    #print("comparaison",premierk,premiern)
                    indiceassocie+=1
                    if indiceassocie<len(decppcm) :
                        premiern=decppcm[indiceassocie][0]
                    #print("premier n après changement ",premiern)

                     # On  regarde le nombre premier suivant
                print("indice associe",indiceassocie,"len",len(decppcm))
                if indiceassocie<len(decppcm):
                    #print("changement",premierk,deck[indice][1])
                    # Ici, On choisit le plus grand des deux exposants pour changer la decomposition
                    decppcm[indiceassocie][1]=max(deck[indice][1],decppcm[indiceassocie][1])

                # Ici, on a que le nombre premier n'est pas dans la liste, on l'ajoute
                if indiceassocie==len(decppcm):
                    decppcm.append([premierk,deck[indice][1]])
                    # normalement, on peut avoir qu'un seul de ce type dans une décomposition, donc on n'a pas à faire attention que indie associe est out of bourn
        ppcm=listeversppcm(decppcm)
        #print(ppcm)
    return decppcm



def listeversppcm(l):
    ppcm=1

    for [premier,exposant] in l :
        ppcm=ppcm*premier**exposant
    return ppcm


from math import sqrt
from math import log
# Sinon on sait pour le ppcm , que il sera de la forme produit des pi avec le plus grand exposant tel que pi^^alpha <n
"""
def listenombrepremier(n):
    resultat=[]
    for k in range(2,n):
        marqueur=True
        #print(sqrt(k))
        for indice in range(2,int(sqrt(k))+1):
            #print("a")
            if k%indice==0:
                #print("aa")
                marqueur=False
        if marqueur==True :
            resultat.append(k)

    return resultat
"""


def ppcmameliore(n): # Version améliorer du ppcm de tous les nombres entre 1 et n
    lnombrepremier=listenombrepremier(n)
    N=1 # C'est le resultat

    for nombrepremier in lnombrepremier:
        print("ici",nombrepremier,n)
        exposant=int(log(n,nombrepremier))
        N=N* nombrepremier**exposant
    return N




# Quesiton sum square difference

def somme(n): # Somme de 1 a n des k
    return (n*(n+1))/2

def sommecube(n): # somme des 1 a n des k²²
    return n*(n+1)*(2*n+1)/6

def question(n):
    return (somme(n))**2-sommecube(n)


# 1001st prime number


def listenombrepremier(n): # Renvoie la liste des nombres premiers entre 1 et n
    resultat=[2]
    marqueur1=True
    k=2

    while marqueur1:
        if k%2 !=0:
            marqueur=True
            for premier in resultat:
                #print("a")
                if premier<= sqrt(k) and k%premier==0:
                    #print("aa")
                    marqueur=False
            if marqueur==True :
                resultat.append(k)
        k+=1

        if k%100000==0:
            print(k)
        if k==n:
            marqueur1=False
        #print(len(resultat))
    return resultat
"""
resultat= listenombrepremier1001(10005)
print(len(resultat))

"""



# Initialisation, on récupère la liste

def trouverabc(n):
    # On cherche a,b,c tel que a²+b² =c² et a+b+c =1000

    for a in range(1,999):
        print("a",a)
        marqueur=True
        b=a-1
        while marqueur:
            b+=1
            c2=a**2+b**2
            c=sqrt(c2)
            if a+b+c==1000:
                return (a,b,c)
            if a+b+c>1000:
                marqueur = False
#"(a,b,c)=trouverabc(1000)
#a=listenombrepremier(int(2e6))
import numpy as np

def sommenombrepremier(n): # Renvoie la somme des nombres premiers entre 1 et n
    somme=2
    for k in range (2,n+1):
        marqueur= True
        entier = 1
        while marqueur and entier <=(sqrt(k)):
            entier+=1
            if k%entier ==0:
                #print("pass")
                marqueur=False
        if marqueur:
            #print(k)
            somme+=k
    return somme
a=sommenombrepremier(10)



# . Append ne marche pas sur des listes trops grande, en faite il fallait initialiser à 0 au tous début pour pas avoir de problème !!!!!!!!!!!


def nombrediviseurs(n): # Renvoie le nombre de diviseurs de n
    somme=0
    for k in range(1,int(sqrt(n))+1):
        if n%k ==0:
            if k ==sqrt(n):
                somme+=1
            else:
                somme+=2
    return somme

def sommediviseurs(n): # Renvoie la somme de tous les diviseurs de n, IL NE COMPTE PAS n
    somme=1
    for k in range(2,int(sqrt(n))):

        if n%k==0:
            #print(k,n//k)
            if k!= int(sqrt(n)):
                somme=k+somme+n//k # On ajoute k , n/k et la somme initial
            else:
                somme+=k

    return somme







def amicalnumber(n):
    somme=0
    liste=[0 for k in range(n)]

    for k in range(n):
        amipotentiel=sommediviseurs(k)
        #print(amipotentiel, "amipotentiel")
        sommeami=sommediviseurs(amipotentiel)
        if k==sommeami and liste[amipotentiel]==0 and sommeami!=amipotentiel:
            print("k",k,liste[sommeami],"sommeami",amipotentiel)
            liste[k]=1
            print(liste[k])
            somme+= k+amipotentiel
    return somme


print(amicalnumber(10000))


def nombretriangulaire(maj):# Renvoie premier nombre triangulaire avec plus de maj diviseurs

    n=1
    nbtriangulaire=somme(n)
    while nombrediviseurs(nbtriangulaire)<maj:
        n+=1
        nbtriangulaire=somme(n)
    return nbtriangulaire


def nextcollatz(k):
    if k%2==0:
        return k//2
    else:
        return 3*k+1
def collatzsequence(n):
    tableaulongueur=np.zeros(2*(n+1))
    tableaulongueur[1]=1
    def aux(k) :
        #print(k,2*(n+1))
        if k<2*(n+1):# On est dans les marges
            #print(k)
            if tableaulongueur[k]!=0 or k==1 :
                return tableaulongueur[k]+1 # La plus longue sous chaine est de longueur k+1
            else:
                #print("ici")
                kprime=nextcollatz(k)
                longueurmaximal=aux(kprime)
                #print(longueurmaximal)
                tableaulongueur[k]=longueurmaximal
                return longueurmaximal+1

        else:
            return aux(nextcollatz(k))+1

    for k in range(2,n+1):
        aux(k)
    return tableaulongueur



#a= collatzsequence(int(1e6))
#print(a)

def maxindice(t):
    indice=0
    for k in range(len(t)):
        if t[k]>t[indice]:
            indice=k
    return indice


# Question 18 , dans un premier temps, il faut transcrire le triangle

# Pour faire cette question, On garde un  tableau associé qui correspond au plus petit cout pour partir du sommet à  l'étape k



def recuperercoutmaximalavant(i,j,t):
    # Renvoie le tuple associé qui a un cout maximal, prend en compte les effets de bords
    p=len(t[i])
    if j==0:
        return max(t[i-1][j],t[i-1][j+1])
    elif j==(p-1): # C'est la bordure
        return t[i-1][j-1]
    elif j==(p-2):
        return max(t[i-1][j],t[i-1][j-1])
    else:
        return max(t[i-1][j],t[i-1][j-1]) # Ici, il fallait faire attention quels étaient les indices qui pouvaient se recnontrer. On avait que deux ancêtre prédéfini
def coutmaximal(t): # Liste de liste déjà prédéfini
    tableauequivalent=t[:][:]
    n=len(t)
    for i in range (1,n):
        print("i",i)
        p=len(t[i])
        for j in range(p):
            print("j",j)
            coutmaximal=recuperercoutmaximalavant(i,j,tableauequivalent)
            tableauequivalent[i][j]=tableauequivalent[i][j]+coutmaximal
    return tableauequivalent

#Transformation de la chaîne de caractère en une liste contenant
#des sous listes (représentant les lignes) qui contiennent
#les nombres de chaque ligne


def factorielle(n):
    somme=1
    for k in range(1,n+1):
        somme=somme*k
    return somme
