# Jumper Game (Generic Brand of 'Hangman')
# Team 10 
# 5/27/2022

import random
from numpy import number

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
        words = ["bolts", "claps", "games", "plant", "water"]
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
        self.user_choice = input("Guess a letter [a-z]: ")
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
# # # Game Class
class Game():
# # init
    def __init__(self):
        self.num_wrong = 0
        self.winner = False
        self.answer_array = [" _ ", " _ ", " _ ", " _ ", " _ "]
    
    """This is the main section of game-play, in which the logic of all of the other classes come together."""
    def play_round(self):
        """Objects are created within the method of this class based on previous classes."""
        game_letter = Letters()
        game_word = Words()
        term_serv = TerminalService()
        letters = ""
        """term_serv is the object created from the TerminalService class, and display is the method within that
        class."""
        puzzle_array = game_word.set_word()
        """A for loop is here to call the letters array from the Letter class"""
        for i in game_letter.letters_array:
            letters += i
        """Here we have the main logic game loop, keeping the game rolling. It tests if the game is won or lost,
        and loops through the logical rules."""
        while term_serv.num_wrong != 5:
            while self.winner != True:
                game_letter.add_letters()
                """This loop checks the puzzle array against the user's choice."""
                for i in puzzle_array:
                    """If the user choice is the same as the piece of the puzzle it's checking
                    in the loop then..."""
                    if (game_letter.user_choice == i):
                        """print this and..."""
                        print("Super Duper!")
                        """We need to find the spot where the letter goes. We use the index function
                        and put the number in the 'place' variable then..."""
                        place = puzzle_array.index(i)
                        """...replace the underscore in the answer array with the value from the user choice."""
                        self.answer_array[place] = i
                        """The right answer is true, which variable is used later down the loop..."""
                        right_answer = True
                        break
                    else:
                        right_answer = False
                """The if statement below takes the returned value of the letters class, which 
                is the test if the letter had already been guessed, and adds the user choice to the
                letters for display if it returns false."""
                if game_letter.already_guessed == False:
                    letters += game_letter.user_choice
                """If the right answer is false, then the num_wrong increases, and the method in the 
                terminalserver class is called upon to remove a part of the whole_jumper's parachute."""
                if right_answer == False:
                    term_serv.num_wrong += 1
                    term_serv.remove_chute()                
                print(" ")
                """I know there's a simpler way to do this, but it's 2am."""
                print(game_play.answer_array[0], game_play.answer_array[1], game_play.answer_array[2],game_play.answer_array[3],game_play.answer_array[4])
                print(" ")
                term_serv.display()
                print(" ")
                print(f'\nNumber of wrong guesses: {term_serv.num_wrong}\n')
                print(f'letters you have guessed: {letters}\n')
                print("")
                """This calls the 'count' function to see if there are any underscores. If not, then the word
                is filled, and the user wins. Hurray!"""
                if self.answer_array.count(" _ ") == 0:
                    print("You have won!")
                    self.winner == True
                    return self.winner
                """It's a bit dark, I know, but it's also 2am, and it's dark outside. Too early for flapjacks???"""
                if term_serv.num_wrong >= 5:
                    print("That's too many wrong. I'm sorry, your jumper's parachute stopped functioning, and now they are dead.")
                    break
            print("Dead, dead, dead.")
        



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
        print("")
        print("^^^^^^^^")

        
game_play = Game()
game_play.play_round()





