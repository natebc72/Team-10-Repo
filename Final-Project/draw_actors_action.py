from action import Action


class DrawActorsAction(Action):
    """
    An output action that draws all the actors.
    
    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        tank1 = cast.get_first_actor("tank1")
        tank2 = cast.get_first_actor("tank2")
        messages = cast.get_actors("messages")
        tank_one = tank1.get_body()
        tank_two = tank2.get_body()
        bullets_one = tank1.get_bullets()
        bullets_two = tank2.get_bullets()

        self._video_service.clear_buffer()
        self._video_service.draw_actors(tank_one)
        self._video_service.draw_actors(tank_two)
        self._video_service.draw_actors(bullets_one)
        self._video_service.draw_actors(bullets_two)
        self._video_service.draw_actors(messages, True)
        self._video_service.flush_buffer()