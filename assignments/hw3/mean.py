"""
Name: Shelby Rhodes
mean.py

Problem:

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

import math

def main():
    values = eval(input("enter the number of values to be entered: "))
    rms_acc = 0
    harmonic_acc = 0
    geo_acc = 1
    for _ in range(values):
        value = eval(input("enter value: "))
        value1 = (value ** 2)
        value2 = (1 / value)
        rms_acc = value1 + rms_acc
        harmonic_acc = value2 + harmonic_acc
        geo_acc = geo_acc * value
    rms_average = math.sqrt(rms_acc / values)
    harmonic_mean = values / harmonic_acc
    geometric_mean = geo_acc ** (1 / values)
    print(round(rms_average, 3))
    print(round(harmonic_mean, 3))
    print(round(geometric_mean, 3))

if __name__ == "__main__":
    main()
