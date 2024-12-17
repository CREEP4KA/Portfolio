# -*- coding: utf-8 -*-

from random import *

def voisinage(n, ligne, colonne):
    
    """ Renvoie la liste des coordonnées des voisins de la case
    (ligne, colonne) en gérant les cases sur les bords. """
    
    voisins = []
    for l in range(max(0,ligne-1), min(n, ligne+2)):
        for c in range(max(0, colonne-1), min(n, colonne+2)):
            if (l, c) != (ligne, colonne):
                voisins.append((l,c))
    return voisins


def incremente_voisins(n, grille, ligne, colonne):
    """ Incrémente de 1 toutes les cases voisines d'une bombe."""
    voisins = voisinage(n, ligne, colonne)
    for l, c in voisins:
        if grille[l][c] != -1:          # si ce n'est pas une bombe
            grille[l][c] += 1           # on ajoute 1 à sa valeur
                                
def genere_grille(bombes):
    
    """ Renvoie une grille de démineur de taille nxn où n est
    le nombre de bombes, en plaçant les bombes à l'aide de
    la liste bombes de coordonnées (tuples) passée en
    paramètre. """
    
    n = bombes
    
    # Initialisation d'une grille nxn remplie de 0
    
    grille = [[0 for colonne in range(n)] for ligne in range(n)]
    
    # Place les bombes et calcule les valeurs des autres cases
    
    
    for loop in range(n):
        pass
    i = 0
    while i < n:
        
        selector_l = randint(0,n-1)
        selector_c = randint(0,n-1)
        
        if grille[selector_l][selector_c] == 0:
            grille[selector_l][selector_c] = -1
            i += 1
            incremente_voisins(n, grille, selector_l, selector_c) # incrémente ses voisins


        
    return grille
    
