#Using the turtle program to create the black and white CSU logo
import turtle

wn=turtle.Screen()
wn.bgcolor("black")

cols=turtle.Turtle()
cols.color("white")
cols.pensize(3)
cols.speed(0)
cols.penup()
cols.setposition(0,200)
cols.pendown()
 
#cols: Outline of logo
cols.right(45)
cols.forward(80)
#half of triangle on logo
cols.left(45)
cols.forward(70)
cols.right(90)
cols.forward(50)
#box on logo

cols.left(45)

#1st hump
for semicircle in range(5):
    cols.left(30)
    cols.forward(15)
    cols.right(40)

cols.left(5)
cols.forward(200)
cols.right(45)

#lower half of outline

for halfcircle in range(16):
    cols.left(30)
    cols.forward(30)
    cols.right(40)

cols.left(25)
cols.forward(200)

#2nd hump
#Used for loop to create circular line
#Realized that if I did a for loop, I can make circular lines, had to do trial and error method 
for semicircle2 in range(5):
    cols.right(40)
    cols.forward(15)
    cols.left(30)
 
cols.left(50)
cols.forward(50)
cols.right(90)
cols.forward(60)
 
cols.left(60)
cols.forward(70)
cols.penup()
#back at starting point
 
#Used cols to make outline for CSU logo

#tower: Creating the clock tower 
tower=turtle.Turtle()
tower.color("white")

tower.penup()
tower.setposition(10,180)
tower.right(90)
tower.forward(10)
tower.pendown()

#Getting tower into position under the outline

tower.begin_fill()
tower.left(45)
tower.forward(50)
tower.right(45)
tower.forward(100)
tower.left(90)
tower.forward(40)
tower.right(90)
tower.forward(5)
tower.right(90)

tower.forward(150)

tower.right(90)
tower.forward(5)
tower.right(90)
tower.forward(40)
tower.left(90)
tower.forward(100)
tower.right(45)
tower.forward(50)
tower.left(45)
tower.end_fill()

clock=turtle.Turtle()
clock.penup()
clock.goto(10,100)
clock.pendown()
clock.pensize(3)
clock.circle(20)
clock.penup()
clock.goto(10,120)
clock.pendown()
clock.forward(9)
clock.forward(-9)
clock.left(90)
clock.forward(9)
clock.forward(-9)
clock.penup()
clock.goto(100,100)

body=turtle.Turtle()
#Getting body of clock tower into position
body.color("white")
body.penup()
body.setposition(-63,20)
body.pendown()

body.begin_fill()
body.forward(150)
body.right(90)
body.forward(120)
body.right(90)
body.goto(-63,-150)
body.right(90)
body.forward(170)
body.pendown()
body.end_fill()
#body below clock tower is filled in

#line that goes through clock tower
line=turtle.Turtle()
line.pensize(10)
line.color("black")
line.penup()
line.goto(-55,20)
line.setheading(270)
line.pendown()
line.forward(200)

#the 4 lines used in the clock tower
body.penup()
body.color("black")
body.shape("square")
body.pensize(5)

body.right(90)
body.forward(50)
body.right(90)
body.forward(10)
body.pendown()
body.forward(70)

body.penup()
body.left(90)
body.forward(15)

body.pendown()
body.left(90)
body.forward(70)

body.penup()
body.right(90)
body.forward(15)
body.pendown()
body.right(90)
body.forward(70)

body.penup()
body.left(90)
body.forward(15)
body.pendown()
body.left(90)
body.forward(70)
body.penup()
body.goto(100,100)




river=turtle.Turtle()
river.color("white")
river.penup()
#using river turtle to make river under the clocktower
river.goto(183,-75)
river.setheading(180)
river.pendown()
river.pensize(4)
river.begin_fill()
#Used for loops for curves 
for curve1 in range(5):
    river.right(5)
    river.forward(6)
    river.left(10)
for bend1 in range(5):
    river.left(15)
    river.forward(2)
    river.right(10)
for curve2 in range(64):
    river.right(6)
    river.forward(5)
    river.left(5)
river.setheading(270)
river.circle(120,90)
for curve3 in range(47):
    river.right(-6)
    river.forward(5)
    river.left(-5)
for bend2 in range(6):
    river.left(-15)
    river.forward(2)
    river.right(-10)
river.goto(183,-75)
river.end_fill()
river.pendown()

turtle.exitonclick()


