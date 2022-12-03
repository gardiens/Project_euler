# problème 104
from math import sqrt
import numpy as np


def fiboopti(n):
    tableau = [0 for k in range(n)]
    tableau[1] = 1
    tableau[2] = 1
    print("le blème est la ")
    for k in range(3, n):
        tableau[k] = tableau[k-1]+tableau[k-2]
    return tableau


"""

print("test", len(str(101)))
# print("test", len("1088"))
tableau = fiboopti(500000)
print("ON EST PASSER ")
"""


def testpandigital(n):
    marqueur = [False for k in range(10)]
    marqueur[0] = True

    for x in n:

        if marqueur[int(x)]:
            return False
        else:
            marqueur[int(x)] = True
    return True


def testpandigitalfibo(i, tableau):  # i représente l'indice de début de recherche
    for k in range(i, len(tableau)):
        if k % 10**4 == 0:
            print("on est a ", k)
        element = tableau[k]
        elementstr = str(element)
        if len(elementstr) > 18:
            debut = elementstr[:9]
            n = len(elementstr)
            fin = elementstr[n-9:n]

            if testpandigital(fin) and testpandigital(debut):
                return k
    return "PAS DE SOLUTION"


"""
print("AA")
i = 100000
print(testpandigitalfibo(i, tableau))
"""
# VERS UNE NOUVELLE APPROCHE
fn = (1-sqrt(5))/2
# Apparement c'est lui qui est le beaucoup plus proche pour phi
phi = (1+sqrt(5))/2


def calcfibo(n):
    resultat = []
    for k in range(n):
        resultat[k] = round(phi**k/5)
    return resultat
