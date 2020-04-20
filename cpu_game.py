
#Program written and maintained by Matthew Meyerink

#File responsible for defining the CPU game class
import random
from cpu_phrases import phrases

class CPU_game:

    def __init__(self):
        self.num_wrong_guesses = 0
        self.cpu_phrase = ""
        self.guessed_word = ""
        self.current_guess = ""
        self.wrong_guesses = []

    #Ramdomly selects a phrase from a list of phrases and assign to cpu_phrase
    def generate_cpu_phrase(self):
        random_number = random.randint(0, len(phrases) - 1)
        self.cpu_phrase = phrases[random_number]

    #Underscores for characters and spaces for spaces in the guessed word
    def init_guessed_word(self):
        for i in range(0, len(self.cpu_phrase)):
            if self.cpu_phrase[i] != " ":
                self.guessed_word += "_"
            else:
                self.guessed_word += " "

    #Gets the current user guess
    def get_user_guess(self):
        input_guess = input("Please enter your guess: ")
        self.current_guess = (input_guess.upper())[0]

    #Checks if current guess is in the word and updates guess word if it is
    def check_guess(self):
        #Bool and branch to check if the player has already guessed this
        already_guessed = (self.current_guess in self.guessed_word
                        or self.current_guess in self.wrong_guesses)

        if (already_guessed):
            print("\nYou already guessed that. Pay better attention dumbass\n")
            self.num_wrong_guesses += 1

        #Go through each part of string and replace guess letter with current
        #letter if they are the same
        num_letters_added = 0
        for i in range(0, len(self.cpu_phrase)):
            if self.cpu_phrase[i] == self.current_guess[0]:
                self.guessed_word = (self.guessed_word[:i] + self.current_guess
                            + self.guessed_word[i + 1:])
                num_letters_added += 1

        #If there were no matches for the guess letter add to wrong bank and
        #Increment wrong guesses
        if num_letters_added == 0:
            self.num_wrong_guesses += 1
            self.wrong_guesses.append(self.current_guess)

    #Determines if the man was hanged ie HANGMAN you lose
    def hanged(self):
        return self.num_wrong_guesses == 8

    #Determines if the user won the game
    def game_won(self):
        blank_left = True
        for i in range(0, len(self.guessed_word)):
            if (self.guessed_word[i] == "_"):
                blank_left = False
        return blank_left

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
