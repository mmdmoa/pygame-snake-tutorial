In this step we will implement the basic behaviour of our `core.game` class.

commit link: https://github.com/mmdmoa/pygame-snake-tutorial/commit/221f86ea41efb02306e97b56bf843c131ee89e7a

# changes at `core.common.resources`

In order to facilitate easy access to our game instance from other components of our program,
we will store it in `core.common.resources`, just like we did with `cr.event_holder` and `cr.screen`.

This approach allows us to create a centralized location for all of our important game components,
making it easier to manage and maintain our codebase.
By storing our game instance in `core.common.resources`,
we can easily access it from any part of our program without having
to worry about passing it around as an argument or creating unnecessary dependencies.
This improves the overall modularity and flexibility of our code.

```python
game = None
```

# changes at `core.game`

Currently, the `__init__` method of our `Game` class simply
retrieves the rectangular area of our screen and shifts its y-coordinates by 10% of its height.

This operation frees up additional space in our window,
allowing us to use it for UI elements in later stages of our project.

We also use the `Color.lerp` method to change the color values of the background color
swiftly and efficiently.
This method performs a linear interpolation between two colors
and returns a new color with the interpolated values.

```python
from core.common.names import *
import core.common.resources as cr

# We will complete this GridSystem class in the next steps, it plays a 
# crucial role in our project
from core.grid_system import GridSystem


class Game :

    def __init__( self ) :
        self.rect = cr.screen.get_rect()
        self.rect.y += self.rect.h * 0.1


    def check_events( self ) :
        ...


    def render( self ) :
        cr.screen.fill("gray")
        pg.draw.rect(cr.screen, Color("gray").lerp("black", 0.5), self.rect)
```

# changes at `core.grid_system`

The `core.grid_system` module is used to create a grid table that allows us to manage 
the movements and collisions of our game entities, such as the `Snake` and `Food`. 
The grid system is an essential part of our program as 
it enables us to render these entities and ensures that they are properly positioned on the screen.

```python
from core.common.names import *
import core.common.resources as cr

class GridSystem :

    def __init__( self ) :
        ...
```

# changes at `main`

With the implementation of `core.game`, 
the final step is to import it in main and create an instance of it. 
This instance will be assigned to a name in core.common.resources, 
allowing easy access throughout the program. 

In each iteration of the main loop, 
we simply need to call the `Game.check_events` and `Game.render` methods 
to handle the game's events and rendering.


### new import statement

```python
from core.game import Game 
```

### new screen size and initializing `cr.game`

```python
cr.screen = pg.display.set_mode([900, 740])
cr.game = Game()
```

### new statements in the main loop

```python
cr.event_holder.get_events()
cr.game.check_events()
cr.game.render()
pg.display.update()
```

