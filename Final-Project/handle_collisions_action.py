import constants
from actor import Actor
from action import Action
from point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the bullet collides into a tank and causes a game over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False
        self._winner = 0

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_bullet_collision(cast)
            self._handle_game_over(cast)


    def _handle_bullet_collision(self, cast):
        """Sets the game over flag if tank1 or tank2 are hit by a bullet.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        tank_one = cast.get_first_actor("tank1")
        tank_two = cast.get_first_actor("tank2")

        tank_one_body = tank_one.get_body()
        tank_two_body = tank_two.get_body()

        tank_one_bullets = tank_one.get_bullets()
        tank_two_bullets = tank_two.get_bullets()


        
        for bullet in tank_one_bullets:
            bullet_position = bullet.get_position()
            tank_position = tank_two_body[0].get_position()
            if bullet_position.get_x() > 800:
                if bullet_position.get_y() == tank_position.get_y():
                    tank_one_bullets.remove(bullet)
                    self._is_game_over = True
                    self._winner = 1
                    #tank1 win
                else:
                    tank_one_bullets.remove(bullet)

        for bullet in tank_two_bullets:
            bullet_position = bullet.get_position()
            tank_position = tank_one_body[0].get_position()
            if bullet_position.get_x() <= 100:
                if bullet_position.get_y() == tank_position.get_y():
                    tank_two_bullets.remove(bullet)
                    self._is_game_over = True
                    self._winner = 2
                    #tank1 win
                else:
                    tank_two_bullets.remove(bullet)

    def _handle_game_over(self, cast):
        """Shows the who won message.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            
            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            if self._winner == 1:
                message.set_text("Player One Wins!")
            if self._winner == 2:
                message.set_text("Player Two Wins")
            message.set_position(position)
            cast.add_actor("messages", message)
