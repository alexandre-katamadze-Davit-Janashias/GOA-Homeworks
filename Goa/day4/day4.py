from turtle import *


#we want to paint a house

#step 1:  draw a square
speed(30)
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

forward(70)
color("yellow")
left(90)
forward(120)   #height of the door
right(90)
forward(60)
right(90)
forward(120)

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(200, 0)
pendown()

color("white")
left(120)
forward(50)


#we want to paint a house

#step 1:  draw a square
speed(30)
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

forward(70)
color("yellow")
left(90)
forward(120)   #height of the door
right(90)
forward(60)
right(90)
forward(120)

penup()
goto(450, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()


penup()
goto(-250, 0)
pendown()

color("white")
left(120)


#we want to paint a house

#step 1:  draw a square
speed(30)
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

forward(70)
color("yellow")
left(90)
forward(120)   #height of the door
right(90)
forward(60)
right(90)
forward(120)

penup()
goto(-50, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(-450,200)
pendown()


color("yellow")
begin_fill()
left(120)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
end_fill()

penup()
goto(-600,-5)
pendown()

color("green")
begin_fill()
forward(1050)
right(90)
forward(500)
right(90)
forward(1050)
right(90)
forward(500)
end_fill()

penup()
goto(-500,200)
pendown()

color("cyan")
begin_fill()
forward(10)
left(90)
forward(10)
left(90)
forward(10)
left(90)
forward(10)
end_fill()

penup()
goto(-300,200)
pendown()

color("cyan")
begin_fill()
forward(10)
left(90)
forward(10)
left(90)
forward(10)
left(90)
forward(10)
end_fill()

penup()
goto(-20,200)
pendown()

color("cyan")
begin_fill()
forward(10)
left(90)
forward(10)
left(90)
forward(10)
left(90)
forward(10)
end_fill()


penup()
goto(220,200)
pendown()

color("cyan")
begin_fill()
forward(10)
left(90)
forward(10)
left(90)
forward(10)
left(90)
forward(10)
end_fill()

exitonclick()