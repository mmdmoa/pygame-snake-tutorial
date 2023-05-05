In this step we will add a `pygame.time.Clock` object to our `main` file in order 
to control the FPS and the speed of the game.

commit link https://github.com/mmdmoa/pygame-snake-tutorial/commit/acc243b0c1ab8e7ff42e6a660d9deb6c322d4d8a

# changes at `main`

### new attributes
```python
cr.game = Game()
cr.game.start()

# addition
fps = 60
# addition
clock = pg.time.Clock()
```

### new statement in the main loop
```python
cr.game.render()
pg.display.update()
# addition
clock.tick(fps)
```
