# fetch
from core.common.names import *

# SnakeCase
class EventHolder:
    def __init__(self):
        self.run = True
        # press, f
        self.pressed_keys = []
        # hold, f 10
        self.held_keys = []
        # release ,f 10 >
        self.released_keys = []


    def get_events( self ):
        self.pressed_keys.clear()
        self.released_keys.clear()

        for event in pg.event.get():
            if event.type == QUIT:
                self.run = False

            if event.type == KEYDOWN:
                self.pressed_keys.append(event.key)

            if event.type == KEYUP :
                self.released_keys.append(event.key)



