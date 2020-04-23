
#Program written and maintained by Matthew Meyerink

#File responsible for defining the game based on user input

from cpu_game import CPU_Game

class User_Game(CPU_Game):

    #Get the user phrase to start the game
    def get_user_phrase(self):
        correct_form = False
        while (not correct_form):

            correct_form = True

            #Recieve the input phrase
            self.phrase = input("Please input a phrase: ").upper()

            #Check to make sure no numbers or special characters in phrase
            for i in range(0, len(self.phrase)):
                alpha_space = self.phrase[i].isalpha() or self.phrase[i].isspace()
                if not alpha_space:
                    correct_form = False
                    print("\nPhrase needs to be all letters\n")
                    break

            #Check to make sure phrase isn't empty
            if self.phrase == "":
                correct_form = False
                print("\nDid you mean to input nothing? Do you want to play or not?!?!\n")
