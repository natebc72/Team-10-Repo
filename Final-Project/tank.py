import constants
from actor import Actor
from point import Point


class Tank(Actor):
    """
    [o]

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self, player):
        super().__init__()
        self.player = player

    def fire_bullet(self):
    
        bullet = Actor()

        velocity = bullet.get_velocity()
        offset = velocity.reverse()
        position = bullet.get_position().add(offset)
        bullet.set_position(position)
        bullet.set_velocity(velocity)
        bullet.set_text("o")
        if self.player == 1:
            bullet.set_color(constants.BLUE)
        if self.player == 2:
            bullet.set_color(constants.RED)      