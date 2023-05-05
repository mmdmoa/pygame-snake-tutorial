In this step we add a tempo functionality to our `core.snake.Snake` class
,so we can control the speed of our snake relatively to game speed.

commit link: https://github.com/mmdmoa/pygame-snake-tutorial/commit/d37cab82fce22dfc6ca02a85240b2ef4c62b55ac

# changes at `core.snake`
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