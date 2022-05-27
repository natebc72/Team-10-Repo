
import random

class Puzzle:
    def __init__(self):
        self._word = self._get_random_word(['book','pen'])
        self._hidden_word = []

    def _get_random_word(self,words):
        return random.choice(words)

    def _get_hidden_word_list(self,letters):
        self._hidden_word = ['_' for i in range(len(self._word))]

        for i in range(len(self._word)):
            for letter in letters:
                if letter == self._word[i]:
                    self._hidden_word[i] = letter
        
        return self._hidden_word

    def is_terminal(self):
        count = 0
        for i in range(len(self._word)):
            if self._word[i] != self._hidden_word[i]:
                count += 1
        if count == 0:
            return True
        return False



        


        



    