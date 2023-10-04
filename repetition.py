from turtle import *

setup(600, 400, 150, 150)
title("Répétition de mouvements")
bgcolor("lightgrey")

sides = 3 # nombre de côtés du polygone
length = window_height()/sides # longueur des côtés du polygone
color("blue")

def draw_shape():
    """Utiliser une boucle pour dessiner un polygone"""
    
    count = 1 # compteur de côtés dessinés
    # structure de répétition (boucle)
    while count <= sides:
        forward(length)
        left(360/sides)
        count = count + 1
    
    right(360/sides)


## TODO changer le nombre de côtés du polygone et observer le résultat

# utiliser la fonction draw_shape une fois
draw_shape()

## TODO utiliser la boucle pour utiliser draw_shape plusieurs fois

num = 100 # à modifier
while num < sides :
    pass # à remplacer avec votre code

    

    


mainloop()