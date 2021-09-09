"""
Name: Shelby Rhodes
lab2.py

Problem: This function does input, produces output and does arithmetic.
"""
import math

def sum_of_threes():
    upper_bound = eval(input("What is the upper bound?"))
    acc = 0
    for x in range(0, upper_bound + 1, 3):
        acc = x + acc
    print(acc)

sum_of_threes()

def multiplication_table():
    for H in range(1, 11):
        for L in range(1, 11):
            print(H * L, end=" ")
        print()

multiplication_table()

def triangle_area():
    a = eval(input("What is the length of side a?"))
    b = eval(input("What is the length of side b?"))
    c = eval(input("What is the length of side c?"))
    s = (a + b + c) / 2
    A = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print(A)

triangle_area()

def sumSquares():
    upper_bound = eval(input("What is the upper bound?"))
    lower_bound = eval(input("What is the lower bound?"))
    acc = 0
    for x in range(lower_bound, upper_bound + 1):
        acc = (x ** 2) + acc
    print(acc)

sumSquares()

def power():
    base = eval(input("What is the base?"))
    exponent = eval(input("What is the exponent?"))
    acc = 1
    for i in range(exponent):
        acc = acc * base
    print(base, "^", exponent, "=", acc)

power()