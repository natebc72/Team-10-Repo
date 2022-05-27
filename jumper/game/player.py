class Player:
    def __init__(self):
        self._letter = ''
        self._letters = []

    def get_letter(self):
        return self._letter

    def set_letter(self, letter):
        self._letter = letter
        self._letters.append(letter)

    def get_letters(self):
            return self._letters
