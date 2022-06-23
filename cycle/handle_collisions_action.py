import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the another snake, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_segment_collision(cast)
            self._handle_snakes_collision(cast)
            self._handle_game_over(cast)
 
    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the snake1 or snake2 collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        snake1 = cast.get_first_actor("snake1")
        snake2 = cast.get_first_actor("snake2")

        snake1_head = snake1.get_segments()[0]
        snake1_segments = snake1.get_segments()[1:]

        snake2_head = snake2.get_segments()[0]
        snake2_segments = snake2.get_segments()[1:]

        for segment in snake1_segments:
            if snake1_head.get_position().equals(segment.get_position()):
                self._is_game_over = True
                #snake1 collided with its segments
        for segment in snake2_segments:
            if snake2_head.get_position().equals(segment.get_position()):
                self._is_game_over = True
                #snake2  collided with its segments

    def _handle_snakes_collision(self,cast):
         """Sets the game over flag if the snake1 or snake2 collides with each other.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        snake1 = cast.get_first_actor("snake1")
        snake2 = cast.get_first_actor("snake2")

        snake1_head = snake1.get_segments()[0]
        snake1_segments = snake1.get_segments()[1:]

        snake2_head = snake2.get_segments()[0]
        snake2_segments = snake2.get_segments()[1:]

        for segment in snake1_segments:
            if snake2_head.get_position().equals(segment.get_position()):
                self._is_game_over = True
                #snake1 win
        for segment in snake2_segments:
            if snake1_head.get_position().equals(segment.get_position()):
                self._is_game_over = True
                #snake2 win

    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake1 and snake2 white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            snake1 = cast.get_first_actor("snake1")
            snake2 = cast.get_first_actor("snake2")
            
            snake1_segments = snake1.get_segments()
            snake2_segments = snake2.get_segments()

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("Game Over!")
            message.set_position(position)
            cast.add_actor("messages", message)

            for segment in snake1_segments:
                segment.set_color(constants.WHITE)

            for segment in snake2_segments:
                segment.set_color(constants.WHITE)
