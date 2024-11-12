# Landon Graessle
# 29 October 2024
# P4LAB1
# Use loops and turtle library to draw a house

import turtle
window = turtle.Screen()
t = turtle.Turtle()

t.pensize(5)
t.pencolor("orange")
t.shape("arrow")

movement = 0

while movement <= 3:
    movement += 1
    t.forward(100)
    t.right(90)

t.left(60)
t.pencolor("red")

movement = 0

for movement in range(3):
    t.forward(100)
    t.right(120)
