"""
Name: Shelby Rhodes
bumper.py

Problem:

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from graphics import *

from random import randint


def main():
    width = 600
    height = 600
    win = GraphWin("Bumper", width, height)
    x = randint(0, 599)
    y = randint(0, 599)
    a = randint(0, 599)
    b = randint(0, 599)
    radius = 30
    move_amounta = randint(-15, 15)
    move_amountb = randint(-15, 15)
    move_amountc = randint(-15, 15)
    move_amountd = randint(-15, 15)
    circle1 = Circle(Point(x, y), radius)
    circle1.setOutline("red")
    circle1.setFill("red")
    circle1.draw(win)
    circle2 = Circle(Point(a, b), radius)
    circle2.setOutline("green")
    circle2.setFill("green")
    circle2.draw(win)

    while circle1.getCenter().getX() + radius < width and circle2.getCenter().getX() + radius < width:
        circle1.move(move_amounta, move_amountb)
        circle2.move(move_amountc, move_amountd)

    # while circle1.getCenter().getY() + radius < height and circle2.getCenter().getY() + radius < height:
    #     circle1.move(move_amounta, move_amountb)
    #     circle2.move(move_amountc, move_amountd)
    #
    # while circle1.getCenter().getX() + radius == width and circle2.getCenter().getX() + radius == width:
    #     circle1.move(-move_amounta, -move_amountb)
    #     circle2.move(-move_amountc, -move_amountd)
    #
    # while circle1.getCenter().getY() + radius == height and circle2.getCenter().getY() + radius == height:
    #     circle1.move(-move_amounta, -move_amountb)
    #     circle2.move(-move_amountc, -move_amountd)

    win.getMouse()
    win.close()



# def get_random(int move_amount):
#     move_amount = randint(-15, 15)
#
# def hit_verticle(Circle ball, Graphwin win):




if __name__ == "__main__":
    main()