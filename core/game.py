from core.common.names import *
import core.common.resources as cr
from core.grid_system import GridSystem

class Game:
    def __init__(self):
        self.game_color = Color(190,190,220)
        self.ui_color = Color(190,190,220).lerp('black',0.1)


        self.game_rect = cr.screen.get_rect()

        self.game_rect.y += self.game_rect.h * 0.1
        self.game_rect.h -= self.game_rect.h * 0.1

        self.ui_rect = cr.screen.get_rect()
        self.ui_rect.h = self.ui_rect.h * 0.1

        self.grid_system = GridSystem(self.game_rect,Vector2(15,12))


    # get_events : event_holder
    # check_events & process, update
    # render

    def check_events( self ):
        ...


    def render( self ):
        cr.screen.fill("white")
        pg.draw.rect(cr.screen,self.game_color,self.game_rect)
        pg.draw.rect(cr.screen,self.ui_color,self.ui_rect)
        self.grid_system.render()
