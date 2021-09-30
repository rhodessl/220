"""
Name: Shelby Rhodes
lab5.py
"""

from graphics import *
import math


def triangle():
    win_width = 500
    win_height = 500
    win = GraphWin("Draw a Triangle", win_width, win_height)

    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)

    x1 = p1.getX()
    x2 = p2.getX()
    x3 = p3.getX()
    y1 = p1.getY()
    y2 = p2.getY()
    y3 = p3.getY()

    triangle = Polygon(p1, p2, p3)
    triangle.draw(win)

    dx1 = x2 - x1
    dx2 = x1 - x3
    dx3 = x3 - x2
    dy1 = y2 - y1
    dy2 = y1 - y3
    dy3 = y3 - y2
    a = math.sqrt(dx1 ** 2 + dy1 ** 2)
    b = math.sqrt(dx2 ** 2 + dy2 ** 2)
    c = math.sqrt(dx3 ** 2 + dy3 ** 2)

    perimeter = a + b + c
    s = perimeter / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    area_txt = Text(Point(50, 20), "The area is " + str(area))
    perimeter_txt = Text(Point(70, 30), "The perimeter is " + str(perimeter))
    area_txt.draw(win)
    perimeter_txt.draw(win)


    # Add code here to accept the mouse clicks, draw the triangle.
    # and display its area in the graphics window.

    # Wait for another click to exit
    win.getMouse()
    win.close()


def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")

    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)

    red_box = Entry(Point(win_width / 2, win_height / 2 + 40), 5)
    green_box = Entry(Point(win_width / 2, win_height / 2 + 70), 5)
    blue_box = Entry(Point(win_width / 2, win_height / 2 + 100), 5)
    red_box.draw(win)
    green_box.draw(win)
    blue_box.draw(win)

    for _ in range(5):
        win.getMouse()
        red = int(red_box.getText())
        green = int(green_box.getText())
        blue = int(blue_box.getText())
        color = color_rgb(red, green, blue)
        shape.setFill(color)

    inst.undraw()
    inst.setText("Click to close")
    inst.draw(win)
    # Wait for another click to exit
    win.getMouse()
    win.close()

def process_string():
    s = input("Enter a string ")
    print(s[0])
    print(s[-1])
    print(s[2:6])
    print(s[0] + s[-1])
    print(s[:3] * 10)
    for i in range(len(s)):
        print(s[i])
    print(len(s))

def process_list():
    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]
    x = values[1] + values[3]
    print(x)
    x =(values[0] + values[2])
    print(x)
    x = values[1] * 5
    print(x)
    x = values[2:5]
    print(x)
    x = values[2:4] + [values[0]]
    print(x)
    x = [values[2], values[0], float(values[5])]
    print(x)
    x = values[0] + values[2] + float(values[5])
    print(x)
    x = len(values)
    print(x)

def another_series():
    n = eval(input("What is the number of terms "))
    acc = 0
    for i in range(n):
        y = 2 + 2 * (i % 3)
        print(y, end=" ")
        acc = acc + y
    print()
    print("Sum =", acc)



def main():
    triangle()
    color_shape()
    process_string()
    process_list()
    another_series()
    pass


main()
