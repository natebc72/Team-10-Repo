import constants
from actor import Actor
from point import Point


class Tank(Actor):
    """
    <=>
      P
    |/\|
    |\/|

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self, player):
        super().__init__()
        self.player = player