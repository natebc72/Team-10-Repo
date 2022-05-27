# Jumper Game (Generic Brand of 'Hangman')
# Team 10 
# 5/19/2022

import random

# J'DEE
# The puzzle is a secret word randomly chosen from a list.
# # Words Class
class Words:
    """ The responsibility of this class is to generate and randomly pick from a list of words.
    
    Attributes: words: an array of words to choose from
                puzzle_word: the chosen word for the game
    """
    def __init__(self):
        self.puzzle_word = ""
# # # Methods
# # # # set_word(self)
    def set_word(self):
        """generates the puzzle word from the words array, and sets the value of the puzzle word to the selected word.
    
    Arguments: self: an insance of words."""
        words = ["boots", "clats", "gamet", "plant", "water"]
        self.puzzle_word = random.choice(words)
        return self.puzzle_word
    
        


    
# NATE
# Letters Class
class Letters():
# # init
    def __init__(self):
# # # Attibutes
        self.letters_array = []
        self.user_choice = ""
        self.already_guessed = False

# Methods
# # # remove_letters(self)

    def add_letters(self):
        self.user_choice = input("Choose a letter: ")
        for i in self.letters_array:
            if i == self.user_choice:
                print("You already guessed this. Try again.")
                self.already_guessed = True
                return self.already_guessed
            else:
                self.already_guessed = False
        self.letters_array.append(self.user_choice)
        return self.already_guessed

# # JEREMY
# # # Rules Class
class Game():
# # init
    def __init__(self):
        self.num_wrong = 0
        self.winner = False
        self.answer_array = [" _ ", " _ ", " _ ", " _ ", " _ "]
    
    def play_round(self):
        game_letter = Letters()
        game_word = Words()
        term_serv = TerminalService()
        letters = ""
        term_serv.display()
        puzzle_array = game_word.set_word()
        for i in game_letter.letters_array:
            letters += i
        while term_serv.num_wrong != 5:
            while self.winner != True:
                game_letter.add_letters()
                for i in puzzle_array:
                    if (game_letter.user_choice == i):
                        print("Super Duper!")
                        place = puzzle_array.index(i)
                        self.answer_array[place] = i
                        right_answer = True
                        break
                    else:
                        right_answer = False
                if game_letter.already_guessed == False:
                    letters += game_letter.user_choice
                if right_answer == False:
                    term_serv.num_wrong += 1
                    term_serv.remove_chute()                
                print(" ")
                print(game_play.answer_array[0], game_play.answer_array[1], game_play.answer_array[2],game_play.answer_array[3],game_play.answer_array[4])
                print(" ")
                print(f'\nNumber of wrong guesses: {term_serv.num_wrong}\n')
                term_serv.display()
                print(" ")
                print(f'letters you have guessed: {letters}\n')
                print("")
        print("That's too many wrong. I'm sorry, your jumper's parachute stopped functioning, and now they are dead.")
        



class TerminalService:
    def __init__(self):
        #Separated each step into a picture which will disappear when there is a mistake.
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
    def remove_chute(self):
        if (self.num_wrong == 1) | (self.num_wrong == 3) | (self.num_wrong == 4):
            self._whole_picture.remove(self._whole_picture[0])
        elif self.num_wrong == 2:
            #replaces second_mistake with third_mistake
            self._whole_picture[0] = self._third_mistake
        elif self.num_wrong == 5:
            self._whole_picture.remove(self._whole_picture[0])
            self._whole_picture[0] = self._dead_guy
        elif self.num_wrong <=0:
            self._whole_picture = self._whole_picture
        return self._whole_picture

    def display(self):
        print(*self._whole_picture, sep='\n')
    

    
    def rules(self):
        pass
        
game_play = Game()
game_play.play_round()



