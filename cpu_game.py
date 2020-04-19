
#Program written and maintained by Matthew Meyerink

#File responsible for defining the CPU game class
import random
from cpu_phrases import phrases

class CPU_game:

    def __init__(self):
        self.num_guesses = 0
        self.num_wrong_guesses = 0
        self.num_correct_guesses = 0
        self.cpu_phrase = ""
        self.guessed_word = ""
        self.current_guess = ""

    #Ramdomly selects a phrase from a list of phrases and assign to cpu_phrase
    def generate_cpu_phrase(self):
        random_number = random.randint(0, len(phrases) - 1)
        self.cpu_phrase = phrases[random_number]

    #Underscores for characters and spaces for spaces
    def init_guessed_word(self):
        for i in range(0, len(self.cpu_phrase)):
            if self.cpu_phrase[i] != " ":
                self.guessed_word += "_"
            else:
                self.guessed_word += " "

    #Gets the current user guess
    def get_user_guess(self):
        input_guess = input("Please enter your guess: ")
        self.current_guess = input_guess.upper()

    #Checks if current guess is in the word
    def check_guess(self):
        self.cpu_phrase.find(current_guess)

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
