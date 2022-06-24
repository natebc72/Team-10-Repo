import constants
from actor import Actor
from action import Action
from point import Point

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
        self._winner = 0

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
        snake_one = cast.get_first_actor("snake1")
        snake_two = cast.get_first_actor("snake2")

        snake_one_head = snake_one.get_segments()[0]
        snake_one_segments = snake_one.get_segments()[1:]

        snake_two_head = snake_two.get_segments()[0]
        snake_two_segments = snake_two.get_segments()[1:]

        for segment in snake_one_segments:
            if snake_one_head.get_position().equals(segment.get_position()):
                self._is_game_over = True
                self._winner = 2
                #snake1 collided with its segments
        for segment in snake_two_segments:
            if snake_two_head.get_position().equals(segment.get_position()):
                self._is_game_over = True
                self._winner = 1
                #snake2  collided with its segments

    def _handle_snakes_collision(self, cast):
         """Sets the game over flag if the snake1 or snake2 collides with each other.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        snake_one = cast.get_first_actor("snake1")
        snake_two = cast.get_first_actor("snake2")

        snake_one_head = snake_one.get_segments()[0]
        snake_one_segments = snake_one.get_segments()[1:]

        snake_two_head = snake_two.get_segments()[0]
        snake_two_segments = snake_two.get_segments()[1:]

        for segment in snake_one_segments:
            if snake_two_head.get_position().equals(segment.get_position()):
                self._is_game_over = True
                self._winner = 1
                #snake1 win
        for segment in snake_two_segments:
            if snake_one_head.get_position().equals(segment.get_position()):
                self._is_game_over = True
                self._winner = 2
                #snake2 win

    def _handle_game_over(self, cast):
        """Shows the who won message and turns the snake1 and snake2 white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            snake_one = cast.get_first_actor("snake1")
            snake_two = cast.get_first_actor("snake2")
            
            snake_one_segments = snake_one.get_segments()
            snake_two_segments = snake_two.get_segments()

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

            for segment in snake_one_segments:
                segment.set_color(constants.WHITE)

            for segment in snake_two_segments:
                segment.set_color(constants.WHITE)