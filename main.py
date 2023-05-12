from core.common.names import *
import core.common.resources as cr
from core.game import Game
from core.event_holder import EventHolder


# __main__
pg.init()

# main object, main window
cr.screen = pg.display.set_mode([800,640])
cr.event_holder = EventHolder()
# 1: type hinting
# 2: linter
# 3: typing library

# snake -> render -> screen
game = Game()

# main loop , game loop
while cr.event_holder.run:

    cr.event_holder.get_events()

    game.render()
    pg.display.update()