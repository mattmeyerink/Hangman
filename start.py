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

print_header()
print_menu()
menu_choice = input()

#Loop through game options until the user quits
while (menu_choice != 3) and (menu_choice != 4):

    if menu_choice == 1:
        print("")
        print("The CPU game will be here soon this takes time fucker\n")
        print_menu()
        menu_choice = input()

    elif menu_choice == 2:
        print("")
        print("That didnt work maybe typing in boobz will help\n")
        print_menu()
        menu_choice = input()

    elif menu_choice == 3:
        print_closer()

    elif menu_choice == 4:
        print("Test Suite coming soon to a develouper near you\n")

    else:
        print("Invalid input, please try again\n")
        print_menu()
        menu_choice = input()
