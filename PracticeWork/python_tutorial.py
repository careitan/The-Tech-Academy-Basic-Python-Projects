#
# Pythoon: 3.7
#
# Author: Allan Reitan
#
# Purpose: The Tech Academy - Python Course tutorial lesson on making a game.
#
#           Uses modules and imported function calls with basic exception handling.


def start():
    print("Hello {}!".format(get_name()))



def get_name():
    name = input("What is your name?")
    return name




if __name__ == "__main__":
    start()
