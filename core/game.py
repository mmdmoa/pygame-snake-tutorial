from core.common.names import *
import core.common.resources as cr

from core.grid_system import GridSystem

class Game:
    def __init__( self ):
        self.rect = FRect(cr.screen.get_rect())
        self.rect.y += self.rect.h * 0.1
        self.grid_system = GridSystem(self.rect,Vector2(12*5,10*5))
    
    def check_events( self ):
        ...

    def render( self ):
        cr.screen.fill("gray")
        pg.draw.rect(cr.screen,Color("gray").lerp("black",0.5),self.rect)

        self.grid_system.render()