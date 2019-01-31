#
# Pythoon: 3.7
#
# Author: Allan Reitan
#
# Purpose: The Tech Academy - Python Course tutorial lesson on making a game.
#
#           Uses modules and imported function calls with basic exception handling.


def start(nice=0,mean=0,name=""):
    # get user's name
    name = describe_game(name)
    nice,mean,name = nice_mean(nice,mean,name)

 def describe_game(name):
     """
     check if this is a new instance of the game.
     """
    if name != "":
        print("\nThank you for playing again, {}!".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nWhat is your name? \n>>> ").capitalize()
                if name != "":
                    print("\nWelcome, {}!".format(name))
                    print("\nIn this game, you will be greeted \nby several different people. \nYou can choose to be nice or mean")
                    print("but at the end of the game your fate \nwill be sealed by your actions.")
                    stop = False
return name

def nice_mean(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mesn,name)
        pick = input("\nA stranger approaches you for a \nconversation. Will you be nice \nor mesn? (N/M) \n>>>").lower()
        if pick == "n":
            print("\nThe stranger walks away smiling...")
            nice = (nice + 1)
            stop = False
        if pick == "m":
            print("\nThe stranger glares at you \nmenacingly and storms off...")
            mean = (mean + 1)
            stop = False
        score(nice,mean,name)   # pass the 3 variables to the score()




if __name__ == "__main__":
    start()
