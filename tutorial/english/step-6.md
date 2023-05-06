In this step we will create and implement our `core.snake` class.

commit link: https://github.com/mmdmoa/pygame-snake-tutorial/commit/e79a12f1d36cc52cc5ff7d7a2355c11700108e36

# changes at `core.common.enums`

### new import statement

We're going to need some enum values for our snake movements, and here we are.
making them.

By utilizing the `enum.Enum` class,
we can define a set of named values that are unique and easily accessible
as enums throughout our codebase.
This can increase code clarity and reduce the likelihood of typos and value errors.

```python
from enum import Enum
```

### new `SnakeDirection` enum class

```python
class SnakeDirection(Enum) :
    up = 'up'
    down = 'down'
    right = 'right'
    left = 'left'
```

# changes at `core.snake`

### new import statements

```python
from core.common.names import *
from core.common.enums import *
import core.common.resources as cr
```

## new `Snake` class

The body of our snake is a `list` of `Vector2` objects that represent the coordinates 
of the snake's body parts. Additionally, the snake has a `color` attribute that determines its color, 
as well as a `direction` attribute that determines the snake's current heading.

As we are using a special method to share important data globally in the `core.common.resources` class, 
and creating our `Snake` from within the `Game` class, 
it is currently not possible to access anything inside the `Game` class through `core.common.resources`, 
as the `core.common.resources.game` attribute has not been assigned yet.

So if there are any adjustments that have to be made according to uninitialized components 
of the `Game` class, they have to be made after those components have been initialized. 
This is the reason for creating the start method.

Additionally, the reset method serves to reset the snake state, 
allowing the snake to be repositioned to its initial state, in the event of losing the game.

The `colored_body` attribute is responsible for mapping each cell of the 
snake's body to its corresponding color, and then adding the resulting pairs to 
`GridSystem.cell_list` to enable rendering. 
Currently, this process is carried out temporarily within the `Snake.check_events` method.

### new `__init__` method

```python
class Snake :

    def __init__( self ) :
        self.body: Optional[list[Vector2]] = None
        self.color: Optional[Color] = None
        self.direction: Optional[SnakeDirection] = None
```

### new `start` method

```python
def start( self ) :
    self.reset()
```

### new `colored_body` method

```python
def colored_body( self ) :
    return [(i, self.color) for i in self.body]
```

### new `reset` method

```python
def reset( self ) :
    gp = cr.game.grid_system.grid_size
    x, y = gp.x // 2, gp.y // 2
    self.body = [Vector2(x + i, y) for i in [-3, -2, -1, 0]]
    self.color = Color("red").lerp("black", 0.5)
    self.direction: SnakeDirection = SnakeDirection.right
```

### new `check_events` method

```python
def check_events( self ) :
    cr.game.grid_system.cell_list.append(self.colored_body())
```



# changes at `core.game`

We have completed the `Snake` class and can now create it as an attribute in our `Game` class. 
We'll call its methods as needed. 
Additionally, we made some adjustments to the background color of the game.

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
def start( self ) :
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
pg.draw.rect(cr.screen, Color("white").lerp("blue", 0.28), self.rect)
```

# changes at `main`

```python
cr.game = Game()
# addition
cr.game.start()

while not cr.event_holder.should_quit :
```