from core.common.names import *
import core.common.resources as cr

from core.event_holder import EventHolder
from core.game import Game

pg.init()
cr.screen = pg.display.set_mode([900,740])
cr.event_holder = EventHolder()
cr.game = Game()

while not cr.event_holder.should_quit:

    if K_ESCAPE in cr.event_holder.released_keys:
        cr.event_holder.should_quit = True

    cr.event_holder.get_events()

    cr.game.check_events()
    cr.game.render()
    pg.display.update()
