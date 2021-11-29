"""
Name: Shelby Rhodes
threeDoorGame.py

Problem: this program plays a door game

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import *
from Button import Button

def main():
    width = 400
    height = 400
    win = GraphWin("Three Button Game", width, height)

    x = 30
    y = 200

    p1 = Point(x, y)
    p2 = Point(x+70, y+50)
    p3 = Point(165, y)
    p4 = Point(235, y+50)
    p5 = Point(300, y)
    p6 = Point(370, y+50)

    button1 = Button(Rectangle(p1, p2), "Door1")
    button1.draw(win)
    button2 = Button(Rectangle(p3, p4), "Door2")
    button2.draw(win)
    button3 = Button(Rectangle(p5, p6), "Door3")
    button3.draw(win)

    top_text = Text(Point(width/2, height/4), "I have a secret door")
    top_text.draw(win)

    bottom_text = Text(Point(width/2, height/1.2), "Click to chose my door")
    bottom_text.draw(win)

    button1_txt = Text(Point(65, 225), "Door1")
    button1_txt.draw(win)
    button2_txt = Text(Point(200, 225), "Door2")
    button2_txt.draw(win)
    button3_txt = Text(Point(335, 225), "Door3")
    button3_txt.draw(win)

    if button1.is_clicked(p1, p2):
        button1.color_button(button1, "red")
        top_text.undraw()
        top_text.setText("You Lost!")
        top_text.draw(win)
        bottom_text.undraw()
        bottom_text.setText("Door2 is my secret door")
        bottom_text.draw(win)
    elif button2.is_clicked(p3, p4):
        button2.color_button(button2, "green")
        top_text.undraw()
        top_text.setText("You Win")
        top_text.draw(win)
        bottom_text.undraw()
        bottom_text.setText("Click to close")
        bottom_text.draw(win)
    elif button3.is_clicked(p5, p6):
        button3.color_button(button3, "red")
        top_text.undraw()
        top_text.setText("You Lost!")
        top_text.draw(win)
        bottom_text.undraw()
        bottom_text.setText("Door2 is my secret door")
        bottom_text.draw(win)

    win.getMouse()
    win.close()

if __name__ == "__main__":
    main()
