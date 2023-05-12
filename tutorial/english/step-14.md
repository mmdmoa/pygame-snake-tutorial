In this step we'll do some polishing to improve the game play and mechanics.

commit link: https://github.com/mmdmoa/pygame-snake-tutorial/commit/4eca7242371934eae48908f7a29b8c6814f34802


# changes at `core.snake`

### new `check_movements` method

```python
def check_movements( self ) :
    # addition {
    head = self.body[-1]
    neck = self.body[-2]
    neck_direction = SnakeDirection.down

    if head.x < neck.x :
        neck_direction = SnakeDirection.right
    elif head.x > neck.x :
        neck_direction = SnakeDirection.left
    elif head.y > neck.y :
        neck_direction = SnakeDirection.up
    # }

    # migrated from `check_events` method *
    # change
    if K_UP in cr.event_holder.pressed_keys and neck_direction != SnakeDirection.up :
        self.direction = SnakeDirection.up
    # change
    if K_DOWN in cr.event_holder.pressed_keys and neck_direction != SnakeDirection.down :
        self.direction = SnakeDirection.down
    # change
    if K_RIGHT in cr.event_holder.pressed_keys and neck_direction != SnakeDirection.right :
        self.direction = SnakeDirection.right
    # change
    if K_LEFT in cr.event_holder.pressed_keys and neck_direction != SnakeDirection.left :
        self.direction = SnakeDirection.left


```

### changes at `check_events` method

```python
def check_events( self ) :
    self.check_movements()

    self.tempo_counter += 1
    if self.tempo == self.tempo_counter :
        self.tempo_counter = 0
```