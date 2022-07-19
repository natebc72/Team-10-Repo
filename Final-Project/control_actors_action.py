import constants
from action import Action
from point import Point
from tank import Tank


class ControlActorsAction(Action):
    """
    An input action that controls the tank.
    
    The responsibility of ControlActorsAction is to get the direction and move the tanks.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._direction_one = Point(0, 0)
        self._direction_two = Point(0, 0)

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        
        """
        tank_one = cast.get_first_actor("tank1")
        tank_two = cast.get_first_actor("tank2")
        
        # first tank up
        if self._keyboard_service.is_key_down('w'):
            self._direction_one = Point(0, -1)
        
        # first tank down
        if self._keyboard_service.is_key_down('s'):
            self._direction_one = Point(0, 1)
            
        #first tank fire
        if self._keyboard_service.is_key_down('f'):
            tank_one.fire_bullet(1)
            
          
        # second tank up
        if self._keyboard_service.is_key_down('u'):
            self._direction_two = Point(0, -1)
        
        # second tank down
        if self._keyboard_service.is_key_down('j'):
            self._direction_two = Point(0, 1)
            
        # second tank fire
        if self._keyboard_service.is_key_down('l'):
            tank_two.fire_bullet(2)
        
        
        direction_one = self._direction_one.scale(constants.CELL_SIZE)
        direction_two = self._direction_two.scale(constants.CELL_SIZE)

        tank_one.change_direction(direction_one)
        tank_two.change_direction(direction_two)


        
        
        

        
        