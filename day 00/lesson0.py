from turtle import *


#we want to paint a house
speed(20)
width(7)
color("turquoise")
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
begin_fill()
forward(70)
color("light green")
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()


penup()
goto(200, 200)
pendown()

color("turquoise")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
begin_fill()
left(30)
forward(60)
left(90)
color("red")
forward(60)
left(90)
forward(60)

end_fill()

penup()
goto(200, 140)
pendown()
begin_fill()

left(90)
forward(60)
right(90)
forward(60)
end_fill()






exitonclick()





