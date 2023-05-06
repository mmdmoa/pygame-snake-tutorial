In this step we'll control our snake's movements and fix
a bug!

commit link: https://github.com/mmdmoa/pygame-snake-tutorial/commit/1df0edde93ccf3e66a2c2edc2c61f040147c21da


# changes at `core.game`
Upon revisiting the code, I have realized that I overlooked an important detail.
When shifting the `Game.rect` downwards, I forgot to adjust its height accordingly.
Therefore, We must now make the necessary changes to ensure that the dimensions of `Game.rect`
are accurate and aligned with the rest of the game's layout

### changes at `__init__` method
```python
self.rect.y += self.rect.h * 0.1
# addition
self.rect.h = self.rect.h * 0.9
```

# changes at `core.snake`

There was another issue with the conditions for the snake's 
teleportation when crossing the top and left edges of the game screen. 
We fixed this by changing `<=` to `<` in both `if new_head.x <= 0` and `if new_head.y <= 0`.

### changes at `move` method
```python
# change
if new_head.x < 0:
    new_head.x = grid_size.x -1

# change
if new_head.y < 0:
    new_head.y = grid_size.y -1
```
### changes at `check_events` method

In this step, we can quickly and efficiently change 
the direction of the snake based on keyboard inputs,
thanks to the `core.event_holder` module and the use of core.common.enums. 
By determining if a specific key, such as `K_UP` or `K_DOWN`, has been pressed, 
we can easily update the direction of the snake. This is a straightforward 
and simple process due to the functionality we have already implemented in previous steps.


```python
# addition *
if K_UP in cr.event_holder.pressed_keys:
    self.direction = SnakeDirection.up
if K_DOWN in cr.event_holder.pressed_keys:
    self.direction = SnakeDirection.down
if K_RIGHT in cr.event_holder.pressed_keys:
    self.direction = SnakeDirection.right
if K_LEFT in cr.event_holder.pressed_keys:
    self.direction = SnakeDirection.left
```

