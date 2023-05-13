from core.common.names import *
import core.common.resources as cr
from core.game import Game
from core.event_holder import EventHolder


# __main__
pg.init()

# main object, main window
cr.screen = pg.display.set_mode([800,640])
cr.event_holder = EventHolder()
cr.game = Game()
# 1: type hinting
# 2: linter
# 3: typing library

# snake -> render -> screen

# main loop , game loop
while cr.event_holder.run:

    cr.event_holder.get_events()
    cr.game.check_events()
    cr.game.render()
    pg.display.update()