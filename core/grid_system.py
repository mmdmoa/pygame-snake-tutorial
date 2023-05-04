from core.common.names import *
import core.common.resources as cr

class GridSystem:
    def __init__(self,rect:FRect,grid_size:Vector2):
        self.rect = rect
        self.grid_size = grid_size
        self.x_step = self.rect.w / grid_size.x
        self.y_step = self.rect.h / grid_size.y

    def render( self ):
        for x in range(int(self.grid_size.x)):
            x *= self.x_step
            x += self.rect.x
            pg.draw.line(cr.screen,"black",(x,self.rect.y),(x,self.rect.y+self.rect.h))

        for y in range(int(self.grid_size.y)):
            y *= self.y_step
            y += self.rect.y
            pg.draw.line(cr.screen,"black",(self.rect.x,y),(self.rect.x+self.rect.w,y))