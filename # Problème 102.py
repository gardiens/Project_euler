# Problème 102

def pretraitement(fichier):
    fichier = open("fi")


def trouverequaplandroite(L):
    # On se donne deux points et on cherche l'équation de la droite  correspondante, on renvoie y=ax+b avec le premier coeff c'est a et le deuxieme c'est b
    A = (x, y)
    B = (b, z)
    if x == v:
        return (0, x)
    else:

        a = (y-z)/x-v
        b = (x*z-b*y)/x-v
        return (a, b)


def memedemiplan(L, F, D):  # on accepte deux points et
    F = (x, y)
    D = (v, w)
    (a, b) = trouverequaplandroite(L)

    def f(P):
        P = (k, l)
        return ak+b-l
    return f(F)*f(D) >= 0
