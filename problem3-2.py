#Angel Ocampo
#November 1,2022
#This program will let user pick the shape,lenght, and color of the shape they want drawn.
print("Do you want to draw a square or triangle")
shape=input()
print("What lenght do you want on each side of the", shape, "in pixels")
lenght=int(input())
print("What color do you want the", shape, "of")
color=input()

import turtle
Tom = turtle.Turtle()
Tom.pencolor("black")

Tom.fillcolor(color)
Tom.begin_fill()

if shape == "triangle":
    for num in range(3):
        Tom.forward(lenght)
        Tom.left(120)
else:
    for num in range(4):
        Tom.forward(lenght)
        Tom.left(90)
Tom.end_fill()