import random
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

"""

Draw the screen
Define controlled object (main robot)
    Set rules for the controlled object
        size, position, left/right movement

Define objects(actors)
Define the robot(actors)
Create actors(cast)
Create cast



Define automated scrolling objects
    OBJECT CLASS(POINT, COLOR):
    Set general rules for the objects
        where do they initiate
            Top of the screen (use Point class)
        how often do they initiate
            every second?
        How many at a time?
            5?
        how are they terminated
            When it goes off screen
            When the position of the object is close enough to the robot
    Set specific rules for objects
        ROCKS CLASS(OBJECTS)
        Rocks(Inherits from Objects)
            Set the character to 'O'
            What happens when the object comes into contact with the robot
                Subtract 1 (Score -= 1)
                Terminate object (remove from object array)
        GEMS CLASS(OBJECTS)
        Gems(Inherits from Objects)
            Set the character display to '*'
            What happens when the object comes into contact with the robot
                Add 1 (Score += 1)
                Terminate object (remove from object array)
Create the objects

            

"""

FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "GREED"
WHITE = Color()


def main():
    
    print("Start")
    
    # create the cast
    cast = Cast()
    
    group1 = "Johnson"
    
    cast.add_actor(group1, "actor1")
    cast.get_actors(group1)
    cast.get_first_actor(group1)
    
    # location of the robot
    x = MAX_X / 2
    y = 10
    position = Point(x, y)
    
    # creating the robot itself
    robot = Actor()
    robot.set_color(WHITE)
    robot.set_text("#")
    robot.set_font_size(FONT_SIZE)
    robot.set_position(position)
    cast.add_actor("robots", robot)
    
    
    # create the scoreboard
    score = 0
    scoreboard = Actor()
    scoreboard.set_text(f'Your score is {score}. ')
    scoreboard.set_font_size(FONT_SIZE)
    scoreboard.set_color(WHITE)
    scoreboard.set_position(Point(590, 15))
    cast.add_actor("banners", scoreboard)
    
    

    # for n in range(DEFAULT_ARTIFACTS):
    #     text = chr(random.randint(33, 126))
    #     message = messages[n]

    #     x = random.randint(1, COLS - 1)
    #     y = random.randint(1, ROWS - 1)
    #     position = Point(x, y)
    #     position = position.scale(CELL_SIZE)

    #     r = random.randint(0, 255)
    #     g = random.randint(0, 255)
    #     b = random.randint(0, 255)
    #     color = Color(r, g, b)
        
    #     artifact.set_text(text)
    #     artifact.set_font_size(FONT_SIZE)
    #     artifact.set_color(color)
    #     artifact.set_position(position)
    #     artifact.set_message(message)
    #     cast.add_actor("artifacts", artifact)
    
    # start the game
    # keyboard_service = KeyboardService(CELL_SIZE)
    # video_service = VideoService(CAPTION, 0, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    # director = Director(keyboard_service, video_service, 0)
    # director.start_game(cast)


if __name__ == "__main__":
    main()
"""
Jeremy
"""