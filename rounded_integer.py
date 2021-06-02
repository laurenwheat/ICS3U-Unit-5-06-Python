#!/usr/bin/env python3

# Created by: Lauren Wheatley
# Created on: May 2021
# This program determines the factorial of a number


def integerRounded(decimal_pc, user_num):

    user_num[0] = user_num[0] * (10 ** decimal_pc[0]) + 0.5
    user_num[0] = int(user_num[0])
    user_num[0] = user_num[0] / (10 ** decimal_pc[0])


def main():

    decimal_pc = []
    user_num = []

    while True:
        try:
            user_input = input("Enter which decimal you want to round: ")
            user_float = float(user_input)

            decimal_input = input("How many places is it rounded to?: ")
            decimal_int = int(decimal_input)

            user_num.append(user_float)
            decimal_pc.append(decimal_int)

            integerRounded(decimal_pc, user_num)

            break
        except Exception:
            print("That is not a valid input!!!")

    print("{0} is {1} rounded to {2} decimal places".format(user_input,
                                                            decimal_pc[0],
                                                            user_num[0]))


if __name__ == "__main__":
    main()
