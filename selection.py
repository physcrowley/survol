from turtle import *

wn = Screen()
wn.setup(600, 400, 125, 125)
wn.title("Sélection de couleurs")

def colorize(x,y):
    """Changer la couleur de fond en fonction de la position du clic"""
    
    # structure de sélection
    if x < -(wn.window_width()/6):
        wn.bgcolor("red")
    elif x < wn.window_width()/6:
        wn.bgcolor("green")
    else:
        wn.bgcolor("blue")

    # TODO ajouter des couleurs et des zones de sélection

wn.onclick(colorize) # utilise colorize à chaque clic dans la fenêtre

# dessiner le contexte
penup()
goto(0,175)
write("Cliquez dans la fenêtre pour changer la couleur de fond", \
      align="center", font=("Arial", 16, "normal"))
setx(-wn.window_width()/6)
pendown()
sety(-200)
penup()
setx(wn.window_width()/6)
pendown()
sety(175)
penup()
hideturtle()



wn.mainloop()