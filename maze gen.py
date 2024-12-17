# Créé par MULLER, le 09/09/2024 en Python 3.7

import random
import turtle

def affiche(grid):
    """ """
    for element in grid:
        print(element)

def start(grid):
    if random.randint(1,2) == 1:
        x_start = random.randint(0,9)
        y_start = 0
    else:
        x_start = 0
        y_start = random.randint(0,9)
    used.append((x_start,y_start))
    return x_start,y_start

def can_use(used):
    usable = []
    for element in used:
        if up(grid,element)[0] or down(grid,element)[0] or right(grid,element)[0] or left(grid,element)[0]:
            usable.append(element)
    return usable

def direction(grid,current,directions):


    if len(directions) == 0 :

        current = random.choice(can_use(used))
        direction(grid, current, ["up","down","right","left"])

    else :

        select = random.choice(directions)

        if select == "up" :
            if up(grid,current)[0]:

                used.append(up(grid,current)[1])
                paths_vert.append((current,(current[0],up(grid,current)[1][1])))
                current = up(grid,current)[1]
                directions = ["up","down","right","left"]

            else:
                del directions[directions.index("up")]
                direction(grid, current, directions)

        elif select == "down" :
            if down(grid,current)[0]:

                used.append(down(grid,current)[1])
                paths_vert.append((current,(current[0],down(grid,current)[1][1])))
                current = down(grid,current)[1]
                directions = ["up","down","right","left"]

            else:
                del directions[directions.index("down")]
                direction(grid, current, directions)

        elif select == "right" :
            if right(grid,current)[0]:

                used.append(right(grid,current)[1])
                paths_hor.append((current,(right(grid,current)[1][0],current[1])))
                current = right(grid,current)[1]
                directions = ["up","down","right","left"]

            else:
                del directions[directions.index("right")]
                direction(grid, current, directions)

        elif select == "left" :
            if left(grid,current)[0]:

                used.append(left(grid,current)[1])
                paths_hor.append((current,(left(grid,current)[1][0],current[1])))
                current = left(grid,current)[1]
                directions = ["up","down","right","left"]

            else:
                del directions[directions.index("left")]
                direction(grid, current, directions)





def up(grid,current):
    test = current[0],current[1]-1
    return (current[1] != 0 and test not in used,test)

def down(grid,current):
    test = current[0],current[1]+1
    return (current[1] != len(grid)-1 and test not in used,test)

def right(grid,current):
    test = current[0]+1,current[1]
    return (current[0] != len(grid[0])-1 and test not in used,test)

def left(grid,current):
    test = current[0]-1,current[1]
    return (current[0] != 0 and test not in used,test)



def path_gen(grid,current):

    while len(used) < colonnes * lignes:

        direction(grid, current, directions)

def tri_vert(l):

    if type(l) != list:
        return None
    n = len(l)

    for i in range(0,n-2):

        ind_min = i

        for j in range(i+1,n-1):

            if l[j][0] < l[ind_min][0]:
                ind_min=j

        if ind_min != i :

            transition = l[i]
            l[i] = l[ind_min]
            l[ind_min] = transition

def tri_hor(l):

    if type(l) != list:
        return None
    n = len(l)

    for i in range(0,n-2):

        ind_min = i

        for j in range(i+1,n-1):

            if l[j][0][1] < l[ind_min][0][1]:
                ind_min=j

        if ind_min != i :

            transition = l[i]
            l[i] = l[ind_min]
            l[ind_min] = transition

def draw_paths():

    turtle.goto(-450,-390)
    turtle.clear()
    turtle.circle(5)
    for element in paths_vert:
        turtle.penup()
        turtle.goto(element[0][0]*20-450,element[0][1]*20-390)
        turtle.pendown()
        turtle.goto(element[1][0]*20-450,element[1][1]*20-390)

    for element in paths_hor:
        turtle.penup()
        turtle.goto(element[0][0]*20-450,element[0][1]*20-390)
        turtle.pendown()
        turtle.goto(element[1][0]*20-450,element[1][1]*20-390)



directions = ["up","down","right","left"]
used = []
paths_hor = []
paths_vert = []
colonnes = int(input("Longueur du labyrinthe \n"))
lignes = int(input("Largeur du labyrinthe\n"))
grid = [[0 for j in range(colonnes)] for i in range(lignes)]





current = start(grid)
direction(grid, current, directions)
print(path_gen(grid, current))
tri_hor(paths_hor)
tri_vert(paths_vert)



turtle.speed(10)
draw_paths()
turtle.hideturtle()

