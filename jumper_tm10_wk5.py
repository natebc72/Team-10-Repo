# Jumper Game (Generic Brand of 'Hangman')
# Team 10 
# 5/19/2022

import random

# J'DEE
# The puzzle is a secret word randomly chosen from a list.
# # Words Class
# # init
# # # Attributes
# # # # self.words -> array 
# # # # self.puzzle_word -> randomly chosen word
# # # Methods
# # # # set_word(self)
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
# # # Displays the parachute and man. Requires the number of mistakes to know how much of the parachute to get rid of.
class TerminalService:

    def __init__(self):
        #Seperatted each step into a picture which will disappear when there is a mistake.
        self.first_mistake = "  ___"
        self.second_mistake = " /___\ "
        #The third mistake is actually just the second line without the / and \.
        self.third_mistake = "  ___"
        self.fourth_mistake = " \   /"
        self.fifth_mistake = "  \ /"
        self.guy = "   o\n  /|\ \n  / \ "
        #Dead guy is used at the very end to represent a loss.
        self.dead_guy = "   x\n  /|\ \n  / \ "
        #Decided to combine all of the different pictures into an array so I could print it easier.
        self.whole_picture = [self.first_mistake, self.second_mistake, self.fourth_mistake, self.fifth_mistake, self.guy]
        
    #display function uses if statements to change the array and then displays it 
    def display(self, num_wrong):
        if num_wrong >= 1:
            self.whole_picture[0] = ""
        if num_wrong >= 2:
            #replaces second_mistake with third_mistake
            self.whole_picture[1] = self.third_mistake
        if num_wrong >= 3:
            self.whole_picture[1] = ""
        if num_wrong >= 4:
            self.whole_picture[2] = ""
        if num_wrong >= 5:
            self.whole_picture[3] = ""
            self.whole_picture[4] = self.dead_guy
        print(*self.whole_picture, sep='\n')

# MARCOS
# main
# Game rules
# create the objects
# # word array
# # alphabet array
# User input
# # 

