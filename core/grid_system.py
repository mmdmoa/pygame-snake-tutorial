from core.common.names import *
import core.common.resources as cr

class GridSystem:
    def __init__(self,rect:Rect,grid_size:Vector2):
        self.rect = rect
        self.grid_size = grid_size

        self.step_x = self.rect.w / self.grid_size.x
        self.step_y = self.rect.h / self.grid_size.y


    def render( self ):
        # grid_size , x: 15, y: 12
        for x in range(int(self.grid_size.x)): # range(15) | 0 , 1 , 2 , 3 -> 14
            x *= self.step_x
            x += self.rect.x
            pg.draw.line(cr.screen,"black",(x,self.rect.y),(x,self.rect.y+self.rect.h))

        for y in range(int(self.grid_size.y)): # range(15) | 0 , 1 , 2 , 3 -> 14
            y *= self.step_y
            y += self.rect.y
            pg.draw.line(cr.screen,"black",(self.rect.x,y),(self.rect.x+self.rect.w,y))