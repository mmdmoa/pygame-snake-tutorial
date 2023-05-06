In this step we add a tempo functionality to our `core.snake.Snake` class
,so we can control the speed of our snake relatively to game speed.

commit link: https://github.com/mmdmoa/pygame-snake-tutorial/commit/d37cab82fce22dfc6ca02a85240b2ef4c62b55ac

# changes at `core.snake`

In this step, we address the issue of the snake's speed being too fast for the player to control, 
even with a large game grid. 

Simply reducing the fps does not solve the problem as it can cause lagging. Therefore, 
we add two new integer attributes, tempo and tempo_counter, to the `Snake` class. 

These attributes allow us to slow down the snake's movement by determining if it should move 
in the current frame or not. For example, if `Snake.tempo` is set to `10` and the fps is `120`, 
the snake will move `12` times per second, which is `1/10` of the total fps. 

This enables us to slow down the snake while maintaining a high fps for smooth gameplay.

### changes at `__init__` method
```python
# addition: new `tempo` parameter 
def __init__(self,tempo:int):
    self.body: Optional[list[Vector2]] = None
    self.color: Optional[Color] = None
    self.direction: Optional[SnakeDirection] = None
    # addition
    self.tempo_counter = 0
    # addition
    self.tempo = tempo
```

### new `render` method
```python
def render( self ):
    cr.game.grid_system.cell_list.append(self.colored_body())
```
### changes at `check_events`
```python
# remove
self.move()
# remove
cr.game.grid_system.cell_list.append(self.colored_body())

# addition *
self.tempo_counter += 1
if self.tempo == self.tempo_counter:
    self.tempo_counter = 0
    self.move()
```
# changes at `core.game`
### changes at `__init__` method
```python
# change
self.snake = Snake(10)
```

### changes at `render` method
```python
# addition
self.snake.render()
```


# changes at `main`
### fps adjustment
```python
fps = 120
```