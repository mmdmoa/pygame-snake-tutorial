from core.common.names import *
import core.common.resources as cr


class Game:
    def __init__(self):
        self.trigger = False

    def render( self ):
        if K_f in cr.event_holder.pressed_keys:
            self.trigger = not self.trigger

        color = 'red'
        if self.trigger:
            color = 'blue'

        cr.screen.fill(color)
