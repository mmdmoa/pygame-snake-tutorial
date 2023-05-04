from core.common.names import *
from core.common.enums import *
import core.common.resources as cr

class Snake:
    def __init__(self):
        self.body: Optional[list[Vector2]] = None
        self.color: Optional[Color] = None
        self.direction: Optional[SnakeDirection] = None

    def start( self ):
        self.reset()

    def colored_body( self ):
        return [(i,self.color) for i in self.body]

    def reset( self ):
        gp = cr.game.grid_system.grid_size
        x,y = gp.x // 2, gp.y // 2
        self.body = [Vector2(x+i,y) for i in [-3,-2,-1,0]]
        self.color = Color("red").lerp("black",0.5)
        self.direction: SnakeDirection = SnakeDirection.right

    def check_events( self ):
        cr.game.grid_system.cell_list.append(self.colored_body())