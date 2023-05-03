from core.common.names import *
import core.common.resources as cr

pg.init()
cr.screen = pg.display.set_mode([800,640])

running = True
while running:
    for i in pg.event.get():
        if i.type == QUIT or i.type == KEYDOWN and i.key == K_ESCAPE:
            running = False