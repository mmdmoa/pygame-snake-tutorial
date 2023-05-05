In this step we'll control our snake's movements and fix
a bug!

commit link: https://github.com/mmdmoa/pygame-snake-tutorial/commit/1df0edde93ccf3e66a2c2edc2c61f040147c21da


# changes at `core.game`
### changes at `__init__` method
```python
self.rect.y += self.rect.h * 0.1
# addition
self.rect.h = self.rect.h * 0.9
```

# changes at `core.snake`
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

