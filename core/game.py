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

        self.score = 0
        self.high_score = 0
        self.grid_system = GridSystem(self.rect,Vector2(12*4,10*4))
        self.snake = Snake(10)
        self.food = Food()

    @property
    def score_text( self ):
        return cr.normal_font.render(f"score: {self.score}",False, "black")

    @property
    def high_score_text( self ) :
        return cr.small_font.render(f"high score: {self.high_score}", False, "black")

    def check_high_score( self ):
        if self.score > self.high_score:
            self.high_score = self.score

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

        score_text = self.score_text
        score_rect = score_text.get_rect()
        score_rect.center = self.ui_rect.center

        cr.screen.blit(score_text,score_rect)

        high_score_text = self.high_score_text
        high_score_rect = high_score_text.get_rect()
        high_score_rect.center = self.ui_rect.center
        high_score_rect.x = self.ui_rect.w*0.99 - high_score_rect.w

        cr.screen.blit(high_score_text, high_score_rect)


        self.snake.render()
        self.food.render()
        self.grid_system.render()