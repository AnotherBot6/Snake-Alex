"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""
import random
import time
from random import randrange
from turtle import *
import random

from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
foodAim = vector(0,-10)

def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def changeFood():
    """Change food direction."""
    foodAim.y = randrange(-10,10,10)
    foodAim.x = randrange(-10,10,10) 


def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        print('Game Over :(')
        return

    snake.append(head)

    if inside(food):
        changeFood()
        food.move(foodAim)

    elif (food.x <= -180 or food.x >= 180): 
        food.move(vector(food.x*-1,food.y))  
    elif (food.y <= -180 or food.y >= 180): 
        food.move(vector(food.x,food.y*-1))


    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()
        
    for body in snake:
        square(body.x, body.y, 9, colors[num_aleatorio])    # se cambia el color deacuerdo con el numero random obtenido

    square(food.x, food.y, 9, colors[num_aleatorio_dos])    # se cambia el color deacuerdo con el numero random obtenido
    update()
    ontimer(move, 100)


colors = ['black','yellow','green','blue','magenta']  #creo un array de 5 colores
num_aleatorio = random.randint(0, 4)        #funcion random para elegir un color del array de colors
num_aleatorio_dos = random.randint(0, 4)
while num_aleatorio ==num_aleatorio_dos :       #se verifica que no se repitan colores 
    num_aleatorio_dos = random.randint(0, 4)
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
random.seed(time.time())
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
#test
