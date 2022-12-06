#!/usr/bin/env python3

# Created by: Kaitlyn Ip
# Created on: Dec 2022
# This program tells the user their mark as a percentage


def calculate(int_mark):
    # This function calculates the user's mark as a %

    # Process
    if int_mark == "4+":
        percentage = 95
    elif int_mark == "4":
        percentage = 87
    elif int_mark == "4-":
        percentage = 80
    elif int_mark == "3+":
        percentage = 77
    elif int_mark == "3":
        percentage = 73
    elif int_mark == "3-":
        percentage = 70
    elif int_mark == "2+":
        percentage = 67
    elif int_mark == "2":
        percentage = 63
    elif int_mark == "2-":
        percentage = 60
    elif int_mark == "1+":
        percentage = 57
    elif int_mark == "1":
        percentage = 53
    elif int_mark == "1-":
        percentage = 50
    elif int_mark == "R":
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

    print("\nDone.")


if __name__ == "__main__":
    main()
