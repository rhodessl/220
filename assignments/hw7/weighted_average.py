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
    avgacc = 0
    number_of_lines = 0
    for line in infile:
        # separates names from w and g's
        x = line.split(": ")
        names = x[0]
        # creates a string of w and g's
        weights_and_grades = x[1]
        numbers = weights_and_grades.split(" ")
        number_of_lines = number_of_lines + 1
        # list is created of w and g's as string
        i = 0
        weightacc = 0
        acc = 0
        weights = numbers[::2]
        grades = numbers[1::2]
        for i in range(len(weights)):
            acc = acc + int(weights[i]) * int(grades[i])
            weighti = int(weights[i])
            weightacc = weightacc + weighti
            i = i + 1
        average = acc / 100
        average = round(average, 1)
        avgacc = average + avgacc
        avgacc = round(avgacc, 1)
        if weightacc > 100:
            outfile.write(names + "'s average: Error: The weights are more than 100." + "\n")
        elif weightacc < 100:
            outfile.write(names + "'s average: Error: The weights are less than 100." + "\n")
        else:
            outfile.write(names + "'s average: " + str(average) + "\n")
    class_average = avgacc / number_of_lines
    class_average = round(class_average, 1)
    outfile.write("Class average: " + str(class_average))

def main():
    weighted_average('grades.txt', 'avg.txt')

if __name__ == "__main__":
    main()
