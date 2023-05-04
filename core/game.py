from core.common.names import *
import core.common.resources as cr

from core.grid_system import GridSystem

class Game:
    def __init__( self ):
        self.rect = cr.screen.get_rect()
        self.rect.y += self.rect.h * 0.1
    
    def check_events( self ):
        ...

    def render( self ):
        cr.screen.fill("gray")
        pg.draw.rect(cr.screen,Color("gray").lerp("black",0.5),self.rect)
