import turtle
from random import *
turtle.colormode(255)
tommy = turtle.Turtle()
tommy.pensize(3)
turtle.speed(0)
turtle.tracer(100)
tommy.hideturtle()

def koch(sideLength, level):
  if level > 0:
    for angle in [60, -120, 60, 0]:
      koch(sideLength/3, level-1) #replace this with a recursive call to koch
      tommy.left(angle)
  else:
       tommy.forward(sideLength)

def invKoch(sideLength, level):
  if level > 0:
    for angle in [60, -120, 60, 0]:
      tommy.color(randint(0,255),randint(0,255),randint(0,255))
      koch(sideLength/4, level-1) #replace this with a recursive call to koch
      tommy.left(angle)
  else:
       tommy.forward(sideLength)

def snowflake(sideLength, level):
  for i in range(3):# loop 3 times
    koch(sideLength, level) # call koch to make one side with the given sideLength and level
    tommy.right(120) # turn tommy to the right by 120 degrees

def invFlake(sideLength, level):
  for i in range(3):
    invKoch(sideLength, level) 
    tommy.right(-120)

tommy.begin_fill()
snowflake(300,4)
tommy.end_fill()
tommy.penup()
tommy.goto((35+40)/2, -150)
tommy.pendown()
invFlake(300,4)
tommy.right(90)
turtle.update()
