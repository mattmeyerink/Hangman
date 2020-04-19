from cpu_game import CPU_game
#Program written and maintained by Matthew Meyerink

#File responsible for testing the functions of the game.

#Test function for CPU_game
def test_cpu_game():

    #Define a game to test
    game = CPU_game()

    #Test CPU_game.print_gallows()
    game.print_gallows(game.num_wrong_guesses)

    game.num_wrong_guesses = 1
    game.print_gallows(game.num_wrong_guesses)

    game.num_wrong_guesses = 2
    game.print_gallows(game.num_wrong_guesses)

    game.num_wrong_guesses = 3
    game.print_gallows(game.num_wrong_guesses)

    game.num_wrong_guesses = 4
    game.print_gallows(game.num_wrong_guesses)

    game.num_wrong_guesses = 5
    game.print_gallows(game.num_wrong_guesses)

    game.num_wrong_guesses = 6
    game.print_gallows(game.num_wrong_guesses)

    game.num_wrong_guesses = 7
    game.print_gallows(game.num_wrong_guesses)

    game.num_wrong_guesses = 8
    game.print_gallows(game.num_wrong_guesses)

    #Test CPU_game.generate_cpu_phrase()
    game.generate_cpu_phrase()
    print(game.cpu_phrase)

    #Test CPU_game.generate_blank_guessed_word()
    game.init_guessed_word()
    print(game.guessed_word)

    #Test CPU_game.get_user_guess()
    game.get_user_guess()
    print(game.current_guess)

    #Test CPU_game.check_guess()
    game.check_guess()
    print(game.guessed_word)

#Test suite main function
def test_suite():
    test_cpu_game()
