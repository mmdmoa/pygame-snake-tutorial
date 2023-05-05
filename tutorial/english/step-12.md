In this step we will implement and create our `core.food` class.

commit link: https://github.com/mmdmoa/pygame-snake-tutorial/commit/e7bd01a8b6415750065a6da66dd1403888e6d982

# changes at `core.common.names`

### new import statement

```python
import random
```

# changes at `core.food`

### new import statements

```python
from core.common.names import *
import core.common.resources as cr
```

## new `core.food.Food` class

### new `__init__` method

```python
class Food :
    def __init__( self ) :
        self.is_eaten = False
        self.pos: Optional[Vector2] = None
        self.color: Optional[Color] = None
```

### new `start` method

```python
def start( self ) :
    self.color = Color("green").lerp("black", 0.5)
    self.spawn()
```

### new `spawn` method

```python
def spawn( self ) :
    self.is_eaten = False
    w, h = cr.game.grid_system.grid_size
    self.pos = Vector2(random.randint(0, w - 1), random.randint(0, h - 1))
```

### new `check_events` method

```python
def check_events( self ) :
    if self.is_eaten :
        self.spawn()
```

### new `render` method

```python
def render( self ) :
    colored_self = (self.pos, self.color)
    cr.game.grid_system.cell_list.append([colored_self])
```

# changes at `core.game`

### new import statement

```python
from core.food import Food
```

### changes at `__init__` method

```python
# addition
self.food = Food()
```

### changes at `start` method

```python
# addition
self.food.start()
```

### changes at `check_events` method

```python
# addition
self.food.check_events()
```

### changes at `render` method

```python
self.snake.render()
# addition
self.food.render()
self.grid_system.render()
```

# changes at `core.snake`

### changes at `has_eaten_food` method
```python
def has_eaten_food( self ):
    # addition
    return self.body[-1] == cr.game.food.pos
```

### changes at `move` method
```python
if not self.has_eaten_food():
    self.body.pop(0)
# addition
else:
    # addition
    cr.game.food.is_eaten = True
```

