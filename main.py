from core.common.names import *
import core.common.resources as cr
from core.game import Game


# __main__
pg.init()

# main object, main window
cr.screen = pg.display.set_mode([800,640])

# 1: type hinting
# 2: linter
# 3: typing library

# snake -> render -> screen
game = Game()

run = True

# main loop , game loop
while run:

    for i in pg.event.get():
        if i.type == QUIT:
            run = False

    game.render()
    pg.display.update()