from core.common.names import *

class EventHolder :
    def __init__( self ) :
        self.pressed_keys = []
        self.released_keys = []
        self.held_keys = []
        self.should_quit = False

    def get_events( self ):
        self.pressed_keys.clear()
        self.released_keys.clear()

        for i in pg.event.get():
            if i.type == QUIT:
                self.should_quit = True

            if i.type == KEYDOWN:
                self.pressed_keys.append(i.key)
                self.held_keys.append(i.key)

            if i.type == KEYUP:
                self.released_keys.append(i.key)
                if i.key in self.held_keys:
                    self.held_keys.remove(i.key)