# Jumper Game (Generic Brand of 'Hangman')
# Team 10 
# 5/19/2022

import random

# J'DEE
# The puzzle is a secret word randomly chosen from a list.
# # Words Class
class Word():
# # init
    def __init__(self):
# # # Attributes
        self.word_array = ["wasps", "pizza", "happy", "milks", "paper", "prone", "child", "joker", "zebra", "lilly", "zebra", "vexed",
                      "gangs", "there", "think", "check", "bluff", "knife", "right", "learn", "fault", "where", "phone", "pinch",
                      "prison", "effect", "relic", "young", "proud"]
        self.puzzle_word = ""
        self.puzzle_array = []
    def set_puzzle_word(self):
        self.puzzle_word = self.word_array[random.randint(0,28)]
        self.puzzle_array = [self.puzzle_word[0],self.puzzle_word[1],self.puzzle_word[2],self.puzzle_word[3],self.puzzle_word[4]]
        return self.puzzle_array
    
        


    
# NATE
# Letters Class
class Letters():
# # init
    def __init__(self):
# # # Attibutes
        self.letters = ["a","b","c","d","e","f","g","h","i","j","k",
                        "l","m","n","o","p","q","r","s","t","u","v",
                        "w","x","y","z"]
        self.user_choice = ""
# Methods
# # # remove_letters(self)
    def remove_letters(self):
        self.letters.remove(self.user_choice)
        return self.letters

# # JEREMY
# # # Rules Class
class Game():
# # init
    def __init__(self):
        self.number_wrong = 0
        self.winner = True
        self.answer_array = [" _ ", " _ ", " _ ", " _ ", " _ "]
    

# # # Attributes:
# # # # self.user_choice -> taken from input
# # # # self.jumper_image -> start with initial ascii
# # # # self.num_wrong -> 1-5, start at 0
# # # # self.winner -> boolean
# # # super init
# # Methods

    
    def rules(self):
        pass
        
        
# # # # If the guess is correct, the letter is revealed.
# # # # If the guess is incorrect, a line is cut on the player's parachute.
# # # # if num_wrong eq 1
# # # # # jumper_image eq 
game_play = Game()
game_word = Word()
puzzle_array = game_word.set_puzzle_word()
print(game_word.puzzle_word)
print(puzzle_array[1])

# game_letter = Letters()
# print(game_letter.letters[3])


# print("")
# print("    ___")
# print("   /___\\")
# print("   \\   /")    
# print("    \\ /")    
# print("     O")
# print("    /|\\")
# print("    / \\")
# print("")
# print("^^^^^^^^^^^^")
# # # # # elif num_wrong eq 2
# # # # # # jumper_image eq ..
# print("")
# print("    ")
# print("   /___\\")
# print("   \\   /")    
# print("    \\ /")    
# print("     O")
# print("    /|\\")
# print("    / \\")
# print("")
# print("^^^^^^^^^^^^")
# # # # # elif num_wrong eq 3
# # # # # # jumper_image eq ..
# print("")
# print("")
# print("")
# print("   \\   /")    
# print("    \\ /")    
# print("     O")
# print("    /|\\")
# print("    / \\")
# print("")
# print("^^^^^^^^^^^^")
# # # # # elif num_wrong eq 4
# # # # # # jumper_image eq ..
# print("")
# print("")
# print("")
# print("")    
# print("    \\ /")    
# print("     O")
# print("    /|\\")
# print("    / \\")
# print("")
# print("^^^^^^^^^^^^")
# # # # # elif num_wrong eq 5
# # # # # # jumper_image eq ..
# print("")
# print("")
# print("")
# print("")    
# print("")    
# print("     X")
# print("    /|\\")
# print("    / \\")
# print("")
# print("^^^^^^^^^^^^")
# # # # # elif the player has no more parachute the game is over.
# # # # # If the puzzle is solved the game is over.

# # CALEB
# # # Display Class
# # # # Displays/updates the ASCII image
# # _ _ _ _ _
# #
# #  


   


# # MARCOS
# # main
# # Game rules
# # create the objects
# # # word array
# # # alphabet array
# # User input
# # # 

