"""
Name: Shelby Rhodes
lab6.py
"""


def name_reverse():
    """
    Read a name in first-last order and display it in last-comma-first order.
    """
    x = input("Enter a person's name in first-last order ")
    x = x.split()
    print(x[1] + " , " + x[0])

def company_name():
    x = input("Enter a three-part internet domain name ")
    x = x.split(".")
    print(x[1])

def initials():
    n = eval(input("How many names will be input "))
    for i in range(n):
        first = input("Enter the first name of student " + str(i+1))
        last = input("Enter the last name of student " + str(i+1))
        print(first[0] + last[0])

def names():
    x = input("Enter a list of names first and last only separated by commas")
    x = x.split(",")
    for name in x:
        parts = name.split()
        print("The initials are " + parts[0][0] + parts[1][0])

def thirds():
    n = eval(input("How many sentences will be input? "))
    for _ in range(n):
        s = input("Enter a sentence ")
        print(s[2::3])

def word_average():
    x = input("Enter a sentence ")
    acc = 0
    x = x.split()
    for word in x:
        acc = acc + len(word)
    print(acc/len(x))

def pig_latin():
    x = input("Enter a sentence ")
    x = x.lower()
    x = x.split()
    for word in x:
        print(word[1:] + word[0] + "ay", end=" ")




def main():
    name_reverse()
    company_name()
    initials()
    names()
    thirds()
    word_average()
    pig_latin()

    # add other function calls here


main()
