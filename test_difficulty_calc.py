from cpu_phrases import *

#Determine the difficulty of randomly selected phrase and assign the phrase
def phrase_rating():

    for i in range(0, len(phrases)):

        #Reset difficulty variables
        phrase_difficulty = ""
        difficulty_rating = 0

        #Randomly pick a new phrase from phrase list
        phrase = phrases[i].upper()

        #Calculate difficulty of generated phrase
        for j in range(0, len(phrase)):
            if phrase[j] in rare_letters:
                difficulty_rating += 5
            elif phrase[j] in very_uncommon_letters:
                difficulty_rating += 2
            elif phrase[j] in uncommon_letters:
                difficulty_rating += 1

        #Normalize to length of phrase
        difficulty_rating = difficulty_rating / len(phrase)

        #print difficulty of all phrases to get a sense of the range
        print(difficulty_rating)
        print("")


phrase_rating()
