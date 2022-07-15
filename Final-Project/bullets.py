from actor import Actor
import constants

class Bullets(Actor):
    """
    A fired projectile from the tank.
    
    The responsability of Bullets is to move the bullet in a straight line from the point it was fired.

    """
    def __init__(self):
        super().__init__()
        self._player
        self._set_text("o")
    
    def move_bullet(self, velocity):
        """
        Moves the bullet in a straight line from the point of fire.
        """
        player = self._player
        
        if player == 1:
            self.set_color(constants.RED)
        elif player == 2:
            self.set_color(constants.BLUE)
        
        self.velocity = velocity
        
