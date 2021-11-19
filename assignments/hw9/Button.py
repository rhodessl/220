"""
Name: Shelby Rhodes
button.py

Problem: the program encapsulates data for a button

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

class Button:
    def __init__(self, shape, label):
        self.shape = shape
        self.label = label

    def get_label(self, label):
        return self.label

    # def draw(self, win, shape, label):
    #     shape.draw(win)
    #     label.draw(win)

    # def undraw(self, win, shape, label):
    #     shape.undraw()
    #     label.undraw()

    def is_clicked(self, point1, point2,  win):
        point = win.getMouse()
        mouse_x = point.getX()
        mouse_y = point.getY()
        return point1.getX() < mouse_x < point2.getX() and point1.getY() < mouse_y < point2.getY()


    def color_button(self, shape, color):
        shape.setFill(color)

    def set_label(self, label, win):
        label.undraw()
        label.setText(label)
        label.draw(win)
