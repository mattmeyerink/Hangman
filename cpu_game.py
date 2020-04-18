
#Program written and maintained by Matthew Meyerink

#File responsible for defining the CPU game class
class CPU_game:

    def __init__(self):
        self.num_guesses = 0
        self.num_wrong_guesses = 0
        self.num_correct_guesses = 0
        self.cpu_phrase = ""
        self.guessed_word = ""
        self.current_guess

    #Ramdomly selects a phrase from a list of phrases
    def generate_phrases():
        phrases = [
        "To the well organized mind death is but the next great adventure",
        "Time will not slow down when somethin unpleasent lies ahead",
        "San Francisco is the best city in California"
        ]

    #Prints the gallows based on the number of incorrect guesses made
    def print_gallows(self, num_wrong_guesses):
        if (num_wrong_guesses == 0):
            print("")
            print("   --------")
            print("  |        |")
            print("  |")
            print("  |")
            print("  |")
            print("  |")
            print("  |")
            print("  |")
            print("  |")
            print("  |")
            print("-----")
            print("")

        if (num_wrong_guesses == 1):
            print("")
            print("   --------")
            print("  |        |")
            print("  |       ***")
            print("  |       ***")
            print("  |")
            print("  |")
            print("  |")
            print("  |")
            print("  |")
            print("  |")
            print("-----")
            print("")

        elif (num_wrong_guesses == 2):
            print("")
            print("   --------")
            print("  |        |")
            print("  |       ***")
            print("  |       ***")
            print("  |        *")
            print("  |        *")
            print("  |")
            print("  |")
            print("  |")
            print("  |")
            print("-----")
            print("")

        elif (num_wrong_guesses == 3):
            print("")
            print("   --------")
            print("  |        |")
            print("  |       ***")
            print("  |       ***")
            print("  |        ****")
            print("  |        *")
            print("  |")
            print("  |")
            print("  |")
            print("  |")
            print("-----")
            print("")

        elif (num_wrong_guesses == 4):
            print("")
            print("   --------")
            print("  |        |")
            print("  |       ***")
            print("  |       ***")
            print("  |     *******")
            print("  |        *")
            print("  |")
            print("  |")
            print("  |")
            print("  |")
            print("-----")
            print("")

        elif (num_wrong_guesses == 5):
            print("")
            print("   --------")
            print("  |        |")
            print("  |       ***")
            print("  |       ***")
            print("  |     *******")
            print("  |        *")
            print("  |         *")
            print("  |          *")
            print("  |")
            print("  |")
            print("-----")
            print("")

        elif (num_wrong_guesses == 6):
            print("")
            print("   --------")
            print("  |        |")
            print("  |       ***")
            print("  |       ***")
            print("  |     *******")
            print("  |        *")
            print("  |       * *")
            print("  |      *   *")
            print("  |")
            print("  |")
            print("-----")
            print("")

        elif (num_wrong_guesses == 7):
            print("")
            print("   --------")
            print("  |        |")
            print("  |       ***")
            print("  |       ***")
            print("  |     *******")
            print("  |        *")
            print("  |       * *")
            print("  |      *   **")
            print("  |")
            print("  |")
            print("-----")
            print("")

        elif (num_wrong_guesses == 8):
            print("")
            print("   --------")
            print("  |        |")
            print("  |       ***")
            print("  |       ***")
            print("  |     *******")
            print("  |        *")
            print("  |       * *")
            print("  |     **   **")
            print("  |")
            print("  |")
            print("-----")
            print("")
