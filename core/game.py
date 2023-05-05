from core.common.names import *
import core.common.resources as cr

from core.grid_system import GridSystem
from core.snake import Snake
from core.food import Food

class Game:
    def __init__( self ):
        self.rect = FRect(cr.screen.get_rect())
        self.ui_rect = self.rect.copy()
        self.rect.y += self.rect.h * 0.1
        self.rect.h = self.rect.h * 0.9
        self.ui_rect.h = self.ui_rect.h * 0.1

        self.grid_system = GridSystem(self.rect,Vector2(12*4,10*4))
        self.snake = Snake(10)
        self.food = Food()

    def start( self ):
        self.snake.start()
        self.food.start()

    def check_events( self ):
        self.grid_system.cell_list.clear()
        self.snake.check_events()
        self.food.check_events()

    def render( self ):
        cr.screen.fill("gray")
        pg.draw.rect(cr.screen,Color("white").lerp("blue",0.28),self.rect)

        self.snake.render()
        self.food.render()
        self.grid_system.render()