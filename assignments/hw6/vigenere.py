"""
Name: Shelby Rhodes
vigenere.py

Problem: this program implements the Vigenere cipher

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from graphics import *


def code(message, keyword):
    message = message.upper()
    message = message.replace(" ", "")
    keyword = keyword.upper()
    keyword = keyword.replace(" ", "")
    keyword_length = len(keyword)
    keyword_as_int = [ord(i) for i in keyword]
    message_int = [ord(i) for i in message]
    resulting_msg = ''
    for i in range(len(message_int)):
        value = (message_int[i] + keyword_as_int[i % keyword_length]) % 26
        resulting_msg += chr(value + 65)
    return resulting_msg

def main():
    width = 600
    height = 400
    win = GraphWin("Vigenere", width, height)
    win.setBackground("white")

    msg = Text(Point(200, 100), "Message to encode")
    msg.draw(win)

    msg_box = Entry(Point(370, 100), 30)
    msg_box.draw(win)

    key = Text(Point(200, 150), "Enter keyword")
    key.draw(win)

    key_box = Entry(Point(350, 150), 20)
    key_box.draw(win)

    button = Rectangle(Point(250, 200), Point(350, 250))
    button.draw(win)

    encode_txt = Text(Point(300, 225), "Encode")
    encode_txt.setSize(15)
    encode_txt.draw(win)

    win.getMouse()
    button.undraw()
    encode_txt.undraw()

    resulting_txt = Text(Point(300, 200), "Resulting Message")
    resulting_txt.draw(win)

    message = msg_box.getText()
    keyword = key_box.getText()

    resulting_msg = code(message, keyword)

    new_message = Text(Point(300, 225), resulting_msg)
    new_message.draw(win)

    inst_pt = Point(width / 2, 300)
    inst_txt = Text(inst_pt, "Click to close")
    inst_txt.draw(win)

    win.getMouse()
    win.close()


if __name__ == "__main__":
    main()

