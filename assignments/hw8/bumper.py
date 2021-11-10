"""
Name: Shelby Rhodes
bumper.py

Problem:

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from graphics import *

from random import randint
from time import sleep
import math


def main():
    width = 600
    height = 600
    win = GraphWin("Bumper", width, height)
    x = randint(0, 599)
    y = randint(0, 599)
    a = randint(0, 599)
    b = randint(0, 599)
    radius = 30
    move_amounta = get_random(15)
    move_amountb = get_random(15)
    move_amountc = get_random(15)
    move_amountd = get_random(15)
    circle1 = Circle(Point(x, y), radius)
    circle1.setFill(get_random_color())
    circle1.draw(win)
    circle2 = Circle(Point(a, b), radius)
    circle2.setFill(get_random_color())
    circle2.draw(win)

    while True:
        circle1.move(move_amounta, move_amountb)
        circle2.move(move_amountc, move_amountd)

        # bounce off of vertical wall
        if hit_vertical(circle1, win):
            move_amounta = -1 * move_amounta
        if hit_vertical(circle2, win):
            move_amountc = -1 * move_amountc

        # bounce off of horizontal wall
        if hit_horizontal(circle1, win):
            move_amountb = -1 * move_amountb
        if hit_horizontal(circle2, win):
            move_amountd = -1 * move_amountd

        if did_collide(circle1, circle2):
            move_amounta = -1 * move_amounta
            move_amountb = -1 * move_amountb
            move_amountc = -1 * move_amountc
            move_amountd = -1 * move_amountd

        sleep(0.1)

    win.getMouse()
    win.close()


def get_random(move_amount):
    return randint(-move_amount, move_amount)


def did_collide(circle1, circle2):
    x1 = circle1.getCenter().getX()
    y1 = circle1.getCenter().getY()
    x2 = circle2.getCenter().getX()
    y2 = circle2.getCenter().getY()
    distance = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
    radius = 30
    return distance <= radius + radius


def hit_vertical(circle, win):
    width = win.getWidth()
    return circle.getCenter().getX() + circle.getRadius() >= width or circle.getCenter().getX() - circle.getRadius() <= 0


def hit_horizontal(circle, win):
    height = win.getHeight()
    return circle.getCenter().getY() + circle.getRadius() >= height or circle.getCenter().getY() - circle.getRadius() <=0


def get_random_color():
    color = color_rgb(randint(0, 255), randint(0, 255), randint(0, 255))
    return color


if __name__ == "__main__":
    main()