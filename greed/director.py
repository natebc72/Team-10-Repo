import random
from point import Point
from color import Color
from objects import Objects
from cast import Cast

"""Global variables are helpful here for the class that will create the rocks."""
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
WHITE = Color(255,255,255)

class Director:
    """
    Caleb
    
    A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service,):
        """Constructs a new Director using the specified keyboard and video services. Also enables the score class.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
            score (Score): An instance of score.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self.score = 0
    """Creating rocks and gems: Rock/gem randomly selected."""
    def create_rocks_and_gems(self, cast):
        list = ["gem", "rock"]
        text = ""
        object_type = random.choice(list)
        # Lane of movement chosen randomly, but it will always start at the top.
        x = random.randint(1, COLS - 1)
        y = 1
        # Position pulled from the Point class and scaled based on a global variable
        position = Point(x, y)
        position = position.scale(CELL_SIZE)
        value = 0
        # Velocity is set at random, so all of the objects are moving at different speeds
        velocity = random.randint(3, 15)
        # This is how the gem and rock are defined. If it is a gem, it will be an asterisk and will
        # be worth a point. If it is a rock, it will be an 'O' (or square in the game) and work -1.
        if (object_type == "gem"):
            value = 1
            text = "*"
        elif(object_type == "rock") :
            value = -1
            text = "O"
        # The color of each object is also randomly selected.
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        
        # Initially, I had each object numbered, but this is unnecessary in this iteration of the program.
        # None-the-less, the name of the object stays the same, as a number requires less memory. Save the whales!
        object_number = 1
        object_number = Objects()
        object_number.set_text(text)
        object_number.set_type(object_type)
        object_number.set_font_size(FONT_SIZE)
        object_number.set_color(color)
        object_number.set_position(position)
        object_number.set_value(value)
        object_number.set_velocity(Point(0, velocity))
        cast.add_actor("objects", object_number)   
    
    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        for n in range(40):
            self.create_rocks_and_gems(cast)
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the robot.
        
        Args:
            cast (Cast): The cast of actors.
        """
        robot = cast.get_first_actor("robots")
        velocity = self._keyboard_service.get_direction()
        robot.set_velocity(velocity)        

    def _do_updates(self, cast):
        """Updates the robot's position and resolves any collisions with objects by deleting the objects and then adding their score to our overall score.
        
        Args:
            cast (Cast): The cast of actors.
        """
        scoreboard = cast.get_first_actor("banners")
        robot = cast.get_first_actor("robots")
        object = cast.get_actors("objects")
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        robot.move_next(max_x, max_y)

        
        """This was the beast that took all of the time. I'll break it down piece by piece."""
        # We start with a loop
        for objects in object:
            # We use the loop to first start the pieces moving.
            objects.move_next(max_x, max_y)
            # Now, we get the position of the object by digging into the Point class.
            # We only need to know the location when the object reaches the bottom of the screen.
            if objects._position.get_y() >= 550:
                # If the object is near the bottom of the screen, we compare its x value with that of the
                # robot. 
                if objects._position.get_x() == robot._position.get_x():
                    # If the location is equal, then we change the score based on the object value...
                    self.score += objects.get_value()
                    # Reset the new score on the scoreboard...
                    scoreboard.set_text(f'Your score is {self.score}. ')
                    # Remove the object from the screen...
                    cast.remove_actor("objects", objects)
                    # and add a new object by calling the create_rocks_and_gems method initialized above.
                    self.create_rocks_and_gems(cast)
                    

                    
        
    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()