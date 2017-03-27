"""
    Creates a box and whisker plot in turtle based on the 5 key values givne by the user
    author: Aidan Rubenstein
"""
from wordData import *
import turtle

def boxAndWhisker(small, q1, med, q3, large):
    """
        Uses the 5 data points to construct the diagram in turtle, with the lengths between each of the boxes
        indicating differnces between the 5 points. Variables height and ends are used to scale the turtle's height
        of the boxes and height of the end caps.
        precondition: all 5 data points are given by user
        postcondition: turtle draws the box and whisker plot at its highest speed
    """
    turtle.speed(10)
    height = 75
    ends = 25
    turtle.left(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward((q3-med)*10)
    turtle.right(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward((large-q3)*10)
    turtle.left(90)
    turtle.forward(ends)
    turtle.forward(-(2*ends))
    turtle.forward(ends)
    turtle.left(90)
    turtle.forward((large-q3)*10)
    turtle.left(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward((q3-med)*10)
    turtle.right(90)
    turtle.forward(height)
    turtle.forward(-height)
    turtle.left(90)
    turtle.forward((med-q1)*10)
    turtle.right(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward((q1-small)*10)
    turtle.left(90)
    turtle.forward(ends)
    turtle.forward(-(2*ends))
    turtle.forward(ends)
    turtle.left(90)
    turtle.forward((q1-small)*10)
    turtle.left(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward((med-q1)*10)
    turtle.hideturtle()
    turtle.done()


def main():
    small = int(input("Enter the minimum: "))
    q1 = int(input("Enter the first quartile: "))
    med = int(input("Enter the median: "))
    q3 = int(input("Enter the third quartile: "))
    large = int(input("Enter the maximum: "))
    boxAndWhisker(small, q1, med, q3, large)

if __name__ == '__main__':
    main()