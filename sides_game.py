from turtle import *
import math
t=Turtle()

t.speed(0)
colors=['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'silver', 'gold']

#Create black backround
t.color("black")
t.hideturtle()
t.begin_fill()
t.hideturtle()
bgcolor("black")
t.end_fill()
t.goto(0,0)

# Ask how many sides the user wants
number_of_sides = int(input("How many sides would you like your shape to have? (1-9) "))

if number_of_sides > 9:
  print("Please enter a number from 1-9.")
  number_of_sides = int(input("How many sides would you like your shape to have? (1-9) "))
  #(JIM) How do I make the user able to input the number of sides they want?

# Draw a spiral with the number of sides the user chose on the screen 200 times
for x in range(200):
  t.pencolor(colors[x % number_of_sides])
  t.forward(x*3/number_of_sides+x)
  t.left(360/number_of_sides+1)


