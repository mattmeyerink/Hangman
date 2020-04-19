
#Program written and maintained by Matthew Meyerink

#File containing function to run CPU and user run hangman games

from cpu_game import CPU_game

def game(menu_choice):
    if menu_choice == 1:

        #Generate a CPU class game
        game = CPU_game()

        #Print CPU game header
        print("Good Luck! The CPU is out to beat you!\n")
        print("--------------------------------------")

        #Generate the phrase for the game
        game.generate_cpu_phrase()
        game.init_guessed_word()

        while not game.hanged() and not game.game_won():
            game.print_gallows(game.num_wrong_guesses)
            print(game.guessed_word)

            game.get_user_guess()
            game.check_guess()

        if (game.hanged()):
            game.print_gallows()
            print("You lost to a computer. AI is clearly taking over the world")

        elif (game.game_won()):
            print("You beat the computer! Maybe AI won't take over the world!")
