import constants
from actor import Actor
from point import Point


class Tank(Actor):

    def __init__(self, player):
        super().__init__()
        self.player = player
        self._bullets = []
        self._body = []
        self._prepare_body()
        
    def get_body(self):
        return self._body
    
    def get_bullets(self):
        return self._bullets

    def move_next(self):
        # move all segments
        for tank in self._body:
            tank.move_next()
        for bullet in self._bullets:
            bullet.move_next()

    def change_direction(self, velocity):
        self._body[0].set_velocity(velocity)
    
    def _prepare_body(self):
        if self.player == 1:
            x = int(constants.MAX_X / 7)
            y = int(constants.MAX_Y / 2)
            text = "==-"
            #velocity = Point(0, 0)
        if self.player == 2:
            x = int(constants.MAX_X / 1.175)
            y = int(constants.MAX_Y / 2)
            text = "-=="
            #velocity = Point(0, 0)

        position = Point(x - 1 * constants.CELL_SIZE, y)

        
        if self.player == 1:
            color = constants.BLUE 
        if self.player == 2:
            color = constants.RED
            
        tank = Actor()
        tank.set_position(position)
        #tank.set_velocity(velocity)
        tank.set_text(text)
        tank.set_color(color)
        self._body.append(tank)

    def fire_bullet(self, player):
    
        bullet = Actor()
        self.player = player
        bullet.set_text("o")
        position = self._body[0].get_position()
        bullet.set_position(position)
        if self.player == 1:
            bullet.set_color(constants.BLUE)
            velocity = Point(1 * constants.CELL_SIZE, 0)
        if self.player == 2:
            bullet.set_color(constants.RED)    
            velocity = Point(-1 * constants.CELL_SIZE, 0)
        bullet.set_velocity(velocity)
        self._bullets.append(bullet)  

