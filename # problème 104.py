# problème 104
# Mettre un string c'est jamais  un bon bail !  On a fortement augmenté lacomplexité
# je pense qu'il faut arreter de stocker les résultat avec fibopti, on perd trop de donnée
from math import log10, floor
from math import log10, sqrt
import numpy as np


def fiboopti(n):
    tableau = [0 for k in range(n)]
    tableau[1] = 1
    tableau[2] = 1
    print("le blème est la ")
    for k in range(3, n):
        tableau[k] = tableau[k-1]+tableau[k-2]
    return tableau


tableau = fiboopti(500000)
print("ON EST PASSER ")


def testpandigital(n):
    Lnombre = list(str(n)).sort()

    return Lnombre == ['1', '2', '3', '4', '5', '6', '7', '8', '9']


def testpandigitalfibo(i, tableau):  # i représente l'indice de début de recherche
    for k in range(i, len(tableau)):
        if k % 10**4 == 0:
            print("on est a ", k)
        element = tableau[k]
        elementstr = str(element)
        if element > 10**18:
            debut = elementstr[:9]
            n = len(elementstr)
            fin = elementstr[n-9:n]

            if testpandigital(fin) and testpandigital(debut):
                return k
    return "PAS DE SOLUTION"


# jamais utiliser les string
# i représente l'indice de début de recherche

# fiboam ne marche pas et s'arrete!!!
def testpandigitalfiboam(i, tableau):
    for k in range(i, len(tableau)):
        if k % 10**4 == 0:
            print("on est a ", k)
        element = tableau[k]
        # ICI, On aimerait ne pas avoir à créer en caractère tous les elements et ainisi diminuer la complexité
        if element > 10**18:
            # C'était le bon point de vue pour le début
            debut = str(element % 10**9)
            exposant = floor(log10(element))
            fin = element // 10**(floor(log10(element)) + 1 - 9)

            if testpandigital(fin) and testpandigital(debut):
                return k
    return "PAS DE SOLUTION"


print("AA")
i = 200000
print(testpandigitalfiboam(i, tableau))

# VERS UNE NOUVELLE APPROCHE
fn = (1-sqrt(5))/2
# Apparement c'est lui qui est le beaucoup plus proche pour phi
phi = (1+sqrt(5))/2


def calcfibo(n):
    resultat = []
    for k in range(n):
        resultat[k] = round(phi**n/5)
    return resultat


"""
print("on test un nouveau truc")
print(calcfibo(10000))
"""
