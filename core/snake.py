from core.common.names import *
from core.common.enums import *
import core.common.resources as cr

class Snake:
    def __init__(self,tempo:int):
        self.body: Optional[list[Vector2]] = None
        self.body_color: Optional[Color] = None
        self.head_color: Optional[Color] = None
        self.direction: Optional[SnakeDirection] = None
        self.tempo_counter = 0
        self.tempo = tempo

    def start( self ):
        self.reset()

    def colored_body( self ):
        return [(i,self.body_color) for i in self.body[:-1]] + \
               [(self.body[-1], self.head_color)]

    def reset( self ):
        gp = cr.game.grid_system.grid_size
        x,y = gp.x // 2, gp.y // 2
        self.body = [Vector2(x+i,y) for i in [-3,-2,-1,0]]
        self.body_color = Color("red").lerp("black",0.5)
        self.head_color = Color("red").lerp("black",0.65)
        self.direction: SnakeDirection = SnakeDirection.right

    def has_eaten_food( self ):
        return self.body[-1] == cr.game.food.pos

    def has_eaten_self( self ):
        return self.body[-1] in self.body[:-1]


    def move( self ):
        grid_size = cr.game.grid_system.grid_size
        head = self.body[-1]
        movement = Vector2(0,0)

        if self.direction == SnakeDirection.up:
            movement.y -= 1
        elif self.direction == SnakeDirection.down:
            movement.y += 1
        elif self.direction == SnakeDirection.right:
            movement.x += 1
        elif self.direction == SnakeDirection.left:
            movement.x -= 1

        new_head = Vector2(head.x+movement.x,head.y+movement.y)

        if new_head.x < 0:
            new_head.x = grid_size.x -1
        if new_head.y < 0:
            new_head.y = grid_size.y -1

        if new_head.x > grid_size.x - 1:
            new_head.x = 0
        if new_head.y > grid_size.y - 1:
            new_head.y = 0

        self.body.append(new_head)

        if not self.has_eaten_food():
            self.body.pop(0)
        else:
            cr.game.food.is_eaten = True

        if self.has_eaten_self():
            self.reset()
            cr.game.food.spawn()

    def render( self ):
        cr.game.grid_system.cell_list.append(self.colored_body())

    def check_movements( self ):
        head = self.body[-1]
        neck = self.body[-2]
        neck_direction = SnakeDirection.down

        if head.x < neck.x :
            neck_direction = SnakeDirection.right
        elif head.x > neck.x :
            neck_direction = SnakeDirection.left
        elif head.y > neck.y :
            neck_direction = SnakeDirection.up

        if K_UP in cr.event_holder.pressed_keys and neck_direction != SnakeDirection.up :
            self.direction = SnakeDirection.up
        if K_DOWN in cr.event_holder.pressed_keys and neck_direction != SnakeDirection.down :
            self.direction = SnakeDirection.down
        if K_RIGHT in cr.event_holder.pressed_keys and neck_direction != SnakeDirection.right :
            self.direction = SnakeDirection.right
        if K_LEFT in cr.event_holder.pressed_keys and neck_direction != SnakeDirection.left :
            self.direction = SnakeDirection.left

    def check_events( self ):
        self.check_movements()

        self.tempo_counter += 1
        if self.tempo == self.tempo_counter:
            self.tempo_counter = 0
            self.move()
