"""
Name: Shelby Rhodes
lab13.py
"""
from random import randint


def is_in_binary(search_val, values):
    mid = len(values) // 2
    while search_val != mid and len(values) != 1:
        if mid < search_val:
            values = values[mid:]
        else:
            values = values[:mid]
        mid = len(values) // 2
    if search_val == mid:
        return True
    return False


def selection_sort(values):
    for i in range(len(values)):
        lowest = values[i]
        pos = i
        for j in range(i, len(values)):
            if j < lowest:
                lowest = values[j]
                pos = j
        values[i], values[pos] = values[pos], values[i]
    print(values)


def get_area(rect):
    return randint(1, 100)


def rect_sort(rectangles):
    d = {}
    areas = []
    for rect in rectangles:
        d[get_area(rect)] = rect
        areas.append(get_area(rect))
    selection_sort(areas)
    for i in range(len(areas)):
        rectangles[i] = d[areas[i]]


def trade_alert(filename):
    infile = open(filename, 'r')
    data = infile.read().split()
    seconds = 0
    for num in data:
        seconds += 1
        if '830' > num > '500':
            print(seconds, "WARNING")
        if num > '830':
            print(seconds, "ALERT!")


def main():
    is_in_binary(3, [1, 2, 3, 4, 5, 6])
    selection_sort([1, 4, 2, 3, 5])
    rect_sort()
    trade_alert('trades.txt')


main()
