
#Program written and maintained by Matthew Meyerink

#File responsible for defining the CPU game class
import random
from cpu_phrases import *
from warning_color import Warning
class CPU_Game:

    def __init__(self):
        self.num_wrong_guesses = 0
        self.phrase = ""
        self.guessed_word = ""
        self.current_guess = ""
        self.wrong_guesses = []

    #Determine the difficulty of randomly selected phrase and assign the phrase
    def phrase_rating(self, difficulty):
        if difficulty == "easy" or difficulty == "medium" or difficulty == "hard":

            #Initialize difficulty values
            phrase_difficulty = ""
            difficulty_rating = 0

            while (not phrase_difficulty == difficulty):

                #Reset difficulty variables
                phrase_difficulty = ""
                difficulty_rating = 0

                #Randomly pick a new phrase from phrase list
                random_number = random.randint(0, len(phrases) - 1)
                self.phrase = phrases[random_number].upper()

                #Calculate difficulty of generated phrase
                for i in range(0, len(self.phrase)):
                    if self.phrase[i] in rare_letters:
                        difficulty_rating += 5
                    elif self.phrase[i] in very_uncommon_letters:
                        difficulty_rating += 2
                    elif self.phrase[i] in uncommon_letters:
                        difficulty_rating += 1

                #Normalize to length of phrase
                difficulty_rating = difficulty_rating / len(self.phrase)

                #Assign difficulty to that phrase
                if difficulty_rating < easy_rating:
                    phrase_difficulty = "easy"

                elif difficulty_rating < medium_rating:
                    phrase_difficulty = "medium"

                else:
                    phrase_difficulty = "hard"

            #return true to indicate a valid difficulty was input
            return True

        else:
            #return false to indicate an invalid difficulty was input
            return False

    #Underscores for characters and spaces for spaces in the guessed word
    def init_guessed_word(self):
        for i in range(0, len(self.phrase)):
            if self.phrase[i] != " ":
                self.guessed_word += "_"
            else:
                self.guessed_word += " "

    #Gets the current user guess
    def get_user_guess(self):
        #Loop to get a user guess until an error isn't thrown
        while True:
            try:
                input_guess = input("Please enter your guess: ")

                #Throw error if more than one char or non letter input
                if ((not input_guess.isalpha()) or len(input_guess) > 1):
                    raise ValueError

                #Assign the current guess if no error thrown
                self.current_guess = (input_guess.upper())[0]

                break

            #Catch thrown error if present
            except ValueError:
                print(Warning.YELLOW +
                    "\nCan you cooperate and actually enter one letter???\n" +
                    Warning.END)

    #Checks if current guess is in the word and updates guess word if it is
    def check_guess(self):

        already_guessed = (self.current_guess in self.guessed_word
                        or self.current_guess in self.wrong_guesses)

        #Go through each part of string and replace guess letter with current
        #letter if they are the same
        num_letters_added = 0
        for i in range(0, len(self.phrase)):
            if self.phrase[i] == self.current_guess[0]:
                self.guessed_word = (self.guessed_word[:i] + self.current_guess
                            + self.guessed_word[i + 1:])
                num_letters_added += 1

        #Bool and branch to check if the player has already guessed this
        if (already_guessed):
            print("")
            print(Warning.RED + "You already guessed that." +
                            " Pay better attention dumbass!!\n" + Warning.END)

            self.num_wrong_guesses += 1

        #If there were no matches for the guess letter add to wrong bank and
        #Increment wrong guesses
        elif num_letters_added == 0:
            self.num_wrong_guesses += 1
            self.wrong_guesses.append(self.current_guess)

    #Determines if the man was hanged ie HANGMAN you lose
    def hanged(self):
        return self.num_wrong_guesses == 6

    #Determines if the user won the game
    def game_won(self):
        blank_left = True
        for i in range(0, len(self.guessed_word)):
            if (self.guessed_word[i] == "_"):
                blank_left = False
        return blank_left

    #Function to print the list of wrong guesses
    def print_wrong_guesses(self):
        for i in range(0, len(self.wrong_guesses)):
            if(i == 0):
                print(self.wrong_guesses[i].upper(), end = '')
            else:
                print(", " + self.wrong_guesses[i].upper(), end = '')

        print("")

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

        #Changed so that 6 wrongs ends game but keeping feet art just in case
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
