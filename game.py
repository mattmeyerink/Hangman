
#Program written and maintained by Matthew Meyerink

#File containing function to run CPU and user run hangman games

from cpu_game import CPU_Game
from user_game import User_Game

def game(menu_choice):

    #Branch for CPU generated game mode
    if menu_choice == 1:

        #Generate a CPU class game
        game = CPU_Game()

        #Print CPU game header
        print("\nGood Luck! The CPU is out to beat you!")
        print("--------------------------------------")

        #Generate the phrase for the game
        correct_difficulty = False
        while (not correct_difficulty):
            difficulty = input("\nPlease input a difficulty (Easy, Medium, Hard): ")
            difficulty = difficulty.lower()

            #Generate CPU phrase and update correct_difficulty
            correct_difficulty = game.generate_cpu_phrase(difficulty)

            #Output if difficulty input invalid
            if (not correct_difficulty):
                print("\nNot a valid difficulty")

        game.init_guessed_word()

        #Loop through the game while the person is not hanged and the word
        #Isn't guessed
        while not game.hanged() and not game.game_won():

            #Print the framework of the game
            game.print_gallows(game.num_wrong_guesses)
            print("Incorrect guesses")
            game.print_wrong_guesses()
            print("\n" + game.guessed_word + "\n")

            #Recieve the user guess and check it
            game.get_user_guess()
            game.check_guess()

        #Check to see if the person was hanged and output loss message
        if (game.hanged()):
            game.print_gallows(game.num_wrong_guesses)
            print("The word was " + game.phrase)
            print("\nYou lost to a computer. AI is clearly taking over the world\n")

        #Check to see if the person won the game and output message
        elif (game.game_won()):
            print("\n" + game.guessed_word)
            print("\nYou beat the computer! Maybe AI won't take over the world!\n")

    #Branch for user generate game mode
    elif menu_choice == 2:

        #Generate a User based game
        game = User_Game()

        #Print User game header
        print("\nGood Luck! Your friend is out to beat you!")
        print("--------------------------------------------")

        #Recieve and handle the phrase for the game
        game.get_user_phrase()
        game.init_guessed_word()

        #Loop through the game while the person is not hanged and the word
        #Isn't guessed
        while not game.hanged() and not game.game_won():

            #Print the framework of the game
            game.print_gallows(game.num_wrong_guesses)
            game.print_wrong_guesses()
            print("\n" + game.guessed_word + "\n")

            #Recieve the user guess and check it
            game.get_user_guess()
            game.check_guess()

        #Check to see if the person was hanged and output loss message
        if (game.hanged()):
            game.print_gallows(game.num_wrong_guesses)
            print("\nYour friend got you on that one. Let their party begin!\n")

        #Check to see if the person won the game and output message
        elif (game.game_won()):
            print("\n" + game.guessed_word)
            print("\nYou beat your friend! Let the party begin!\n")
