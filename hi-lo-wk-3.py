
import random
# This class sets the player's points, and is updated based on the functions of the gameplay
class Player:
    def __init__(self):
        self.score = 300
    #Comment here
    def player_score(self):
        return self.score
# The 'Game' class is designed to create and set the values of the cards and the user input,
# and determine if the user is a winner or a loser.
class Game:
    def __init__(self):
        self.card_value = 1
        self.next_card_value = 0
        self.player_choice = " "
        self.winner = True


    def get_next_card_value(self):
        return self.next_card_value

   # Two if-then statements are set here, taking input from the attributes of the class
   # and outputting and answer, then testing the user-based answer against the corect
   # answer.
    def is_winner(self):
        correct_answer = 1
        answer = 1
        if self.next_card_value > self.card_value:
            correct_answer = 1
        else:
            correct_answer = 2
        if self.player_choice == "l":
            answer = 2
        else:
            answer = 1

        if answer == correct_answer:
            self.winner = True
        else: 
            self.winner = False
       # This returns the winner, which changes after each turn, based on the logic above. 
        return self.winner
        
# Below is the main game-play. Objects are created from the classes, 
# and the logic of the game is set within a 'while' loop.
player = Player()
game = Game()
play_again = "y"
# As long as the variable 'play_again' is yes, the game-play continues.
# In essense, this is a 'do-while' loop.
# User input is prompted and put into variables within the corresponding
# objects, and the logic ensues.
while play_again == "y":
    print(f'The card is: {game.card_value}')
    game.player_choice = input("Higher or lower? [h/l]: ")
    game.next_card_value = random.randint(2,12)
    print(f'The next card was: {game.next_card_value}')
    game.is_winner()
    # After values are set and placed into their corresponding object variables,
    # the is_winner function needs to run, within the game object. If True is
    # returned, the player.score attribute within the player object is increased
    # by 100. If False is returned, 100 points are taken away.
    if game.winner == True:
        player.score += 100
    elif game.winner == False:
        player.score -= 100      
    print(f'Your score is: {player.score}')
    # The new card needs to be set and the current card value in case the user chooses
    # to play again.
    game.card_value = game.next_card_value
    play_again = input("Play again? [y/n]: ")
    print(" ")
else:
    print(f'Thanks for playing!! Your final score was: {player.score}')
