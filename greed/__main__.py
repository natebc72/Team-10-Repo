
import os
import random

from actor import Actor
from cast import Cast
from director import Director
from keyboard_service import KeyboardService
from video_service import VideoService
from color import Color
from point import Point
from objects import Objects


FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
CAPTION = "GREED"
WHITE = Color(255,255,255)


def main():
    
    print("Start")
    
    # create the cast
    cast = Cast()
    
    """Initial test:"""
    """group1 = "Johnson"
    
    cast.add_actor(group1, "actor1")
    cast.get_actors(group1)
    cast.get_first_actor(group1)"""
    
    # location of the robot
    x = MAX_X / 2
    y = 10
    position = Point(x, y)
    
    """End of initial test"""
    
    # creating the robot itself
    robot = Actor()
    robot.set_color(WHITE)
    robot.set_text("#")
    robot.set_font_size(FONT_SIZE)
    robot.set_position(Point(450,580))
    cast.add_actor("robots", robot)
    
    
    # create the scoreboard
    score = 0
    scoreboard = Actor()
    scoreboard.set_text(f'Your score is {score}. ')
    scoreboard.set_font_size(FONT_SIZE)
    scoreboard.set_color(WHITE)
    scoreboard.set_position(Point(1, 1))
    cast.add_actor("banners", scoreboard)
    
    
    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()
"""
Jeremy
"""