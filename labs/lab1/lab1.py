"""
Name: Shelby Rhodes
lab1.py

Problem: This function calculates the area of a rectangle
"""


def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)

def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height: "))
    volume = length * width * height
    print("Volume =", volume)

def shooting_percentage():
    total_shots = eval(input("Enter the total shots: "))
    shots_made = eval(input("Enter the shots made: "))
    percentage = shots_made / total_shots * 100
    print("Shooting percentage = %", percentage)

def coffee():
    number_of_pounds_of_coffee_purchased = eval(input("Enter the number of pounds of coffee purchased: "))
    total_cost = 11.36 * number_of_pounds_of_coffee_purchased + 1.50
    print("Total cost = $", total_cost)

def kilometers_to_miles():
    kilometers = eval(input("Enter the number of kilometers: "))
    miles = kilometers / 1.61
    print("Miles =", miles)


