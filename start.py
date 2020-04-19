
#Program written and maintained by Matthew Meyerink

#File responsible for starting the game and handling user menu choice

import test
import game

#Function to print the game's header
def print_header():
    print("")
    print("Welcome to the hangman game!")
    print("----------------------------")
    print("")

#Function to print the game menu
def print_menu():
    print("Please pick one of the options below")
    print("(1) Play game against CPU")
    print("(2) Play game against another user")
    print("(3) Quit")
    print("(4) Run Test Suite")
    print("")

#Function to print the game closer
def print_closer():
    print("---------------------------------------")
    print("Thank you for playing the hangman game!")

menu_choice = 1

#Loop through game options until the user quits
while (menu_choice != 3) and (menu_choice != 4):

    #Get initial menu choice
    print_header()
    print_menu()
    menu_choice = int(input())

    #Branch to run game against the CPU
    if menu_choice == 1:
        game.game(menu_choice)
        print_menu()
        menu_choice = int(input())

    #Branch to run game against another user
    elif menu_choice == 2:
        print("")
        print("That didnt work maybe typing in boobz will help\n")
        print_menu()
        menu_choice = int(input())

    #Branch to quit the game and print the closer
    elif menu_choice == 3:
        print_closer()

    #Temporary branch to run the test suite
    elif menu_choice == 4:
        test.test_suite()

    #Branch to catch invalid input
    else:
        print("Invalid input, please try again\n")
        print_menu()
        menu_choice = int(input())
