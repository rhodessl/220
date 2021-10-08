"""
Name: Shelby Rhodes
greeting.py

Problem: This program displays a greeting

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from graphics import GraphWin, Circle, Point, Polygon, Text, Line

def main():
    width = 500
    height = 500
    win = GraphWin("Greeting", width, height)
    win.setBackground("pink")


    shape = Circle(Point(200, height/3), 50)
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    triangle = Polygon(Point(150, 178), Point(250, 300), Point(350, 178))
    triangle.setOutline("red")
    triangle.setFill("red")
    triangle.draw(win)

    arrow = Line(Point(-50, 550), Point(0, 500))
    arrow.setArrow("last")
    arrow.draw(win)
    arrow.setWidth(10)

    shape = Circle(Point(300, height / 3), 50)
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)


    greeting_pt = Point(width / 2, height / 8)
    greeting_txt = Text(greeting_pt, "Happy Valentine's Day!")
    greeting_txt.setTextColor("white")
    greeting_txt.setSize(30)
    greeting_txt.draw(win)


    for _ in range(550):
        arrow.move(1, -1)

    inst_pt = Point(width/2, 400)
    inst_txt = Text(inst_pt, "Click to close")
    inst_txt.setTextColor("white")
    inst_txt.setSize(20)
    inst_txt.draw(win)

    win.getMouse()
    win.close()

if __name__ == "__main__":
    main()
