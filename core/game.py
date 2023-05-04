from core.common.names import *
import core.common.resources as cr

from core.grid_system import GridSystem
from core.snake import Snake

class Game:
    def __init__( self ):
        self.rect = FRect(cr.screen.get_rect())
        self.rect.y += self.rect.h * 0.1
        self.rect.h = self.rect.h * 0.9
        self.grid_system = GridSystem(self.rect,Vector2(12*2,10*2))
        self.snake = Snake()

    def start( self ):
        self.snake.start()

    def check_events( self ):
        self.grid_system.cell_list.clear()
        self.snake.check_events()

    def render( self ):
        cr.screen.fill("gray")
        pg.draw.rect(cr.screen,Color("white").lerp("blue",0.28),self.rect)

        self.grid_system.render()