In this step we will add a text in the top left corner
of our screen that is going to show the fps.

commit link: https://github.com/mmdmoa/pygame-snake-tutorial/commit/1e2e589444664e9659926c28debdaa537e997a2b


# changes at `core.common.resources`

### new attribute

```python
game = None
# addition
fps_font: Optional[pg.font.Font] = None
```

# changes at `core.game`

### changes at `__init__` method

```python
self.rect = FRect(cr.screen.get_rect())
# addition
self.ui_rect = self.rect.copy()
self.rect.y += self.rect.h * 0.1
self.rect.h = self.rect.h * 0.9
# addition
self.ui_rect.h = self.ui_rect.h * 0.1
```

# changes at `main`

### new attributes and function
```python
# addition
cr.fps_font = pg.font.SysFont('monospace',25)

# addition
def get_fps_text():
    return cr.fps_font.render(f"FPS: {round(final_fps)}",False, "black")

fps = 120
# addition
final_fps = 0
clock = pg.time.Clock()
```

### changes in the main loop
```python
cr.game.check_events()
cr.game.render()

# addition {
fps_text = get_fps_text()
fps_rect = fps_text.get_rect()
fps_rect.x = cr.game.ui_rect.x
fps_rect.y = cr.game.ui_rect.y
cr.screen.blit(fps_text,fps_rect)
# }
pg.display.update()

clock.tick(fps)
# addition
final_fps = clock.get_fps()
```

