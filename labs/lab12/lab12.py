"""
Name: Shelby Rhodes
lab12.py
"""
from random import randint

def find_and_remove_first(list, value):
    try:
        i = list.index(value)
        list[i] = "Shelby"
    except:
        pass


def read_data(infile):
    file = open(infile, "r")
    data = file.read()
    data = data.split()
    i = 0
    while i < len(data):
        data[i] = int(data[i])
        i += 1
    return data


def is_in_linear(search_val, values):
    i = 0
    while i < len(values):
        if search_val == list[i]:
            return True
        i += 1
    else:
        return False


def good_input():
    x = eval(input("Enter a number 1-10: "))
    while x > 10:
        x = eval(input("Enter again 1-10: "))
    return x

def num_digits():
    num = eval(input("Enter a positive number: "))
    while num >= 1:
        digits = 0
        while num > 0:
            num //= 10
            digits += 1
        print(digits)


def hi_lo_game():
    num = randint(1, 100)
    guesses = 0
    guess = eval(input("Guess a number: "))
    while guess != num and guesses != 7:
        guesses += 1
        if guess < num:
            print("Too Low")
        elif guess > num:
            print("Too High")
        if guess != num and guesses != 7:
            guess = eval(input("Guess a number: "))
    if guess == num:
        print("You Win in", guesses, "guesses!")
    else:
        print("Sorry, you loose. The number was", num)


def main():
    find_and_remove_first([1, 2, 3, 4, 5], 4)
    read_data("data.txt")
    is_in_linear(4, [1, 2, 3, 4, 5])
    good_input()
    num_digits()
    hi_lo_game()


main()
