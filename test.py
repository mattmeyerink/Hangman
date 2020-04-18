from cpu_game import CPU_game
#Program written and maintained by Matthew Meyerink

#File responsible for testing the functions of the game.

#Test function for CPU_game
def test_cpu_game():

    game = CPU_game()
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

#Test suite main function
def test_suite():
    test_cpu_game()
