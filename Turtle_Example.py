# Turtle_Example.py
# Programmer: Jon Phillips (JPhillips39@cnm.edu)
# Objective: Just me playing around with turtle

import turtle
import time



t=turtle.Turtle()

t.speed(10)

turtle.bgcolor("black")

t.color("white")

t.hideturtle()

screen_width = turtle.getcanvas().winfo_width() // 2

screen_height = turtle.getcanvas().winfo_height() // 2



# draw opening design

# draw square in center of screen
t.penup()
t.goto(0,50)
t.pendown()  
t.setheading(0)
t.forward(50)
t.setheading(270)
t.forward(100)
t.setheading(180)
t.forward(100)
t.setheading(90)
t.forward(100)
t.setheading(0)
t.forward(50)
t.penup()

# draw top circle
t.pendown()
t.circle(100)
t.penup()

# draw right circle
t.goto(50,0)
t.pendown()
t.setheading(270)
t.circle(100)
t.penup()

# draw bottom circle
t.goto(0,-50)
t.pendown()
t.setheading(180)
t.circle(100)
t.penup()

# draw left circle
t.goto(-50,0)
t.pendown()
t.setheading(90)
t.circle(100)
t.penup()

# draw outer circle
t.goto(-250,0)
t.pendown()
t.setheading(270)
t.circle(250)
t.penup()

# add outer square
t.goto(0,250)
t.pendown()
t.setheading(0)
t.forward(250)
t.setheading(270)
t.forward(500)
t.setheading(180)
t.forward(500)
t.setheading(90)
t.forward(500)
t.setheading(0)
t.forward(250)
t.penup()

# draw inner circle
t.goto(0,-50)
t.pendown()
t.circle(50)
t.penup()

# draw inner triangle
t.goto(0,50)
t.pendown()
t.setheading(300)
t.forward(86.6)
t.setheading(180)
t.forward(86.6)
t.setheading(60)
t.forward(86.6)
t.penup()

time.sleep(1)
t.goto(0,0)


#transistion into next design
t.speed(0)
t.color("black")
t.pensize(19)
for i in range(0,250,10):
    t.goto(0,i)
    t.pendown()
    t.forward(i)
    t.setheading(270)
    t.forward(i*2)
    t.setheading(180)
    t.forward(i*2)
    t.setheading(90)
    t.forward(i*2)
    t.setheading(0)
    t.forward(i)
    t.penup()


# draw square design
t.goto(0,0)
t.pensize(1)
t.color("white")

t.speed(0)
t.hideturtle()
t.penup()
for i in range(250,0,-10):
    t.goto(0,i)
    t.pendown()
    t.forward(i)
    t.setheading(270)
    t.forward(i*2)
    t.setheading(180)
    t.forward(i*2)
    t.setheading(90)
    t.forward(i*2)
    t.setheading(0)
    t.forward(i)
    t.penup()

# Transisiton to ending design

t.goto(0,0)
t.pensize(15)
t.color("black")

t.speed(0)
t.hideturtle()
t.penup()
for i in range(250,0,-10):
    t.goto(0,i)
    t.pendown()
    t.forward(i)
    t.setheading(270)
    t.forward(i*2)
    t.setheading(180)
    t.forward(i*2)
    t.setheading(90)
    t.forward(i*2)
    t.setheading(0)
    t.forward(i)
    t.penup()

    
    
# create ending design
t.goto(0,0)
t.color("red")
t.pensize(1)

t.speed(0)
t.hideturtle()

for i in range(0,250,5):
  
    t.goto(0,-i)
    t.pendown()
    t.circle(i)
    t.penup()

for i in range(0,250,5):
    t.pensize(2)
    t.color("black")
    t.pendown()
    t.circle(i)

time.sleep(1)
t.goto(0,0)
t.penup()
t.color("White")
t.goto(-180,-300)
t.write("Thank you for watching", font=("Arial", 24, "bold italic"))


turtle.done()



