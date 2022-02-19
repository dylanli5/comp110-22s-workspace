"""Describe your scene program."""

__author__ = "730401544"

from turtle import Turtle, colormode, done 
colormode(255)


def draw_square(square: Turtle, x: float, y: float, width: float) -> None:
    """Draw a square of the given width whose top-left corner is located at x, y."""
    square.penup()
    square.goto(x, y) 
    square.setheading(0.0)
    square.pendown()
    i: int = 0
    while i < 4:
        square.forward(width)
        square.right(90)
        i = i + 1
          

def draw_triangle(triangle: Turtle, x: float, y: float, lateral: float) -> None:
    """Draw a equilateral triangle of the given lateral whose top-left corner is located at x, y."""
    triangle.penup()
    triangle.goto(x, y) 
    triangle.setheading(0.0)
    triangle.pendown()
    i: int = 0
    while i < 3:
        triangle.forward(lateral)
        triangle.left(120)
        i = i + 1
     
       
def draw_rectangular(rectangula: Turtle, x: float, y: float, length: float, width: float) -> None:
    """Draw a rectangular of the given length and width whose top-left corner is located at x, y."""
    rectangula.penup()
    rectangula.goto(x, y) 
    rectangula.setheading(0.0)
    rectangula.pendown()
    """For part 7, I break up the function into two simpler parts of drawing a rectangular."""
    i: int = 0

    def rec_first(length: float) -> None:
        rectangula.forward(length)
        rectangula.right(90)

    def rec_second(width: float) -> None:
        rectangula.forward(width)
        rectangula.right(90)

    while i < 2:
        rec_first(length)
        rec_second(width)
        i = i + 1


def draw_line(line: Turtle, x: float, y: float, length: float) -> None:
    """Draw a line with certain length."""
    line.penup()
    line.goto(x, y) 
    line.setheading(0.0)
    line.pendown()
    line.forward(length)


def draw_circle(circle: Turtle, x: float, y: float, radius: float) -> None:
    """Draw a circle with certain radius."""
    """For Part 8, I used circle function to draw the doorknob on the door"""
    circle.penup()
    circle.goto(x, y) 
    circle.setheading(0.0)
    circle.pendown()
    circle.circle(radius)


def main() -> None:
    """The entrypoint of my scene."""
    square: Turtle = Turtle()
    triangle: Turtle = Turtle()
    rectangula: Turtle = Turtle()
    line: Turtle = Turtle()
    circle: Turtle = Turtle()

    triangle.color(147, 73, 35)
    triangle.begin_fill()
    draw_triangle(triangle, -250, 55, 450)
    triangle.end_fill()

    square.color(142, 127, 96)
    square.begin_fill()
    draw_square(square, -250, 55, 450)
    square.end_fill()

    square.color(0, 0, 0)
    i: int = 0
    x = -175
    while i < 2:
        draw_square(square, x, -20, 100)
        x += 200
        i += 1

    draw_rectangular(rectangula, -100, -195, 150, 200)

    count_1: int = 0
    x = -175
    while count_1 < 2:
        draw_line(line, x, -70, 100)
        x += 200
        count_1 += 1

    count_2: int = 0 
    x = -175
    line.right(90)
    while count_2 < 2:
        draw_line(line, x, -25, 100)
        x += 200
        count_2 += 1
    
    draw_circle(circle, -70, -300, 7.5)
    
    done()
    
    
if __name__ == "__main__":
    main()