# Jumper Game (Generic Brand of 'Hangman')
# Team 10 
# 5/19/2022

import random

# J'DEE
# The puzzle is a secret word randomly chosen from a list.
class words:
    """ The responsibility of this class is to generate and randomly pick from a list of words.
    
    Attributes: words: an array of words to choose from
                puzzle_word: the chosen word for the game
    """
def __init__(self):
    self.words = ["books", "class", "games", "plant", "water"]
    self.puzzle_word = ""
# # # Methods
# # # # set_word(self)
def set_word(self):
    """generates the puzzle word from the words array, and sets the value of the puzzle word to the selected word.
    
    Arguments: self: an insance of words.
    """
    self.puzzle_word = random.self.words()
# # # # # logic (random.xyz)

# NATE
# # Letters Class
"""""variable will hold the gueesed letters"""
lettersGuessed = ""
"""logic: Removes letters as the user chooses them and stores them into the variable."""
"""guess is a placeholder for the user input."""
lettersGuessed = lettersGuessed + guess(userinput)


# JEREMY
# # Rules Class
# # init
# # # Attributes:
# # # # self.user_choice -> taken from input
# # # # self.jumper_image -> start with initial ascii
# # # # self.num_wrong -> 1-5, start at 0
# # # # self.winner -> boolean
# # # super init
# # Methods
# # # rules(self)
# # # # If the guess is correct, the letter is revealed.
# # # # If the guess is incorrect, a line is cut on the player's parachute.
# # # # if num_wrong eq 1
# # # # # jumper_image eq 
# # # # If the puzzle is solved the game is over.

# CALEB
# # Display Class
# # # Displays/updates the ASCII image
# _ _ _ _ _
#
#  


   

# # # Displays the parachute and man. Requires the number of mistakes to know how much of the parachute to get rid of.
class TerminalService:


    def __init__(self):
        #Seperatted each step into a picture which will disappear when there is a mistake.
        self._first_mistake = "  ___"
        self._second_mistake = " /___\ "
        #The third mistake is actually just the second line without the / and \.
        self._third_mistake = "  ___"
        self._fourth_mistake = " \   /"
        self._fifth_mistake = "  \ /"
        self._guy = "   o\n  /|\ \n  / \ "
        #Dead guy is used at the very end to represent a loss.
        self._dead_guy = "   x\n  /|\ \n  / \ "
        #Decided to combine all of the different pictures into an array so I could print it easier.
        self._whole_picture = [self._first_mistake, self._second_mistake, self._fourth_mistake, self._fifth_mistake, self._guy]
        self.num_wrong = 0
        
    #display function uses if statements to change the array and then displays it 
    def display(self):
        if self.num_wrong >= 1:
            self._whole_picture.remove("  ___")
        if self.num_wrong >= 2:
            #replaces second_mistake with third_mistake
            self._whole_picture[0] = self._third_mistake
        if self.num_wrong >= 3:
            self._whole_picture.remove("  ___")
        if self.num_wrong >= 4:
            self._whole_picture.remove(" \   /")
        if self.num_wrong >= 5:
            self._whole_picture.remove("  \ /")
            self._whole_picture[0] = self._dead_guy
        print(*self._whole_picture, sep='\n')

# MARCOS
# main
# Game rules
# create the objects
# # word array
# # alphabet array
# User input
# # 

#def main():
    #words = Words()
    #letters = Letters()
    #rules = Rules()
    #display = Display()

    #User Input
    #rules.user_choice = input("Guess a letter [a-z]: ")
    #rules.verify_letter(words.puzzle_word)
    


