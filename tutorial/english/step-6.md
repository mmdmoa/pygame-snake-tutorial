In this step we will create and implement our `core.snake` class.

commit link: https://github.com/mmdmoa/pygame-snake-tutorial/commit/e79a12f1d36cc52cc5ff7d7a2355c11700108e36

# changes at `core.common.enums`
### new import statement 
```python
from enum import Enum
```

### new `SnakeDirection` enum class
```python
class SnakeDirection(Enum):
    up = 'up'
    down = 'down'
    right = 'right'
    left = 'left'
```

# changes at `core.game`

### new import statement
```python
from core.snake import Snake
```
### changes at `__init__` method

```python
# addition
self.snake = Snake()
```

### new `start` method
```python
def start( self ):
    self.snake.start()
```

### changes at `check_events` method
```python
# addition *
self.grid_system.cell_list.clear()
self.snake.check_events()
```

### changes at `render` method
```python
# change
pg.draw.rect(cr.screen,Color("white").lerp("blue",0.28),self.rect)
```


# changes at `core.snake`

### new import statements
```python
from core.common.names import *
from core.common.enums import *
import core.common.resources as cr
```

## new `Snake` class
### new `__init__` method
```python
class Snake:
    def __init__(self):
        self.body: Optional[list[Vector2]] = None
        self.color: Optional[Color] = None
        self.direction: Optional[SnakeDirection] = None
```
### new `start` method
```python
def start( self ):
    self.reset()
```
### new `colored_body` method
```python
def colored_body( self ):
    return [(i,self.color) for i in self.body]
```
### new `reset` method
```python
def reset( self ):
    gp = cr.game.grid_system.grid_size
    x,y = gp.x // 2, gp.y // 2
    self.body = [Vector2(x+i,y) for i in [-3,-2,-1,0]]
    self.color = Color("red").lerp("black",0.5)
    self.direction: SnakeDirection = SnakeDirection.right
```
### new `check_events` method
```python
def check_events( self ):
    cr.game.grid_system.cell_list.append(self.colored_body())
```

# changes at `main`

```python
cr.game = Game()
# addition
cr.game.start()

while not cr.event_holder.should_quit:
```