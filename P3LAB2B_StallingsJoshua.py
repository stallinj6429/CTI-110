'''
Created on Oct 1, 2020

@author: jdsta
'''
import turtle
screen = turtle.Screen()
myTurtle = turtle.Turtle()
screen.title('Initials')
myTurtle.color('green')
myTurtle.fillcolor('red')
myTurtle.pencolor('black')
myTurtle.pensize(4)
myTurtle._rotate(-90)
myTurtle.forward(50)
myTurtle._rotate(90)
myTurtle.forward(50)
myTurtle._rotate(90)
myTurtle.forward(150)
myTurtle._rotate(90)
myTurtle.forward(75)
myTurtle._rotate(180)
myTurtle.forward(150)
myTurtle._rotate(-90)
myTurtle.penup()
myTurtle.forward(149)
myTurtle.pendown()
myTurtle.forward(1)
myTurtle._rotate(90)
myTurtle.penup()
myTurtle.forward(100)
myTurtle.pendown()
myTurtle.forward(75)
myTurtle._rotate(90)
myTurtle.forward(75)
myTurtle._rotate(90)
myTurtle.forward(75)
myTurtle._rotate(-90)
myTurtle.forward(75)
myTurtle._rotate(-90)
myTurtle.forward(75)


screen.mainloop() 