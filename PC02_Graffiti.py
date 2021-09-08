#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: Nita Byati
May 29, 2020
'''

import turtle #import the library of commands that you'd like to use

turtle.colormode(255)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif" 

panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======
turtle.up()
turtle.goto(-15,110)
turtle.down()
turtle.pensize(10)
turtle.color("red")
turtle.right(16)
turtle.left(30)
turtle.up()
turtle.goto(-15,112)
turtle.down() 
turtle.pensize(7)
turtle.right(17)
turtle.forward(250)
turtle.up()
turtle.goto(46,121)
turtle.right(20)
turtle.left(21)
turtle.down()
turtle.forward(250)
turtle.up()
turtle.color('gold')
turtle.fillcolor("gold")
turtle.width(5)
turtle.goto(50,-90)
turtle.left(180)
turtle.right(90)
turtle.begin_fill()
turtle.down()
turtle.forward(20)
turtle.right(90)
turtle.forward(11)
turtle.right(90)
turtle.forward(20)
turtle.right(90)
turtle.forward(11)
turtle.end_fill()
turtle.up()
turtle.right(180)
turtle.forward(5)
turtle.left(90)
turtle.forward(10)
turtle.down()
turtle.color('turquoise1')
turtle.fillcolor('turquoise1')
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()

turtle.done()

#=======Clean up code (do not change)======
# this code ensures that your script runs correctly each time.
#turtle.done()
