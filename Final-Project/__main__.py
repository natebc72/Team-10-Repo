import constants

from cast import Cast
from script import Script
from control_actors_action import ControlActorsAction
from move_actors_action import MoveActorsAction
from handle_collisions_action import HandleCollisionsAction
from draw_actors_action import DrawActorsAction
from director import Director
from keyboard_service import KeyboardService
from video_service import VideoService
from color import Color
from point import Point
from tank import Tank



def main():
    
    # create the cast
    cast = Cast()
    cast.add_actor("tank1", Tank(1))
    cast.add_actor("tank2", Tank(2))
    
   
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()