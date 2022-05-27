from game.terminal_service import TerminalService
from game.player import Player
from game.game import Game


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        player: 
        is_playing (boolean): Whether or not to keep playing.
        puzzle:        
        terminal_service: For getting and displaying information on the terminal.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._player = Player()
        self._is_playing = True
        self._game = Game()
        self._terminal_service = TerminalService()
        
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        """Moves the seeker to a new location.

        Args:
            self (Director): An instance of Director.
        """
        new_letter = self._terminal_service.read_text("\nGuess a letter [a-z]: ")
        self._player.set_letter(new_letter)
        
    def _do_updates(self):
        """Keeps watch on where the seeker is moving.

        Args:
            self (Director): An instance of Director.
        """
        self._game._get_hidden_word_list(self._player.get_letters())
        self._game._is_letter_in_word(self._player._letter)
        
        
    def _do_outputs(self):
        """Provides a hint for the seeker to use.

        Args:
            self (Director): An instance of Director.
        """
        self._terminal_service.display_word(self._game._hidden_word)
       
        if self._game.is_terminal():
            self._is_playing = False