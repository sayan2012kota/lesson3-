import pgzrun
from random import randint

HEIGHT = 1200
WIDTH = 1200

def draw():
    width=600
    height= 500

    rect=Rect((10,20) , (width , height))
    screen.draw.rect( rect , (200,20,100))

pgzrun.go()