#!/usr/bin/env python3

# Created by: Kaitlyn Ip
# Created on: Dec 2022
# This program tells the user their mark as a percentage


def calculate(mark):
    # this function calculates the user's mark as a percentage

    # Process
    if mark == "4+":
        percentage = 95
    elif mark == "4":
        percentage = 87
    elif mark == "4-":
        percentage = 80
    elif mark == "3+":
        percentage = 77
    elif mark == "3":
        percentage = 73
    elif mark == "3-":
        percentage = 70
    elif mark == "2+":
        percentage = 67
    elif mark == "2":
        percentage = 63
    elif mark == "2-":
        percentage = 60
    elif mark == "1+":
        percentage = 57
    elif mark == "1":
        percentage = 53
    elif mark == "1-":
        percentage = 50
    elif mark == "R":
        percentage = 30
    else:
        percentage = -1
    return percentage


def main():
    # This function allows the user to input a mark and receive an outputted %

    # Input
    user_mark = input("Enter the level you want to convert into a percentage: ")

    # Process
    user_percentage = calculate(user_mark)

    # Output
    if user_percentage == -1:
        print("That is not a valid input.")
    else:
        print("Your mark as a percentage is: {0}%".format(user_percentage))


if __name__ == "__main__":
    main()
