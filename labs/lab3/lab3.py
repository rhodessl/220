"""
Name: Shelby Rhodes
lab3.py
"""

def average():
    HW = eval(input("Number of grades to input:"))
    acc = 0
    for i in range(HW):
        grade = eval(input("Enter your grade on HW" +str(i + 1)))
        acc = grade + acc
    average =  acc / HW
    print(average)

average()

def tip_jar():
    acc = 0
    for i in range(1, 6):
        donation = eval(input("Amount of donation:"))
        acc = donation + acc
    print(acc)

tip_jar()

def newton():
    x = eval(input("Number:"))
    refine = eval(input("How many times:"))
    approx = x / 2
    for i in range(refine):
        approx = (approx + x/approx)/2
    print(approx)

newton()

def sequence():
    n = eval(input("What is the number of terms"))
    for x in range(n):
        y = 1 + ((x + 1) // 2 * 2)
        print(y)

sequence()

def pi():
    acc = 1
    terms = eval(input("What is the number of terms"))
    for x in range(terms):
        num = 2 + (x // 2 * 2)
        den = 1 + ((x + 1) // 2 * 2)
        acc = acc * (num/den)
    print(acc * 2)

pi()