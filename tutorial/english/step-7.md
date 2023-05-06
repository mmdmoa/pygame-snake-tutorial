In this step, we will be adding a `pygame.time.Clock` object to our `main` file. 
This object is used to control the framerate of the game, 
and therefore, the speed of the game. 
It works by regulating the amount of time that elapses between each frame of the game, 
which ensures that the game runs smoothly and consistently.



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
