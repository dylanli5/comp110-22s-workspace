from turtle import Turtle, colormode, done
leo: Turtle = Turtle()
colormode(255)

# leo.forward(50)
# leo.right(90)
# leo.forward(50)
# leo.right(90)
# leo.forward(50)
# leo.right(90)
# leo.forward(50)
# leo.right(90) 

# done()

# i: int = 0
# while (i < 4):
#     leo.forward(50)
#     leo.left(90)
#     i += 1
# leo.penup()
# leo.goto(45, 60)
# leo.pendown()


leo.penup()
leo.color(99, 204, 250)
leo.goto(-120, -60)
leo.pendown()

leo.begin_fill()
i: int = 0
while (i < 3):
    leo.forward(400)
    leo.left(120)
    i += 1
leo.end_fill()

leo.speed(50)
leo.hideturtle()

bob: Turtle = Turtle()

bob.penup()
bob.color(0, 0, 0)
bob.goto(-120, -60)
bob.pendown()

bob.speed(100)
bob.hideturtle()


# bob.begin_fill()
# i: int = 0
# while (i < 3):
#     bob.forward(300)
#     bob.left(120)
#     i += 1
# bob.end_fill()

side_length: float = 400

bob.begin_fill()
i: int = 0
while (i < 3):
    bob.forward(side_length)
    bob.left(122)
    side_length = side_length * 0.5
    i += 1
bob.end_fill()

done()