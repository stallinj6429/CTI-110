'''
Created on Oct 1, 2020

@author: jdsta
'''
#turtle Graphics

import turtle
screen = turtle.Screen()
myTurtle = turtle.Turtle()
myTurtle.color('green')
myTurtle.pencolor('red')
myTurtle.pensize(3)

for i in (1, 2, 3):
    myTurtle.forward(100)
    myTurtle._rotate(120)
    
myTurtle.pencolor('white')
myTurtle.backward(100)
myTurtle.pencolor('blue')
for i in (1, 2, 3, 4):
    myTurtle.forward(100)
    myTurtle._rotate(90)
myTurtle.pencolor('white')
myTurtle.backward(100)
myTurtle.pencolor('purple')
myTurtle.forward(100)
for i in (1, 2, 3, 4):
    myTurtle._rotate(145)
    myTurtle.forward(100)


    



screen.mainloop()