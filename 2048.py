"""
JEU 2048

lancer une partie

générer grille 5*5

afficher le High score et le score actuel

afficher un bouton reset
    si cliqué effacer les valeurs de toutes les cases
    mettre le score à 0
    générer 2 cases d'une valeur de 2 ou 4

générer 2 cases d'une valeur de 2 ou 4

si une touche flèche directionelle est pressée
    enregistrer les valeurs de chaque case
    si la case à droite est vide se déplacer dans le sens demandé:
    si il y a une case de valeur différente bloquer
    si il y a un mur bloquer
    si il y a une case de la même valeur fusionner et ajouter au score la valeur créée
    vérifier si les valeurs de chaque case ont changé
        si aucune n'a changé game over
    vérifier si une case atteint la valeur de 2048
        finir le jeu

si le score est plus grand que le high score, remplacer

afficher un bouton rejouer

"""
#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import time
from pynput import keyboard
import random



def roundstart()->list:

    xgrid=random.randint(0,4)
    ygrid=random.randint(0,4)

    empty_positions = [(i, j) for i in range(5) for j in range(5) if grid[i][j] == 0]

    if not not empty_positions:

        while grid[xgrid][ygrid] != 0:
            xgrid=random.randint(0,4)
            ygrid=random.randint(0,4)

        grid[xgrid][ygrid]=random.choice(genbox)

    print(not not empty_positions)
    return grid

    """
    la fonction modifie la liste "grid" en y ajoutant
    2 valeurs choisies dans la liste "genbox" si il
    reste des emplacements libres et renvoie la liste modifiée
    """


def left():
    for loop in range(4):
        for i in range(5):
            for j in range(1, 5):
                if grid[i][j] != 0 and grid[i][j - 1] == grid[i][j]:
                    grid[i][j - 1] = grid[i][j]*2
                    grid[i][j]=0

                elif grid[i][j] != 0 and grid[i][j - 1]==0:
                    grid[i][j - 1] = grid[i][j]
                    grid[i][j]=0

    """
    la fonction déplace toutes les valeurs vers la
    gauche quand la flèche directionnelle correspondante est pressée
    """

def right():
    for loop in range(4):
        for i in range(5):
            for j in range(0, 4):
                if grid[i][j] != 0 and grid[i][j + 1] == grid[i][j]:
                    grid[i][j + 1] = grid[i][j]*2
                    grid[i][j]=0

                elif grid[i][j] != 0 and grid[i][j + 1]==0:
                    grid[i][j + 1] = grid[i][j]
                    grid[i][j]=0

    """
    la fonction déplace toutes les valeurs vers la
    droite quand la flèche directionnelle correspondante est pressée
    """

def up():
    for loop in range(4):
        for i in range(1,5):
            for j in range(5):
                if grid[i][j] != 0 and grid[i-1][j] == grid[i][j]:
                    grid[i-1][j] = grid[i][j]*2
                    grid[i][j]=0

                elif grid[i][j] != 0 and grid[i-1][j]==0:
                    grid[i-1][j] = grid[i][j]
                    grid[i][j]=0

    """
    la fonction déplace toutes les valeurs vers le
    haut quand la flèche directionnelle correspondante est pressée
    """

def down():
    for loop in range(4):
        for i in range(0,4):
            for j in range(5):
                if grid[i][j] != 0 and grid[i+1][j] == grid[i][j]:
                    grid[i+1][j] = grid[i][j]*2
                    grid[i][j]=0

                elif grid[i][j] != 0 and grid[i+1][j]==0:
                    grid[i+1][j] = grid[i][j]
                    grid[i][j]=0

    """
    la fonction déplace toutes les valeurs vers le
    bas quand la flèche directionnelle correspondante est pressée
    """

def on_press(key:input)->bool:

    if key == keyboard.Key.left:
        left()
    elif key == keyboard.Key.right:
        right()
    elif key == keyboard.Key.up:
        up()
    elif key == keyboard.Key.down:
        down()
    return False

    """
    détecte les inputs et exécute les fonctions correspondantes
    à l'aide du module pynput
    """

def on_release(key:input)->bool:

    if key == keyboard.Key.esc:

        return False

    return False
    """
    la fonction évite de détecter plusieurs inputs pour une seule pression
    """

def end_check(checker:bool)->bool:

    empty_positions = [(i, j) for i in range(5) for j in range(5) if grid[i][j] == 0]

    if len(empty_positions)==0:
        checker = True

        for j in range(5):
            for i in range(4):
                if grid[i+1][j] != grid[i][j]:
                    pass
                else :
                    checker = False

        for j in range(4):
            for i in range(5):
                if grid[i][j+1] != grid[i][j]:

                    pass
                else:
                    checker = False

    return checker

    """
    la fonction vérifie si le joueur a encore un coup légal à jouer
    et renvoie True si le jeu est fini
    """


def win(winner:bool)->bool:
    winner = False

    for j in range(5):
        for i in range(5):

            if grid[i][j]==2048:
                winner= True
                break

    return winner
    """
    la fonction vérifie si le joueur a atteint la valeur 2048
    et renvoie True si le jeu est fini
    """
genbox=[2,2,2,2,2,2,2,2,2,4]
score=0
grid=[[0 for j in range(5)] for i in range(5)]


checker = False
winner = False


roundstart()

while win(winner)== False and end_check(checker) == False :

    for loop in range(5):
        print('')

    print(grid[0])
    print(grid[1])
    print(grid[2])
    print(grid[3])
    print(grid[4])


    with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
        listener.join()

    listener = keyboard.Listener(
        on_press=on_press,
        on_release=on_release)
    listener.start()

    time.sleep(0)
    roundstart()

    win(winner)
    end_check(checker)



for loop in range(5):
    print('')

print(grid[0])
print(grid[1])
print(grid[2])
print(grid[3])
print(grid[4])

listener.stop()

if win(winner)==True:
    print("YOU WIN")

elif end_check(checker)== True:
    print("YOU LOSE")


print("END OF THE GAME")



















#test interface graphique
"""


score=1111

from tkinter import *
import random
fenetre= Tk()
fenetre.title("2048")
fenetre.config(bg= "#e6e6e6")
fenetre.geometry("800x700")
fenetre.minsize(400,350)
fenetre.maxsize(1000,875)
fenetre.anchor("nw")

textetitre= Label(fenetre,anchor="n",bg="#e6e6e6",fg="#5d5d5d",text="--<><>--<><>--<><>--<><>--<><>--<><>--JEU DU 2048--<><>--<><>--<><>--<><>--<><>--<><>--\n=====================================================================================",font=("Impact", 30))
textetitre.pack(anchor="w")
scoreui= Label(fenetre,bg="#e6e6e6",fg="#5d5d5d",text="Score :",font=("Impact", 20))
scoreui.pack(anchor="w")
highscoreui= Label(fenetre,bg="#e6e6e6",fg="#5d5d5d",text="Highscore :" ,font=("Impact", 20))
highscoreui.pack(anchor="w")



fenetre.mainloop()


"""
