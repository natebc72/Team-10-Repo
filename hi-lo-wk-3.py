
import random
#Comment here
class Player:
    def __init__(self):
        self.score = 300
    #Comment here
    def player_score(self):
        return self.score
#Comment here
class Game:
    def __init__(self):
        self.card_value = 1
        self.next_card_value = 0
        self.player_choice = " "
        self.winner = True

    #Comment here
    def get_next_card_value(self):
        return self.next_card_value

   #Comment Here
    def is_winner(self):
        correct_answer = 1
        answer = 1
        if self.next_card_value > self.card_value:
            correct_answer = 1
        else:
            correct_answer = 2
        #Comment here
        if self.player_choice == "l":
            answer = 2
        else:
            answer = 1
        #Comment here
        if answer == correct_answer:
            self.winner = True
        else: 
            self.winner = False
            
        return self.winner
        
#Comment here
player = Player()
game = Game()
play_again = "y"
#Comment here
while play_again == "y":
    print(f'The card is: {game.card_value}')
    game.player_choice = input("Higher or lower? [h/l]: ")
    game.next_card_value = random.randint(2,12)
    print(f'The next card was: {game.next_card_value}')
    game.is_winner()
    #Comment here
    if game.winner == True:
        player.score += 100
    elif game.winner == False:
        player.score -= 100      
    print(f'Your score is: {player.score}')
    game.card_value = game.next_card_value
    play_again = input("Play again? [y/n]: ")
    print(" ")
else:
    print(f'Thanks for playing!! Your final score was: {player.score}')