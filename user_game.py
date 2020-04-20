
#Program written and maintained by Matthew Meyerink

#File responsible for defining the game based on user input

from cpu_game import CPU_game

class User_Game(CPU_game):

    #Get the user phrase to start the game
    def get_user_phrase(self):
        self.phrase = input("Please input a phrase: ").upper()
        print("")
