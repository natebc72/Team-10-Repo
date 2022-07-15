import pyray
from point import Point


class KeyboardService:
    """Detects player input. 
    
    The responsibility of a KeyboardService is to indicate whether or not a key is up or down.

    Attributes:
        _keys (Dict[string, int]): The letter to key mapping.
    """

    def __init__(self):
        """Constructs a new KeyboardService."""
        self._keys = {}
        
        self._keys['w'] = pyray.KEY_W
        self._keys['s'] = pyray.KEY_S
        self._keys['f'] = pyray.KEY_F

        self._keys['u'] = pyray.KEY_U
        self._keys['j'] = pyray.KEY_J
        self._keys['l'] = pyray.KEY_L

    def is_key_up(self, key):
        """Checks if the given key is currently up.
        
        Args:
            key (string): The given key (w, s, f or u, j, l)
        """
        pyray_key = self._keys[key.lower()]
        return pyray.is_key_up(pyray_key)

    def is_key_down(self, key):
        """Checks if the given key is currently down.
        
        Args:
            key (string): The given key (w, s, f or u, j, l)
        """
        pyray_key = self._keys[key.lower()]
        return pyray.is_key_down(pyray_key)