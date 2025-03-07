#!/usr/bin/env python3
# Created By: Jayden Smith
# Date: March 6, 2025
# This programs calculates the circumference and area of a circle

import math


def main():
    # This give the user input for the radius
    radius = int(input("What is the radius of the circle? (cm) "))
    # This part of the code calculates the Circumference and area of a circle.
    circumference = (math.pi * radius * 2)
    area = (math.pi * (radius**2))
    # Code then displays information
    print("Circumference is {:.2f}cm".format(circumference))
    print("Area is {:.2f}cm".format(area))


if __name__ == "__main__":
    main()
