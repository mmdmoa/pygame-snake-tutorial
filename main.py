from core.common.names import *
import core.common.resources as cr

from core.event_holder import EventHolder
from core.game import Game

pg.init()
cr.screen = pg.display.set_mode([900,740])
cr.event_holder = EventHolder()
cr.small_font = pg.font.SysFont('monospace',25)
cr.normal_font = pg.font.SysFont('monospace',35)
cr.game = Game()
cr.game.start()



def get_fps_text():
    return cr.small_font.render(f"FPS: {round(final_fps)}",False, "black")

fps = 120
final_fps = 0
clock = pg.time.Clock()

while not cr.event_holder.should_quit:

    if K_ESCAPE in cr.event_holder.released_keys:
        cr.event_holder.should_quit = True

    if K_F3 in cr.event_holder.pressed_keys:
        cr.event_holder.should_render_debug = not cr.event_holder.should_render_debug

    cr.event_holder.get_events()

    cr.game.check_events()
    cr.game.render()

    fps_text = get_fps_text()
    fps_rect = fps_text.get_rect()
    fps_rect.center = cr.game.ui_rect.center
    fps_rect.x = cr.game.ui_rect.x
    fps_rect.x += cr.game.ui_rect.w * 0.01

    cr.screen.blit(fps_text,fps_rect)


    pg.display.update()

    clock.tick(fps)
    final_fps = clock.get_fps()