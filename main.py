from core.common.names import *
import core.common.resources as cr

from core.event_holder import EventHolder

pg.init()
cr.screen = pg.display.set_mode([800,640])
cr.event_holder = EventHolder()

while not cr.event_holder.should_quit:

    if K_ESCAPE in cr.event_holder.released_keys:
        cr.event_holder.should_quit = True

    cr.event_holder.get_events()