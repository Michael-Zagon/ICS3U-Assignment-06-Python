#!/usr/bin/env python3

# Created by: Michael Zagon
# Created on: Oct 2021
# This program finds the perimeter of a hexagon


def perimeter_calculation(length):
    # This function calculates the perimeter of a hexagon

    perimeter = length * 6

    return perimeter


def main():
    # This function gets length from the user

    length = input("Enter the length of one of the hexagons sides (cm): ")

    try:
        length = int(length)
        # Call function
        final_perimeter = perimeter_calculation(length)
        print(
            "\nThe perimeter of a hexagon with the side lengths of {0} cm is {1} cm.".format(
                length, final_perimeter
            )
        )
    except Exception:
        print("\nInvalid Input.")

    print("\nDone.")


if __name__ == "__main__":
    main()
