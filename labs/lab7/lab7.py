"""
Name: Shelby Rhodes
Partner: <your partner's name goes here – first and last>
lab7.py
"""
import math

def cash_conversion():
    number = eval(input("Enter an integer "))
    print('{:.2f}'.format(number))

def encode():
    s = input("Enter a message to be encoded ")
    keyword = eval(input("Enter an integer key value "))
    acc = ""
    for c in s:
       i = ord(c)
       sum = keyword + i
       c = chr(sum)
       acc = acc + c
    print(acc)

def sphere_area(radius):
    area = 4 * math.pi * (radius ** 2)
    return area

def sphere_volume(radius):
    volume = (4 / 3) * math.pi * (radius ** 3)
    return volume

def sum_n(n):
    sum = (n * (n + 1)) /2
    return sum

def sum_n_cubes(n):
    sum = (n ** 2 * ((n + 1) ** 2)) /4
    return sum

def encode_better():
    s = input("Enter a message ")
    k = input("Enter a key value ")
    acc = ""
    for i in range(len(s)):
        c = s[i]
        key = k[i % len(k)]
        c = ord(c)
        key = ord(key) - 97
        sum = key + c
        c = chr(sum)
        acc = acc + c
    print(acc)




def main():
    cash_conversion()
    encode()
    print(sphere_area(2))
    print(sphere_volume(2))
    print(sum_n(5))
    print(sum_n_cubes(3))
    encode_better()
    pass


main()
