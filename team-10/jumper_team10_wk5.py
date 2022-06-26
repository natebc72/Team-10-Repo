# Jumper Game (Generic Brand of 'Hangman')
# Team 10 
# 5/19/2022

import random

# J'DEE
# The puzzle is a secret word randomly chosen from a list.
class Words:
    """ The responsibility of this class is to generate and randomly pick from a list of words.
    
    Attributes: words: an array of words to choose from
                puzzle_word: the chosen word for the game
    """
def __init__(self):
    self._words = ["books", "class", "games", "plant", "water"]
    self.puzzle_word = ""
# # # Methods
# # # # set_word(self)
def set_word(self):
    """generates the puzzle word from the words array, and sets the value of the puzzle word to the selected word.
    
    Arguments: self: an insance of words.
    """
    self.puzzle_word = random._self.words()
    return self.puzzle_word

# # # # # logic (random.xyz)

# NATE
# # Letters Class
# # init
# # # Attibutes
# # # # self.letters -> array
# # Methods
# # # # remove_letters(self)
# # # # # logic: Removes letters as the user chooses them

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
# # # # elif num_wrong eq 2-5
# # # # # jumper_image eq ..
# # # # elif the player has no more parachute the game is over.
# # # # If the puzzle is solved the game is over.

# CALEB
# # Display Class
# # # Displays/updates the ASCII image

# MARCOS
# main
# Game rules
# create the objects
# # word array
# # alphabet array
# User input
# # 
