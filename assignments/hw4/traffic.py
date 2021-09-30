"""
Name: Shelby Rhodes
traffic.py

Problem: This program will analyze traffic patterns

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

def main():
    roads = eval(input("How many roads were surveyed? "))
    total = 0
    for i in range(roads):
        acc = 0
        days = eval(input("How many days was road " + str(i + 1) + " surveyed? "))
        for _ in range(days):
            cars = eval(input("How many cars traveled on day " + str(_ + 1) + "? "))
            acc = acc + cars
            total = total + cars
            average_vehicles = acc / days
        print("Road", (i+1), "average vehicles per day: ", round(average_vehicles, 2))
    print("Total number of vehicles traveled on all roads: ", total)
    average_per_road = total / roads
    print("Average number of vehicles per road: ", round(average_per_road,2))

if __name__ == "__main__":
    main()
