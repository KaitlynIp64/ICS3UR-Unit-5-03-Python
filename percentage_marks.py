#!/usr/bin/env python3

# Created by: Kaitlyn Ip
# Created on: Dec 2022
# This program tells the user their mark as a percentage


def calculate_grade(mark: str) -> int:
    # calculate area

    # process
    match mark:
        case "4+":
            percent = 97
        case "4":
            percent = 87
        case "4-":
            percent = 80
        case "3+":
            percent = 78
        case "3":
            percent = 75
        case "3-":
            percent = 70
        case "2+":
            percent = 68
        case "2":
            percent = 65
        case "2-":
            percent = 61
        case "1+":
            percent = 58
        case "1":
            percent = 54
        case "1-":
            percent = 51
        case "R":
            percent = 30
        case "NE":
            percent = 0
        case _:
            percent = -1

    return percent


def main():
    # input

    mark = input("Enter the level you want converted into a percentage: ")

    # call functions
    mark_percentage = calculate_grade(mark)
    if mark_percentage == -1:
        print("That is not a valid input.")
    else:
        print(
            "The level {0} converted into a percentage is: {1}%".format(
                mark, mark_percentage
            )
        )

    print("\nDone.")


if __name__ == "__main__":
    main()
