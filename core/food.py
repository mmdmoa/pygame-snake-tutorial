from core.common.names import *
import core.common.resources as cr

class Food:
    def __init__(self):
        self.is_eaten = False
        self.pos: Optional[Vector2] = None
        self.color: Optional[Color] = None

    def start( self ):
        self.color = Color("green").lerp("black",0.5)
        self.spawn()


    def spawn( self ):
        self.is_eaten = False
        w,h = cr.game.grid_system.grid_size
        self.pos = Vector2(random.randint(0,w-1),random.randint(0,h-1))


    def check_events( self ):
        if self.is_eaten:
            self.spawn()

    def render( self ):
        colored_self = (self.pos,self.color)
        cr.game.grid_system.cell_list.append([colored_self])