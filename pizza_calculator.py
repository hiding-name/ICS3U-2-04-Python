#!/usr/bin/env python3

# Created by: Matsuru Hoshi
# Created on: Sept 2019
# This is program calculates price of pizza

import constants


def main():
    # funciton calculates price pizza

    # Welcome statement
    print("Welcome, this is the Pizza Calculator 1000!")
    input("Press Enter to continue.")

    # input
    diameter = float(input("What is the diameter of your pizza (in): "))

    # process
    sub_total = (diameter * constants.MATERIALS) + constants.RENT \
        + constants.LABOUR
    total = sub_total + (sub_total * constants.HST)

    # output
    print("\nThe price is $" + str(round(total, 2)))


if __name__ == "__main__":
    main()
