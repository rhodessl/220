"""
Name: Shelby Rhodes
weighted_average.py

Problem: Compute averages and write them to a file

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

def weighted_average(in_file_name, out_file_name):
    infile = open(in_file_name, 'r')
    outfile = open(out_file_name, 'w+')
    acc= 0
    for line in infile:
        # separates names from w and g's
        x = line.split(": ")
        names = x[0]
        names = names.split(" ")
        # creates first and last name order
        first_and_last = names[0] + " " + names[-1]
        # creates a string of w and g's
        weights_and_grades = x[1]
        numbers = weights_and_grades.split(" ")
        # list is created of w and g's as string
        i = 0
        weights = 0
        for number in numbers:
            # gets position of the w's
            w = numbers[i]
            wint = int(w)
            weights = weights + wint
            g = numbers[1]
            i = i + 1
            product = int(w) * int(g)
            print(product)
            average = product / 100
        print(weights)
        acc = acc + average
        class_average = round(acc, 1)
    if weights == 100:
        outfile.write(first_and_last + "'s average: " + average + "\n")
    elif weights < 100:
        outfile.write(first_and_last + "'s average: Error: The weights are less than 100." + "\n")
    else:
        outfile.write(first_and_last + "'s average: Error: The weights are more than 100." + "\n")
    outfile.write("Class average: " + str(class_average))

def main():
    weighted_average('grades.txt', 'avg.txt')

main()
