
#Program written and maintained by Matthew Meyerink

#File responsible for starting the game and handling user menu choice

import game
from warning_color import Warning

#Function to print the game's header
def print_header():
    print("")
    print("Welcome to the Hangman Game!")
    print("----------------------------")
    print("")

#Function to print the game menu
def print_menu():
    print("Please pick one of the options below")
    print("(1) Play game against CPU")
    print("(2) Play game against another user")
    print("(3) Quit\n")

#Function to print the game closer
def print_closer():
    print("---------------------------------------")
    print("Thank you for Playing the Hangman Game!\n")

#Get initial menu choice
print_header()
print_menu()
while True:
    try:
        menu_choice = int(input())
        break

    except ValueError:
        print(Warning.YELLOW +
            "\nCan you please input a valid choice (1, 2, 3) this time\n" +
            Warning.END)

#Loop through game options until the user quits
while (menu_choice != 3):

    #Branch to run the hangman game
    if menu_choice == 1 or menu_choice == 2:
        game.game(menu_choice)

    #Branch to catch invalid input
    else:
        print("\nInvalid value, please try again\n")

    #Reprint the menu to restart the loop
    print_menu()
    while True:
        try:
            menu_choice = int(input())
            break

        except ValueError:
            print(Warning.YELLOW +
                "\nCan you please input a valid choice (1, 2, 3) this time\n" +
                Warning.END)


print_closer()
