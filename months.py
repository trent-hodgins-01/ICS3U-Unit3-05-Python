# !/user/bin/env python3

# Created by Trent Hodgins
# Created on 09/22/2021
# This is the Month program
# The user enters in the number of a month and the program tells them the month


def main():
    # this function checks what month it is

    # input
    number = int(input("Enter in number (1-12): "))
    print("")

    # process and output
    if number == 1:
        print("January")
    elif number == 2:
        print("February")
    elif number == 3:
        print("March")
    elif number == 4:
        print("April")
    elif number == 5:
        print("May")
    elif number == 6:
        print("June")
    elif number == 7:
        print("July")
    elif number == 8:
        print("August")
    elif number == 9:
        print("September")
    elif number == 10:
        print("October")
    elif number == 11:
        print("November")
    elif number == 12:
        print("December")
    else:
        print("Not a month. Enter a number between 1 and 12")

    print("\nDone")


if __name__ == "__main__":
    main()
