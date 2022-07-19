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

    
    def _prepare_body(self):
        if self.player == 1:
            x = int(constants.MAX_X / 7)
            y = int(constants.MAX_Y / 2)
            text = "==-"
            velocity = Point(1 * constants.CELL_SIZE, 5)
        if self.player == 2:
            x = int(constants.MAX_X / 1.175)
            y = int(constants.MAX_Y / 2)
            text = "-=="
            velocity = Point(0, 0)

        position = Point(x - 1 * constants.CELL_SIZE, y)

        
        if self.player == 1:
            color = constants.BLUE 
        if self.player == 2:
            color = constants.RED
            
        tank = Actor()
        tank.set_position(position)
        tank.set_velocity(velocity)
        tank.set_text(text)
        tank.set_color(color)
        self._body.append(tank)

    def fire_bullet(self, player):
    
        bullet = Actor()
        self.player = player
        velocity = bullet.get_velocity()
        offset = velocity.reverse()
        position = bullet.get_position().add(offset)
        bullet.set_position(position)
        bullet.set_velocity(velocity)
        bullet.set_text("o")
        if self.player == 1:
            bullet.set_color(constants.BLUE)
        if self.player == 2:
            bullet.set_color(constants.RED)    
        self._bullets.append(bullet)  

