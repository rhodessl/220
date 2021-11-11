"""
Name: Shelby Rhodes
lab11.py
"""
import random

def read_words():
    filename = "wordlist.txt"
    file = open(filename, "r")
    words = file.readlines()
    return words


def pick_secret_word(words):
    secret_word = random.choice(words)
    print(secret_word)
    return secret_word


def guessed_word(secret_word, blanks):
    letter = input('\n' "Guess a letter:")
    # acc = ""
    # for letter in secret_word:
    #     acc = acc + " " + letter
    # print(acc)
    # letters = acc.split(" ")
    # letters = letters[1:-1]
    # print(letters)
    for _ in range(len(secret_word)):
        if secret_word[_] == letter:
            blanks[_] = secret_word[_]
    print(blanks)


def word_spelled(secret_word, blanks):
    if blanks[:] == secret_word[:]:
        return True
    else:
        return False


def play_game():
    words = read_words()
    secret_word = pick_secret_word(words)
    blanks = []
    for _ in range(len(secret_word[1:])):
        blanks.append("_")
    for i in range(len(secret_word)):
        guessed_word(secret_word, blanks)

def main():
    play_game()
    pass


main()
