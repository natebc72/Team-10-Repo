from color import Color
from point import Point

class Score:
   
    """
    Nate

    Take the value from the objects class and update our score
    """
    #sets up the score and constructs scoreboard 
    def __init__(self):
        self._text = ""
        self._font_size = 18
        self._color = Color(255, 255, 255)
        self._position = Point(0, 0)
        
        
        
    def set_text(self, text):
        #this will update the scoreboard text
        self._text = text
   
    def set_font_size(self, font_size):
        #this will set the font size
        self._font_size = font_size
        
    def set_color(self, color):
        #this will be used to set the scoreboard color    
        self._color = color
        
    def set_position(self, position):
        #this will be used to place the scoreboard on the screen
        self._position = position
